# price_manager.py
import sqlite3
from fetch_prices import get_prices
import os

DB_PATH = os.path.join("data", "prices.db")

class PriceManager:
    # Start up and load saved data
    def __init__(self) -> None:
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self) -> None:
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            SEK_per_kWh REAL,
            EUR_per_kWh REAL,
            EXR REAL,
            time_start TEXT,
            time_end TEXT
        )
        ''')

    # Return all records
    def show_all(self) -> list[dict]:
        pass

    # Find records that start at a given hour
    def search_by_start_time(self, hour: str) -> list[dict]:
        pass

    # Add one record and save
    def add_record(self, rec: dict) -> None:
        self.cursor.execute(
            "Insert into prices (SEK_per_kWh, EUR_per_kWh, EXR, time_start, time_end) VALUES (?, ?, ?, ?, ?)",
            (rec["SEK_per_kWh"], rec["EUR_per_kWh"], rec["EXR"], rec["time_start"], rec["time_end"])
        )
        self.conn.commit() 
        return None
        

    # Remove record with the help of id then save
    def remove_record(self, id: int) -> None:
        self.cursor.execute("Delete from prices where id = ?", (str(id)))
        self.conn.commit()
        return None
        

    # Turn one record into a nice text line
    def format_summary(self, r: dict) -> str:
        pass

    # Get fresh data from API, replace old data, save, return how many
    def fetch_and_replace(self, date: str, zone: str = "SE3") -> int:
        pass

