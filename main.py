# main.py
from price_manager import PriceManager


def main() -> None:
    m = PriceManager()  # create a manager (should load data)

    while True:
        # show menu options
        print("\nMenu:")
        print("1. Fetch & save from Elpris API")
        print("2. Show all records")
        print("3. Search by start hour (HH or HH:MM)")
        print("4. Add a record (manual)")
        print("5. Remove last record")
        print("6. Exit")

        c = input("Choose: ")

        match c:
            case "1":
                # ask for date + zone, fetch data from API, show how many saved
                pass
            case "2":
                # loop through all records and print nicely
                pass
            case "3":
                # ask for hour, find matching records, print them
                pass
            case "4":
                # ask user for all record details, then add and save
                pass
            case "5":
                # remove last record and confirm
                pass
            case "6":
                # exit program
                pass
            case _:
                # handle invalid choice
                pass


if __name__ == "__main__":
    main()
