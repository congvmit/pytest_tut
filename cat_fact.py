import json
import logging

import requests

base_url = "https://meowfacts.herokuapp.com/"


def get_cat_fact() -> tuple[int, dict] | str:
    try:
        response = requests.get(base_url)
        if response.status_code in (200, 201):
            return response.status_code, response.json()
        else:
            return json.dumps({"ERROR": "Cat Fact Not Available"})
    except requests.exceptions.HTTPError as errh:
        logging.error(errh)
    except requests.exceptions.ConnectionError as errc:
        logging.error(errc)
    except requests.exceptions.Timeout as errt:
        logging.error(errt)
    except requests.exceptions.RequestException as err:
        logging.error(err)
