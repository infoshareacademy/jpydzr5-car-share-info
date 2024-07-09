import datetime
from datetime import timedelta

def get_rental_period() -> tuple | bool:
    # start date
    try:
        date: str = input("[4/20] Podaj datę rozpoczęcia wynajmu (YYYY-MM-DD): ")

        start_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        if start_date < datetime.date.today():
            raise ValueError
        # else:
        #     return start_date

    except ValueError:
        print("Nieprawidłowy format daty lub data przeszła. Spróbuj ponownie.")
        return False

    # start time
    try:
        time: str = input(
            "[5/20] Podaj godzinę odbioru (format HH:MM, między 06:00 a 23:00): "
        )

        start_time = datetime.datetime.strptime(time, "%H:%M").time()
        if not datetime.time(6, 0) <= start_time <= datetime.time(23, 0):
            raise ValueError
        # else:
        #     return start_time

    except ValueError:
        print(
            "Nieprawidłowy format godziny lub godzina poza zakresem. Spróbuj ponownie."
        )
        return False

    # end date
    try:
        date: str = input("[6/20] Podaj datę zakończenia wynajmu (YYYY-MM-DD): ")

        end_date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        if end_date < datetime.date.today():
            raise ValueError
        # else:
        #     return end_date

    except ValueError:
        print("Nieprawidłowy format daty lub data przeszła. Spróbuj ponownie.")
        return False

    # end time
    try:
        time: str = input(
            "[7/20] Podaj godzinę zwrotu (format HH:MM, między 06:00 a 23:00): "
        )

        end_time = datetime.datetime.strptime(time, "%H:%M").time()
        if not datetime.time(6, 0) <= end_time <= datetime.time(23, 0):
            raise ValueError
        # else:
        #     return end_time

    except ValueError:
        print(
            "Nieprawidłowy format godziny lub godzina poza zakresem. Spróbuj ponownie."
        )
        return False

    # set minimal rental period
    min_rent_date = timedelta(days=1)

    diff_rent_date = end_date - start_date

    # check if minimal rental period and correct dates are preserved
    if start_date >= end_date:
        print("Data zwrotu nie może być taka sama lub wcześniejsza od daty wynajmu.")
        return False
    elif diff_rent_date <= min_rent_date:
        print("Czas wynajmu nie może być krótszy niż 1 dzień.")
        return False
    else:
        pass

    # convert data type to str
    start_date = start_date.strftime("%Y-%m-%d")
    start_time = start_time.strftime("%H:%M")
    end_date = end_date.strftime("%Y-%m-%d")
    end_time = end_time.strftime("%H:%M")

    # return arguments
    return start_date, start_time, end_date, end_time

def main():
    print(get_rental_period())


if __name__ == "__main__":
    main()
