from price_manager import PriceManager

if __name__ == "__main__":
   p = PriceManager()
   p.add_record({
    "time_start": "2025-10-01T12:00:00",
    "time_end": "2025-10-01T13:00:00",  
    "SEK_per_kWh": 0.43,
    "EUR_per_kWh": 0.53,
    "EXR": 0.99
   })

   p.remove_record(2)

