# price_manager.py
import json
from fetch_prices import get_prices

DATA_FILE = "data/prices.json"   # assume data/ already exists

class PriceManager:
    # Start up and load saved data
    def __init__(self) -> None:
        pass

    # Read data from file into memory
    def load_data(self) -> None:
        pass

    # Write current data back to file
    def save_data(self) -> None:
        pass

    # Return all records
    def show_all(self) -> list[dict]:
        pass

    # Find records that start at a given hour
    def search_by_start_time(self, hour: str) -> list[dict]:
        pass

    # Add one record and save
    def add_record(self, rec: dict) -> None:
        pass

    # Remove the last record and save
    def remove_last_record(self) -> None:
        pass

    # Turn one record into a nice text line
    def format_summary(self, r: dict) -> str:
        pass

    # Get fresh data from API, replace old data, save, return how many
    def fetch_and_replace(self, date: str, zone: str = "SE3") -> int:
        pass
