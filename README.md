# Content-Based-Recommender

## What?

Content based recommender system based on [Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index). The application consists of a web server with a built-in recommender system and a web UI available at [127.0.0.1:5000](http://127.0.0.1:5000). The system uses data from user-defined *storages*. Currently available *storages* are: `MockUpStorage` (for testing purposes), `IRozhlasStorage` (parses articles from [irozhlas.cz](https://www.irozhlas.cz/)). You can define your own storage by implementig a class derived form the following abstract class:
```python
class Storage(ABC):
    
    @abstractmethod
    def get_data(self) -> list[StorageItem]:
        pass
```

## Setup

* clone this repository
```bash
git clone https://github.com/radimvalis/Content-Based-Recommender.git
```

* create and activate a virtual environment
```bash
python3 -m venv venv
. venv/bin/activate
```

* install the project
```bash
pip install .
```

* run the server
```bash
cbr
```

* open [127.0.0.1:5000](http://127.0.0.1:5000) in your browser