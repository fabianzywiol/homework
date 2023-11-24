time_24_hour = input("Podaj czas (format 24-godzinny, hh:mm): ")

if ":" in time_24_hour:
    split_time = time_24_hour.split(':')
    hours = int(split_time[0])
    minutes = int(split_time[1])

    if 0 <= hours < 24 and 0 <= minutes < 60:
        if hours % 12 != 0:
            hours_12_hour_format = hours % 12
        else:
            hours_12_hour_format = 12

        if hours < 12:
            period = "am"
        else:
            period = "pm"

        print(f"Czas w formacie 12-godzinnym: {hours_12_hour_format}:{minutes:02d}{period}")
    else:
        print("Błędne godziny lub minuty. Podaj poprawne wartości.")
else:
    print("Błędny format czasu. Podaj czas w formacie hh:mm.")
