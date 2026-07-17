import logging
import os
import time

import requests
from dotenv import load_dotenv

load_dotenv()
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "10"))
FALLBACK_LAT = float(os.getenv("FALLBACK_LAT", "0.0"))
FALLBACK_LON = float(os.getenv("FALLBACK_LON", "0.0"))

logger = logging.getLogger(__name__)


logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

class ApiError(Exception):
    pass

def get_iss_position() -> tuple[float, float]:
    try:
        response = requests.get("https://api.wheretheiss.at/v1/satellites/25544", timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        logger.info("Connection to ISS API success")
        return (data["latitude"], data["longitude"])
    except ApiError as error:
        raise ApiError(f"ISS API failed {error}" )


def get_temperature(latitude: float, longitude: float) -> float:
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m"
    }
    try:
        response = requests.get("https://api.open-meteo.com/v1/forecast", params=params, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        data = response.json()
        logger.info("Connection to meteo API success")
        return data["current"]["temperature_2m"]
    except requests.exceptions.RequestException as error:
        raise ApiError(f"Meteo API request failed: {error}") from error # achowuje oryginalny traceback (zobaczysz "The above exception was the direct cause of...")

def main() -> None:
    for attempt in range(1, 4):
        try:
            latitude, longitude = get_iss_position()
            temperature = get_temperature(latitude, longitude)
            print(f"ISS is over: ({latitude}, {longitude})")
            print(f"Ground temperature: {temperature} °C")
            logger.info(f"Data downloaded correct: ISS coordinates {latitude, longitude}, temperature {temperature}")
            break
        except ApiError as error:
            logging.warning(f"Attempt {attempt} failed {error}.")
            if attempt < 3:
                time.sleep(1)
    else:
        print("ERROR: All attempts failed. Using fallback coordinates")
        logger.error("All attempts failed. Using fallback coordinates")
        return FALLBACK_LAT, FALLBACK_LON

if __name__ == "__main__":
    main()
