
from user import UserProfile
from storage import Storage, StorageItem

class Recommender:

    __storage: list[StorageItem] = []

    def recommend(self, user_profile: UserProfile) -> list[StorageItem] :
        pass

    def load_storage(self, storage: Storage) -> None :
        self.__storage = storage.get_data()