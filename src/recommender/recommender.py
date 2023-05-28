
from ..user import UserProfile
from ..item import Item

class Recommender:

    def recommend_to(user_profile: UserProfile, items: list[Item], recommendations_limit: int = 100) -> list[Item]:
        user_preferences = user_profile.preferences
        items_copy = items.copy()
        if len(user_preferences) > 0:
            items_copy.sort(
                key = lambda item: Recommender.__jaccard_index(item.keywords, user_preferences), reverse = True
            )

        if len(items_copy) < recommendations_limit:
            return items_copy

        return items_copy[:recommendations_limit]

    def __jaccard_index(a: set[str], b: set[str]) -> float:
        intersection_size = len(a.intersection(b))
        return intersection_size / (len(a) + len(b) - intersection_size)