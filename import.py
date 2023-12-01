import requests
import shutil
import os

from datetime import date
from typing import Any
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("TOKEN")
TEMPLATE = os.getenv("TEMPLATE")

PYFILENAME = "spaghet.py"
INPUTFILENAME = "input.txt"

TODAY = date.today()
CURRENTDAY = TODAY.day
CURRENTYEAR = TODAY.year


def make_path(day: int) -> str:
    """Creates path to where the file should be saved or where to check if the file exist."""
    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)

    # Construct the day directory
    day_path = os.path.join(script_dir, str(day))
    
    # Create the day directory if missing
    if not os.path.exists(day_path):
        os.mkdir(day_path)
        shutil.copy(TEMPLATE, day_path + "\\" + PYFILENAME)

    # Construct the full file path
    file_path = os.path.join(day_path, INPUTFILENAME)

    return file_path


def _get_data(day: int) -> str:
    """Get data from from the api and save it to a txt file."""

    url = f"https://adventofcode.com/{CURRENTYEAR}/day/{day}/input"
    response = requests.get(url=url, cookies={"session": TOKEN})
    response_data = response.text

    with open(make_path(day), "w") as input:
        input.write(response_data)

    return response_data


def get_data(day: int = CURRENTDAY) -> str:
    """
    Gets the data from aoc api if there is no file saved containing the data,
    if no file exist get data from api and create the file.
    """

    file_path = make_path(day)

    # Check if the file exist
    if os.path.exists(file_path):
        print(f"File exist! No new data downloaded for day: {day}")
        with open(file_path, "r") as file:
            return file.read()
    else:
        return _get_data(day=day)


get_data()