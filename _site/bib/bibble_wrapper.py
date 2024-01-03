import sys
from jinja2 import Environment
from custom_filters import ieee_citation
from bibble.main import main as bibble_main

def main():
    # Set up the Jinja2 environment with custom filters
    env = Environment(...)
    env.filters['ieee_citation'] = ieee_citation

    # Call the original Bibble main function
    bibble_main(sys.argv[1:])

if __name__ == "__main__":
    main()
