
from .item import Item

class CbrConfig:
    
    items: list[Item] = []
    """
    Items for recommendation
    """

    users_path: str = ""
    """
    Path to permanent storage of user profiles
    """

    user_history_limit: int = 5
    """
    Number of viewed items to store in the user's profile
    """

    recommendations_limit: int = 100
    """
    Number of recommended items
    """

    results_per_page_limit: int = 10
    """
    Number of recommended items shown at once
    """

    debug: bool = False
    """
    Flask debug mode
    """