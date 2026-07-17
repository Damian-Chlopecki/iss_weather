# ISS Weather app

Project is made for check actual temperature in place where ISS satellite is.
It requires requests package and dotenv. 

## Requirements

- Python 3.12+
- look requirements.txt

## Installation 

1. python -m venv .venv
2. .\venv\Scripts\Activate.ps1
3. pip install -r requirements.txt
4. copy .env.example to .env



## Usage

python iss_weather.py

Configurable in .env
FALLBACK_LAT
FALLBACK_LON
REQUEST_TIMEOUT

## Example output :
ISS is over: (2.5012680218029, 104.30469774465)
Ground temperature: 28.0 °C