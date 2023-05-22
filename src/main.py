#!/usr/bin/env python3

from webapp import create_app
from config import DEBUG

def main():
    app = create_app()
    app.run(debug=DEBUG)

if __name__ == "__main__":
    main()