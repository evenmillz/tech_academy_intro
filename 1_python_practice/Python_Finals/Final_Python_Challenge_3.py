def start():
    print('This program is intended to calculate your age in moon years!')
    Sun_Age = int(input('Enter your age in Sun years: '))
    Moon_Age = Sun_Age * 13.52
    print(f'You are {Moon_Age} Moon years old!')
    Sun_Months = Sun_Age * 12
    print(f'You are also {Sun_Months} Sun months old!')
    Sun_Minutes = Sun_Age * 525600
    print(f'That is {Sun_Minutes} Sun minutes...')
    Sun_Seconds = Sun_Age * 31,536,000
    print(f'and {Sun_Seconds} Sun seconds!')
start()
