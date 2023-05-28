
from .config import CbrConfig
from .webapp import create_app

class Cbr:

    def run() -> None:
        """
        Starts content based recommender
        """

        if CbrConfig.items == []:
            print("No items provided!")
            return
        
        if CbrConfig.users_path == "":
            print("No users path provided!")
            return

        create_app().run(debug=CbrConfig.debug)