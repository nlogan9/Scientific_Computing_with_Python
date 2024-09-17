def add_time(start, duration, day=''):
    start_hours = start.split(':')[0]
    start_min = start.split(':')[1].split(' ')[0]
    start_M = start.split(':')[1].split(' ')[1]
    dur_hours = duration.split(':')[0]
    dur_min = duration.split(':')[1]
    days_later = int(dur_hours) // 24
    print(start_hours, start_min, start_M, dur_hours, dur_min, days_later)
    new_min = (int(start_min) + int(dur_min)) % 60
    if new_min < 10:
        new_min = '0' + str(new_min)
    new_hours = (int(start_hours) + int(dur_hours) + (int(start_min) + int(dur_min)) // 60) % 12
    if new_hours == 0:
        new_hours = 12
    if ((int(start_hours) + int(dur_hours) + (int(start_min) + int(dur_min)) // 60) // 12) % 2 == 1:
        if start_M == 'AM':
            new_M = 'PM'
        elif start_M == 'PM':
            new_M = 'AM'
            days_later += 1
    else:
        new_M = start_M

    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

    if days_later == 0:
        days_later_text = ''
    elif days_later == 1:
        days_later_text = '(next day)'
    else:
        days_later_text = f'({days_later} days later)'

    if day:
        day_index = days.index(day.lower())
        new_index = (day_index + days_later) % 7
        new_day = days[new_index].capitalize()
        new_time = f'{new_hours}:{new_min} {new_M}, {new_day}'
    else:
        new_time = f'{new_hours}:{new_min} {new_M}'
    if days_later_text:
        new_time += f' {days_later_text}'


    print(new_time)

    return new_time

add_time('11:55 AM', '0:5')