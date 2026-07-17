# ISS Weather app

this project check the current ground temperature at the location the ISS flying over.
It requires requests package and dotenv. 

## Requirements

- Python 3.12+
- see requirements.txt

## Installation 

1. python -m venv .venv
2. .\.venv\Scripts\Activate.ps1
3. pip install -r requirements.txt
4. copy .env.example to .env



## Usage
```powershell
python iss_weather.py
```
Configurable in .env
FALLBACK_LAT
FALLBACK_LON
REQUEST_TIMEOUT

## Example output:
```powershell
ISS is over: (2.5012680218029, 104.30469774465)
Ground temperature: 28.0 °C
```