# File to test if translation flask app works

import requests


data = {
    "english_cap": [
            "three playing cards and one ace for jacks n",
            "three playing cards with the same image and different colors",
            "two different cards with hearts and a one with a shadow",
            "a pair of playing cards that are both with hearts",
            "a pair of playing cards with hearts on them",
            "three playing cards with one playing card in the middle"
        ],
    "tags": [
        [
            "ace",
            0.598117470741272
        ],
        [
            "cards",
            0.21348552405834198
        ],
        [
            "card",
            0.15310586988925934
        ],
        [
            "jacks",
            0.017633328214287758
        ]
    ]
}

url = "http://127.0.0.1:5000/2"
response = requests.post(url, json=data)

def handle_response(response: requests.Response):
    if response.status_code == 200:
        print("Request was successful!")
        print(response.json())
    else:
        print(f"Request failed with status code {response.status_code} : {response.text}")

handle_response(response)
