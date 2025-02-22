def fahr_to_celsius(temp_fahrenheit):
    '''
    Convert temperatures from Fahrenheit to Celsius.
    '''
    return (temp_fahrenheit - 32) / 1.8


def temp_classifier(temp_celsius):
    '''
    Classify given temperatures based on the criteria below:
    | 0            | Temperatures below -2 degrees Celsius                                    |
    | 1            | Temperatures equal or warmer than -2, but less than +2 degrees Celsius   |
    | 2            | Temperatures equal or warmer than +2, but less than +15 degrees Celsius  |
    | 3            | Temperatures equal or warmer than +15 degrees Celsius                    | 
    '''
    if temp_celsius < -2:
        return 0
    elif -2 <= temp_celsius < 2:
        return 1
    elif 2 <= temp_celsius < 15:
        return 2
    elif 15 <= temp_celsius:
        return 3