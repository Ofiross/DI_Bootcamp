def current_date():
    todays_date = datetime.today().strftime('%d-%m-%Y')
    print(f'Todays date is:\n{todays_date}')


current_date()


# Exercise 2
def time_to_january():
    todays_date = datetime.today()
    dead_line_date = datetime(2022, 6, 1)
    time_between = dead_line_date - todays_date
    print(f"{'-'*40}\nThe time between todays date and the 1st of june is : \n{time_between}\n{'-'*40}")


time_to_january()


# Exercise 3
def how_long_are_you_alive():

    usr_bd = input(
        'Please indicate your birthday date in the following format DD/MM/YYYY: ')
    try:
        birthday = datetime.strptime(f'{usr_bd}', "%d/%m/%Y")
    except ValueError:
        print("Incorrect date format!")

    todays_date = datetime.now()

    hours_alive = todays_date - birthday
    difference_minutes = hours_alive.total_seconds() / 60
    print(f'{"-" * 45}\nThe total minutes this person is alive are:\n {difference_minutes}\n{"-" * 45}')


how_long_are_you_alive()

print('\n')
# Exercise 4


def current_date():
    pesach = datetime(2022, 4, 15)

    todays_date = datetime.today()
    time_to_pesach = pesach - todays_date
    print(f'{"-" * 40}\nTodays date is:\n{todays_date}\nAnd the time until Pesach is:\n{time_to_pesach}\n{"-" * 40}')


current_date()

print('\n')
# Exercise 5


def age_on_diffrent_planet():
    usr_bd = input(
        'Please indicate your birthday date in the following format DD/MM/YYYY: ')
    try:
        birthday = datetime.strptime(f'{usr_bd}', "%d/%m/%Y")
    except ValueError:
        print("Incorrect date format!")

    todays_date = datetime.now()
    time_alive = todays_date - birthday
    difference_seconds = time_alive.total_seconds()

    age_on_earth = int(difference_seconds) / 31557600
    age_on_mercury = int(difference_seconds) / 7600387.751258
    age_on_venus = int(difference_seconds) / 19413750.404352
    age_on_mars = int(difference_seconds) / 59352813.921442
    age_on_jupiter = int(difference_seconds) / 374347972.14948
    age_on_saturn = int(difference_seconds) / 929273280.9061
    age_on_uranus = int(difference_seconds) / 2651315576.4134
    age_on_neptune = int(difference_seconds) / 5200311775.2566

    print(f"{'-' * 45}\nYour age on other planets is as followed:\nEarth: {age_on_earth} Earth-years old\nMercury: {age_on_mercury} Earth-years old\nVenus: {age_on_venus} Earth-years old\nMars: {age_on_mars} Earth-years old\nJupiter: {age_on_jupiter} Earth-years old\nSaturn: {age_on_saturn} Earth-years old\nUranus: {age_on_uranus} Earth-years old\nNeptune: {age_on_neptune} Earth-years old\n{'-' * 45}")


age_on_diffrent_planet()