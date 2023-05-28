
class Item:

    def __init__(self, title: str, url: str,  keywords: list[str] | set[str]) -> None:
        self.__url = url
        self.__title = title
        self.__keywords = set(keywords)
    
    @property
    def url(self) -> str :
        return self.__url
    
    @property
    def title(self) -> str:
        return self.__title
    
    @property
    def keywords(self) -> set[str]:
        return self.__keywords