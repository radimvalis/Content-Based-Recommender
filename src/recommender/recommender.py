
from user import UserProfile
from storage import Storage, StorageItem

class Recommender:

    def __init__(self) -> None:
        self.__storage: list[StorageItem] = []

    def recommend_to(self, user_profile: UserProfile, recommendations_limit: int = 100) -> list[StorageItem]:
        user_preferences = user_profile.preferences
        storage = self.__storage.copy()
        if len(user_preferences) > 0:
            storage.sort(
                key = lambda item: Recommender.__jaccard_index(item.keywords, user_preferences), reverse = True
            )

        if len(storage) < recommendations_limit:
            return storage

        return storage[:recommendations_limit]

    def load_storage(self, storage: Storage) -> None:
        self.__storage = storage.get_data()

    def __jaccard_index(a: set[str], b: set[str]) -> float:
        intersection_size = len(a.intersection(b))
        return intersection_size / (len(a) + len(b) - intersection_size)