
from abc import ABC, abstractmethod

class StorageItem:

    def __init__(self, title: str, url: str,  keywords: list[str] | set[str]) -> None:
        self.__url = url
        self.__title = title
        self.__keywords = set(keywords)
    
    def url(self) -> str :
        return self.__url
    
    def title(self) -> str:
        return self.__title
    
    def keywords(self) -> set[str]:
        return self.__keywords

class Storage(ABC):
    
    @abstractmethod
    def get_data(self) -> list[StorageItem]:
        pass