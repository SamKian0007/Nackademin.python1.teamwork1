from price_manager import PriceManager
import json

def load_from_json(p: PriceManager, file_path: str) -> int:
   try:
         with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
   except FileNotFoundError:
         print(f"File {file_path} not found.")
         return 0

   count = 0
   for rec in data:
         p.add_record(rec)
         count += 1

   print(f"Added {count} rows from {file_path}")
   return count

def remove_record(p: PriceManager):
   while True:
      try:
            id_string = input("Delete records, if you press 0 the program stops")
            id_number = int(id_string)
            if id_number == 0:
               break
       
            p.remove_record(id_number)
      except ValueError:
            print("Give me a real number")
      except Exception as e:
            print(f"Something went wrong: {e}")
         

if __name__ == "__main__":
   p = PriceManager()
   load_from_json(p, "data/prices_2025-08-01_SE2.json")
   remove_record(p)

""" 
  p.add_record({
    "time_start": "2025-10-01T12:00:00",
    "time_end": "2025-10-01T13:00:00",  
    "SEK_per_kWh": 0.43,
    "EUR_per_kWh": 0.53,
    "EXR": 0.99
   })

   p.remove_record(2)
"""

