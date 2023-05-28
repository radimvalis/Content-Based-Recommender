
import os 
import json
from ..item import Item
from ..user import UserProfile

class StorageItemEncoder(json.JSONEncoder):

    def default(self, o: Item):
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

    def save_users(users: list[UserProfile], users_path: str) -> None:
        UserProfileSerializer.__validate_path(users_path)
        try:
            with open(users_path, "w") as stream:
                json.dump(users, stream, cls=UserProfileEncoder, ensure_ascii=False)
        except:
            print("Invalid users path!")
            exit(1)

    def load_users(users_path: str) -> list[str]:
        UserProfileSerializer.__validate_path(users_path)
        users = []
        try:
            with open(users_path, "r") as stream:
                users_as_json = json.load(stream)
                for user in users_as_json:
                    view_history = [Item(i["title"], i["url"], i["keywords"]) for i in user["view_history"]]
                    users.append(UserProfile(user["username"], view_history, user["history_limit"]))
        except:
            print("Invalid users path!")
            exit(1)

        return users

    def __validate_path(users_path: str) -> None:
        if not os.path.isfile(users_path):
            try:
                with open(users_path, "x") as stream:
                    stream.write("[]")
            except:
                print("Invalid users path!")
                exit(1)                