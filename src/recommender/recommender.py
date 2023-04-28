
from user import UserProfile
from storage import Storage, StorageItem

class Recommender:

    def __init__(self) -> None:
        self.__storage: list[StorageItem] = []

    def recommend_to(self, user_profile: UserProfile, max_recommendations_count: int = 100) -> list[StorageItem]:
        user_preferences = user_profile.preferences()
        self.__storage.sort(
            key = lambda item: Recommender.__jaccard_index(item.keywords(), user_preferences), reverse = True
        )

        if len(self.__storage) < max_recommendations_count:
            return self.__storage.copy()

        return self.__storage[:max_recommendations_count]

    def load_storage(self, storage: Storage) -> None:
        self.__storage = storage.get_data()

    def __jaccard_index(a: set[str], b: set[str]) -> float:
        intersection_size = len(a.intersection(b))
        return intersection_size / (len(a) + len(b) - intersection_size)