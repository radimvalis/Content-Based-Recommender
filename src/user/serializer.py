
from storage import StorageItem
from user import UserProfile
import json
import os 

class StorageItemEncoder(json.JSONEncoder):

    def default(self, o: StorageItem):
        as_dict = {
            "title": o.title,
            "url": o.url,
            "keywords": list(o.keywords)
        }
        return as_dict

class UserProfileEncoder(json.JSONEncoder):

    def default(self, o: UserProfile):
        as_dict = {
            "username": o.username,
            "view_history": [StorageItemEncoder().default(si) for si in o.view_history],
            "history_limit": o.history_limit
        }
        return as_dict

class UserProfileSerializer:

    def save_users(users: list[UserProfile]) -> None:
        users_path = UserProfileSerializer.__users_path()
        with open(users_path, "w") as stream:
            json.dump(users, stream, cls=UserProfileEncoder, ensure_ascii=False)

    def load_users() -> list[str]:
        users_path = UserProfileSerializer.__users_path()
        users = []
        with open(users_path, "r") as stream:
            users_as_json = json.load(stream)
            for user in users_as_json:
                view_history = [StorageItem(i["title"], i["url"], i["keywords"]) for i in user["view_history"]]
                users.append(UserProfile(user["username"], view_history, user["history_limit"]))
        
        return users
    
    def __users_path() -> str:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        users_path = dir_path + "/users.json"
        if not os.path.isfile(users_path):
            with open(users_path, "x") as stream:
                stream.write("[]")
        
        return users_path
    