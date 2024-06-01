import asyncio
import logging

import aiohttp


class CatFact:

    def __init__(self) -> None:
        self.base_url = "https://meowfacts.herokuapp.com/"

    async def get_fact(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.base_url) as response:
                    if response.status in (200, 201):
                        resp_js = await response.json()
                        #  {'stastus': 200, 'result': {'data': ['Julius Ceasar, Henri II, Charles XI, and Napoleon were all afraid of cats.']}}
                        return {"status": response.status, "result": resp_js}
                    else:
                        return {"status": response.status, "result": "Cat fact not available."}
        except aiohttp.ClientError as e:
            logging.error(f"Error fetching cat fact: {e}")
            return {"status": 500, "result": "Failed to fetch cat fact."}
        except Exception as e:
            logging.error(f"Error fetching cat fact: {e}")
            return {"status": 500, "result": "Failed to fetch cat fact."}


async def main():
    cat_fact = CatFact()
    fact = await cat_fact.get_fact()
    print(f"Fact: {fact}")


if __name__ == "__main__":
    asyncio.run(main())
