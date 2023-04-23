
from abc import ABC, abstractmethod

class StorageItem:

    def __init__(self, keywords: list[str], url: str, title: str | None = None) -> None :
        self.__keywords = keywords
        self.__url = url
        self.__title = title

    def keywords(self) -> list[str] :
        return self.__keywords
    
    def url(self) -> str :
        return self.__url
    
    def title(self) -> str | None :
        return self.__title


class Storage(ABC):
    
    @abstractmethod
    def get_data(self) -> list[StorageItem] :
        pass