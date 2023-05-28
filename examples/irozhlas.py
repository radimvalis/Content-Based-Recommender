
from cbr import Cbr, CbrConfig, Item
from datetime import datetime, timedelta
from aiohttp import ClientSession
from bs4 import BeautifulSoup
import asyncio

class ProgressBar:

    def __init__(self, message: str, tasks_count: int) -> None:
        self.__message = message
        self.__tasks_count = tasks_count
        self.__completed_tasks_count = 0
    
    def make_progress(self):
        self.__completed_tasks_count += 1
        if self.__completed_tasks_count <= self.__tasks_count:
            print(f"{self.__message}: {self.__completed_tasks_count} / {self.__tasks_count}", end="\r", flush=True)
        else:
            print("Loading completed", flush=True)


class IRozhlas:

    ARTICLE_BASE_URL = "https://www.irozhlas.cz"
    ARCHIVE_BASE_URL = "https://www.irozhlas.cz/zpravy-archiv/"
    DAYS_COUNT = 14

    def get_archive_urls():
        archive_urls = []
        today = datetime.now()
        for i in range(IRozhlas.DAYS_COUNT):
            date = (today - timedelta(days=i)).date()
            archive_url = IRozhlas.ARCHIVE_BASE_URL + (str)(date)
            archive_urls.append(archive_url)
        
        return archive_urls
    
    async def create_article_item(article_url: str, session: ClientSession):
        async with session.get(article_url) as response:
            article_html = await response.text()
        article_soup = BeautifulSoup(article_html, "html.parser")
        nav_node = article_soup.find("nav", {"class": "m-breadcrumb"})
        if nav_node == None:
            return None
        
        keywords = [kw.text for kw in nav_node.css.select('a[href*="zpravy-tag"]')]
        if len(keywords) == 0:
            return None
        
        title = article_soup.find("title").text[:-31]
        return Item(title, article_url, keywords)

    async def extract_links_to_articles(archive_url: str, session: ClientSession):
        async with session.get(archive_url) as response:
            archive_html = await response.text()
        archive_soup = BeautifulSoup(archive_html, "html.parser")
        link_nodes = archive_soup.find_all("a", {"class": "b-article__link"})
        return [IRozhlas.ARTICLE_BASE_URL + a["href"] for a in link_nodes]
    
    async def create_storage():
        async with ClientSession() as session:
            archive_urls = IRozhlas.get_archive_urls()
            archives_tasks = []
            for archive_url in archive_urls:
                task = asyncio.ensure_future(IRozhlas.extract_links_to_articles(archive_url, session))
                archives_tasks.append(task)

            archive_progress_bar = ProgressBar("Loading archives", len(archives_tasks))
            for result in asyncio.as_completed(archives_tasks):
                await result
                archive_progress_bar.make_progress()
        
            articles_per_day = await asyncio.gather(*archives_tasks, return_exceptions=True)
            articles_tasks = []
            for day in articles_per_day:
                for article_url in day:
                    task = asyncio.ensure_future(IRozhlas.create_article_item(article_url, session))
                    articles_tasks.append(task)
            
            articles_progress_bar = ProgressBar("Loading articles", len(articles_tasks))
            for result in asyncio.as_completed(articles_tasks):
                await result
                articles_progress_bar.make_progress()

            storage_items = await asyncio.gather(*articles_tasks, return_exceptions=True)
            return [i for i in storage_items if i != None]

    def get_data() -> list[Item]:
        return asyncio.get_event_loop().run_until_complete(IRozhlas.create_storage())
    
def main():
    CbrConfig.items = IRozhlas.get_data()
    CbrConfig.users_path = "users-irozhlas.json"
    Cbr.run()

if __name__ == "__main__":
    main()