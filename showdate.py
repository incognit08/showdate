import datetime

def main():
    # Get the current date
    today = datetime.date.today()

    # Format the date as Month Day, Year
    formatted_date = today.strftime("%B %d, %Y")

    # Print the formatted date
    print(f"Today's date is: {formatted_date}")

if __name__ == "__main__":
    main()
