# (c) 2021 Yannic Breiting

# S. 108

sec = int(input('Bitte die Sekunden angeben!'))
min, seconds = divmod(sec, 60)
hours, minutes = divmod(min, 60)
print(f'{hours}:{minutes}:{seconds}')
