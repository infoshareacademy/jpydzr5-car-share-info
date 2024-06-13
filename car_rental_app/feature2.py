import datetime


def get_rental_period() -> datetime.date | bool:

    # start date
    try:
        start_date: str = input("Podaj datę rozpoczęcia wynajmu (YYYY-MM-DD): ")

        date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
        if date < datetime.date.today():
            raise ValueError
        else:
            return date

    except ValueError:
        print("Nieprawidłowy format daty lub data przeszła. Spróbuj ponownie.")
        return False
    
    # start time
    ...

    # end date
    ...

    # end time
    ...


def main():
    print(get_rental_period())


if __name__ == "__main__":
    main()
