import requests
import json
import sys

url = "https://en.wikipedia.org/w/api.php"

if len(sys.argv) > 1:
    variable = sys.argv[1]
    print(f"Received page: {variable}, attempting to parse...")
    params = {
        "action": "parse",
        "page": variable,
        "format": "json",
        "prop": "wikitext"
    }
    response = requests.get(url, params=params)
    data = response.json()
    print(data)
else:
    print("No page was passed!")


