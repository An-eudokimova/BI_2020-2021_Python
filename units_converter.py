# Here are collected the physical quantities that
# cause the biggest conversion difficulties for my students
print('This converter can calculate the following quantities:',
      'Cubic metre (m3) <--> Liter (l)',
      'Joule (J) <--> eV', 'Joule (J) <--> erg',
      'Celsius scale (C) <--> Kelvin scale (K)',
      'Celsius scale (C) <--> Fahrenheit scale (F)',
      'Metre per second (ms) <--> Kilometres per hour (kmh)',
      'Pascal (Pa) <--> Millimetre of mercury (mm_Hg)',
      'Parsec (pc) <--> Astronomical unit (ae)',
      'Parsec (pc) <--> Light-year (ly)',
      'Light-year (ly) <--> Astronomical unit (ae)', sep='\n')

# divided all units of measurement by quantities,
# for each quantities there are function
# value has format "Units from", "Units to", "number"


def volume(value):
    if value[0] == 'm3' and value[1] == 'l':
        return value[2] / 1000
    elif value[0] == 'l' and value[1] == 'm3':
        return value[2] * 1000
    else:
        print('Input error, please, check your input')


def energy(value):
    if value[0] == 'J' and value[1] == 'eV':
        return value[2] / (1, 6 * 10 ** (-19))
    elif value[0] == 'eV' and value[2] == 'J':
        return value[2] * (1.6 * 10 ** (-19))
    elif value[0] == 'J' and value[1] == 'cal':
        return value[2] * 0.2390
    elif value[0] == 'cal' and value[1] == 'J':
        return value[0] / 0.2390
    elif value[0] == 'J' and value[1] == 'erg':
        return value[2] * 10 ** 7
    elif value[0] == 'erg' and value[1] == 'J':
        return value[2] / 10 ** 7
    else:
        print('Input error, please, check your input')


def temp(value):
    if value[0] == 'C' and value[1] == 'K':
        return value[2] + 273
    elif value[0] == 'K' and value[1] == 'C':
        return value[2] - 273
    elif value[0] == 'C' and value[1] == 'F':
        return (value[2] + 32) * 5 / 9
    elif value[0] == 'F' and value[1] == 'C':
        return (value[2] + 32) * 9 / 5
    else:
        print('Input error, please, check your input')


def speed(value):
    if value[0] == 'kmh' and value[1] == 'ms':
        return value[2] * 1000 / 3600
    elif value[0] == 'ms' and value[1] == 'kmh':
        return value[2] * 3600 / 1000
    else:
        print('Input error, please, check your input')


def pressure(value):
    if value[0] == 'Pa' and value[1] == 'mm_Hg':
        return value[2] / 133.322
    elif value[0] == 'mm_Hg' and value[1] == 'Pa':
        return value[2] * 133.322
    else:
        print('Input error, please, check your input')


def astronomy(value):
    if value[0] == 'pc' and value[1] == 'ae':
        return value[2] * 206265
    elif value[0] == 'ae' and value[0] == 'pc':
        return value[2] / 206265
    elif value[0] == 'ly' and value[1] == 'pc':
        return value[2] / 3.26
    elif value[0] == 'pc' and value[1] == 'ly':
        return value[2] * 3.26
    elif value[0] == 'ly' and value[1] == 'ae':
        return value[2] * 63241
    elif value[0] == 'ae' and value[1] == 'ly':
        return value[2] / 63241
    else:
        print('Input error, please, check your input')


while True:
    print('To calculating press any key, to stop enter "stop"')
    answer = input()
    if answer == 'stop':
        break
    else:
        print('Input data in the format: "Unit from" "Unit to" "number"')
        inputData = input().split()
        inputData[2] = float(inputData[2])

        if inputData[0] == 'm3' or inputData[0] == 'l':
            print(inputData[2], inputData[0], '=',
                  volume(inputData), inputData[1], sep=' ')
        elif inputData[0] == 'J' or inputData[0] == 'erg' or \
                inputData[0] == 'eV':
            print(inputData[2], inputData[0], '=',
                  energy(inputData), inputData[1], sep=' ')
        elif inputData[0] == 'C' or inputData[0] == 'K' or \
                inputData[0] == 'F':
            print(inputData[2], inputData[0], '=',
                  temp(inputData), inputData[1], sep=' ')
        elif inputData[0] == 'kmh' or inputData[0] == 'ms':
            print(inputData[2], inputData[0], '=',
                  speed(inputData), inputData[1], sep=' ')
        elif inputData[0] == 'Pa' or inputData[0] == 'mm_Hg':
            print(inputData[2], inputData[0], '=',
                  pressure(inputData), inputData[1], sep=' ')
        elif inputData[0] == 'pc' or inputData[0] == 'ae' or \
                inputData[0] == 'ly':
            print(inputData[2], inputData[0], '=',
                  astronomy(inputData), inputData[1], sep=' ')
        else:
            print('Input error, check your input')
