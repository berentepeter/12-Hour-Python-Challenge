# Temperature Converter: Create a function that converts a 
# temperature from Fahrenheit to Celsius and vice versa, 
# based on a second argument indicating the direction of 
# conversion ('F_to_C' or 'C_to_F').

def convert_temperature(temp: float, direction: str) -> float:
    if direction not in ('F_to_C', 'C_to_F'):
        print('Invalid direction! Please direction properly: F_to_C or C_to_F');
        return None;
    elif direction == 'C_to_F':
        fahrenheit: float = (temp * 1.8) + 32;
        return fahrenheit;
    elif direction == 'F_to_C':
        celsius: float = (temp - 32) / 1.8;
        return celsius;
    
