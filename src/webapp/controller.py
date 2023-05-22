
from recommender import Recommender
from user import UserProfile, UserProfileSerializer
from storage import StorageItem
from config import STORAGE, MAX_VIEW_HISTORY_LEN

class UserProfileProxy:

    def __init__(self, user: UserProfile) -> None:
        self.__real_user = user
        self.__recommended_items: list[StorageItem] = []
        self.__updated_view_history: bool = True
        self.__next_item_idx = -1
    
    @property
    def user(self) -> UserProfile:
        return self.__real_user

    @property
    def username(self) -> str:
        return self.__real_user.username

    @property
    def updated_view_history(self) -> bool:
        return self.__updated_view_history
    
    @updated_view_history.setter
    def updated_view_history(self, updated: bool) -> None:
        self.__updated_view_history = updated

    @property
    def recommended_items(self) -> list[StorageItem]:
        return self.__recommended_items
    
    @recommended_items.setter
    def recommended_items(self, recommended_items: list[StorageItem]) -> None:
        self.__recommended_items = recommended_items
        self.__updated_view_history = False
        self.__next_item_idx = -1
    
    def update_view_history(self, viewed_item: StorageItem) -> None:
        self.__real_user.update_view_history(viewed_item)
        self.__updated_view_history = True
    
    def next_recommended_item(self) -> StorageItem:
        self.__next_item_idx += 1
        if self.__next_item_idx >= len(self.__recommended_items):
            self.__next_item_idx = 0
            
        return self.__recommended_items[self.__next_item_idx] 


class RecommenderController:

    def __init__(self) -> None:
        self.__user_proxies: list[UserProfileProxy] = self.__load_user_proxies()
        self.__current_user_proxy: UserProfileProxy = None
        self.__recommender = Recommender()
        self.__recommender.load_storage(STORAGE())

    @property
    def users(self) -> list[str]:
        return [up.username for up in self.__user_proxies]
    
    @property
    def current_user(self) -> str:
        return self.__current_user_proxy.username

    def set_current_user(self, username: str) -> bool:
        if self.__current_user_proxy != None:
            self.__current_user_proxy.updated_view_history = True

        for up in self.__user_proxies:
            if up.username == username:
                self.__current_user_proxy = up
                return True
           
        return False

    def create_user(self, username: str) -> bool:
        if any(up.username == username for up in self.__user_proxies):
            return False
        
        new_user_proxy = UserProfileProxy(UserProfile(username, max_view_history_len=MAX_VIEW_HISTORY_LEN))
        self.__user_proxies.append(new_user_proxy)
        self.__current_user_proxy = new_user_proxy
        self.__save_user_proxies()
        return True
    
    def delete_user(self, username: str) -> bool:
        for i, up in enumerate(self.__user_proxies):
            if up.username == username:
                self.__user_proxies.pop(i)
                self.__save_user_proxies()
                return True
        
        return False

    def update_view_history(self, username: str, item_title: str) -> bool:
        if self.__current_user_proxy.username == username:
            for item in self.__current_user_proxy.recommended_items:
                if item.title == item_title:
                    self.__current_user_proxy.update_view_history(item)
                    self.__save_user_proxies()
                    return True
        
        return False

    def get_recommendation_for(self, username: str) -> list[StorageItem] | None:
        if self.__current_user_proxy.username == username:
            if self.__current_user_proxy.updated_view_history:
                new_recommended_items = self.__recommender.recommend_to(self.__current_user_proxy.user)
                self.__current_user_proxy.recommended_items = new_recommended_items

            return [self.__current_user_proxy.next_recommended_item() for _ in range(5)] 

        return None
    
    def __load_user_proxies(self):
        return [UserProfileProxy(u) for u in UserProfileSerializer.load_users()]

    def __save_user_proxies(self):
        UserProfileSerializer.save_users([up.user for up in self.__user_proxies])

controller = RecommenderController()