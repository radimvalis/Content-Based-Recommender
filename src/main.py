#!/usr/bin/env python3

from webapp import create_app

def main():
    app = create_app()
    app.run(debug=True)

if __name__ == "__main__":
    main()