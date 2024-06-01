# number_facts.py


import requests


def get_number_fact(number):
    url = f"http://numbersapi.com/{number}?json"
    response = requests.get(url)
    json_resp = response.json()

    if json_resp["found"]:
        return json_resp["text"]
        # Example: 3 is the cost in cents to make a $1 bill in the United States.

    return "No fact about this number."


if __name__ == "__main__":
    print(get_number_fact(3))
