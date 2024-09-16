import logging
import os
import requests

logger = logging.getLogger(__name__)
logging.basicConfig(encoding="utf-8", level=logging.DEBUG)

TOKEN = os.environ.get("TOKEN")
BACKENDS = ["https://www.ncei.noaa.gov/cdo-web/api/v2/stations?limit=10"]


def cli():
    "Fetches all URLs in the list, logs the results, then stops"
    for url in BACKENDS:
        content = requests.get(url, headers={"token": TOKEN}).json()
        logger.info(content)


if __name__ == "__main__":
    cli()
