from storage import MockUpStorage, IRozhlasStorage

# Source of items for recommendation
STORAGE = MockUpStorage

# Number of viewed items to store in the user's profile
USER_HISTORY_LIMIT = 5

# Number of recommended items
RECOMMENDATIONS_LIMIT = 100

# Number of recommended items shown at once
RESULTS_PER_PAGE_LIMIT = 10

# Flask debug mode
DEBUG = False