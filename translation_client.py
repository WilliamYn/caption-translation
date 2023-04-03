import requests

data = {
    "tags": [
        [
            "traffic",
            0.7948160767555237
        ],
        [
            "freeway",
            0.08834600448608398
        ],
        [
            "cars",
            0.02651975117623806
        ],
        [
            "direction",
            0.025509683415293694
        ],
        [
            "lanes",
            0.015784043818712234
        ],
        [
            "road",
            0.010963880456984043
        ],
        [
            "exit",
            0.006227716337889433
        ],
        [
            "europe",
            0.005784913897514343
        ],
        [
            "full",
            0.005649014841765165
        ],
        [
            "busy",
            0.004490676335990429
        ],
        [
            "city",
            0.004447447136044502
        ],
        [
            "towards",
            0.002754420507699251
        ],
        [
            "traveling",
            0.0017260592430830002
        ],
        [
            "going",
            0.0016977312043309212
        ],
        [
            "heavy",
            0.0013506737304851413
        ],
        [
            "street",
            0.001317215384915471
        ],
        [
            "signs",
            0.0010754705872386694
        ],
        [
            "one",
            0.0005146128823980689
        ],
        [
            "many",
            0.00032997032394632697
        ],
        [
            "showing",
            0.00017075767391361296
        ],
        [
            "multiple",
            0.00015955971321091056
        ],
        [
            "view",
            0.00013871821283828467
        ],
        [
            "bunch",
            0.00011566036846488714
        ],
        [
            "open",
            0.00010997253411915153
        ]
    ],
    "captions": [
        "a bunch of cars that are in the street"
    ],
    "english_cap": [
        "many cars traveling on a city street with multiple lanes",
        "a view down a busy street showing the exit to an open road",
        "a street full of cars and street signs",
        "a freeway full of traffic going towards one direction",
        "heavy traffic on a freeway in europe",
        "a bunch of cars that are in the street"
    ]
}

url = "http://127.0.0.1:5000"
response = requests.get(url, json=data)

def handle_response(response: requests.Response):
    if response.status_code == 200:
        print("Request was successful!")
        print(response.json())
    else:
        print(f"Request failed with status code {response.status_code} : {response.text}")

handle_response(response)