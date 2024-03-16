import json

import requests


if __name__ == "__main__":

    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    data = response.json()
    print(data)

    with open("dogs.json", "w") as f:
        json.dump(data, f)

    api_url = "https://api.jsonbin.io/v3/b"
    headers = {
        "Content-Type": "application/json",
        "X-Master-Key": "$2a$10$96OFsZKNFa2aH7/9G.DNUOcz6ei3uvVcbJwnoyEYvnCcoZoGPvkiy",
        "X-Collection-Id": "65ab4419dc7465401896f12a",
    }

    with open("dogs.json", "r") as f:
        data = json.load(f)

    response = requests.post(api_url, json=data, headers=headers)
    print(response.json())