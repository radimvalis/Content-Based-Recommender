
from .config import CbrConfig
from .webapp import create_app

class Cbr:

    def run() -> None:
        """
        Starts content based recommender
        """
        create_app().run(debug=CbrConfig.debug)