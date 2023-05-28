# Content-Based-Recommender

## What?

Content based recommender system based on [Jaccard index](https://en.wikipedia.org/wiki/Jaccard_index). The project consists of a web server with a built-in recommender system and a web UI available at [127.0.0.1:5000](http://127.0.0.1:5000).

## Setup

* clone this repository
```bash
git clone https://github.com/radimvalis/Content-Based-Recommender.git
cd Content-Based-Recommender
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

## Example

The system recommends user-provided data. You only need to store your items in an object of type `list[Item]` and assign it then to `CbrConfig.items`. A simple example:

```python
from cbr import Cbr, CbrConfig, Item
    
def get_example_data() -> list[Item]:
    # 
    # creating items ...
    #
    
# Load items for recommendation
CbrConfig.items = get_example_data()

# Provide path to permanent storage
CbrConfig.users_path = "users-example.json"

# Start the server
Cbr.run()
```

Then you can open [127.0.0.1:5000](http://127.0.0.1:5000) in your browser to see the system in action. For more examples check the `examples/` directory.