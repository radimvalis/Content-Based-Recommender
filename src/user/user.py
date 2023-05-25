
from storage import StorageItem

class UserProfile:

    def __init__(self, username: str, view_history: list[StorageItem] = None, history_limit: int = 5) -> None:
        self.__username = username
        self.__view_history = view_history if view_history is not None else []
        self.__history_limit = history_limit

    @property
    def username(self) -> str:
        return self.__username

    @property
    def preferences(self) -> set[str]:
        preferences = set()
        for item in self.__view_history:
            for keyword in item.keywords:
                preferences.add(keyword)

        return preferences
    
    @property
    def view_history(self) -> set[StorageItem]:
        return self.__view_history
    
    @property
    def history_limit(self) -> int:
        return self.__history_limit
    
    def update_view_history(self, viewed_item: StorageItem) -> None:
        if len(self.__view_history) >= self.__history_limit:
            self.__view_history.pop(0)

        self.__view_history.append(viewed_item)