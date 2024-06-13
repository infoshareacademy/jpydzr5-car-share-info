import datetime


def get_rental_period() -> tuple | bool:
    # start date
    try:
        date: str = input("Podaj datę rozpoczęcia wynajmu (YYYY-MM-DD): ")

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
            "Podaj godzinę odbioru (format HH:MM, między 06:00 a 23:00): "
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
        date: str = input("Podaj datę zakończenia wynajmu (YYYY-MM-DD): ")

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
        time: str = input("Podaj godzinę zwrotu (format HH:MM, między 06:00 a 23:00): ")

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

    # return arguments
    return start_date, start_time, end_date, end_time


def main():
    print(get_rental_period())

    # BUG: there's no minimal rental period
    # BUG: end_date can be past start_date


if __name__ == "__main__":
    main()
