from colorama import init, Fore, Back, Style



init()
# all available foreground colors
FORES = [ Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE ]
# all available background colors
BACKS = [ Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE ]
# brightness values
BRIGHTNESS = [ Style.DIM, Style.NORMAL, Style.BRIGHT ]


def print_with_color(s, color=Fore.WHITE, brightness=Style.NORMAL, **kwargs):
    """Utility function wrapping the regular `print()` function 
    but with colors and brightness"""
    print(f"{brightness}{color}{s}{Style.RESET_ALL}", **kwargs)


def start_program():
    print_with_color("Coldroom Duty Calculator", color=Fore.BLUE, brightness=Style.BRIGHT)
    project_ref = input("Please enter your project name or reference: \n")
    if project_ref == '':
        print_with_color("Please enter a reference name or number to continue.\n", color=Fore.RED, brightness=Style.BRIGHT) 
    else:
        print_with_color(f"Welcome to Coldroom Calculator for your project - {project_ref}.\n", color=Fore.BLUE, brightness=Style.BRIGHT ) 
        print_with_color("Please input the required data to calculate your refrigeration power demand", color=Fore.BLUE, brightness=Style.BRIGHT) 


def num_validator(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print_with_color("Sorry, I didn't understand that, please enter a numerical value.", color=Fore.RED, brightness=Style.BRIGHT)
            continue
        if value < 0:
            print_with_color("Sorry, your response must not be negative.", color=Fore.RED, brightness=Style.BRIGHT )
            continue
        else:
            return value


def temperature(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print_with_color("Sorry, I didn't understand that, please enter a numerical value.", color=Fore.RED, brightness=Style.BRIGHT)
            continue
        if value <= 0:
            temp = 20 + abs(value)
            return temp
        else:
            temp = 20-value
            return temp

        
def insulation(prompt):
    u_value = [{'Name': '80mm PIR Panel', 'U_value': 0.26},
               {'Name': '100mm PIR Panel', 'U_value': 0.21},
               {'Name': '150mm PIR Panel', 'U_value': 0.15},
               {'Name': '200mm PIR Panel', 'U_value': 0.10}]
  
    print(f'1. {u_value[0]["Name"]}')
    print(f'2. {u_value[1]["Name"]}')
    print(f'3. {u_value[2]["Name"]}')
    print(f'4. {u_value[3]["Name"]}')
  
    while True:
        try:
            panel = int(input(prompt))
        except ValueError:
            print_with_color("Please select an option between 1 and 4.", color=Fore.BLUE, brightness=Style.BRIGHT)
            continue
        if panel not in range(1, 5):
            print_with_color("Please enter an option between 1 and 4:", color=Fore.RED, brightness=Style.BRIGHT)
            continue
        elif panel == 1:
            energy_rating = u_value[0]["U_value"]
        elif panel == 2:
            energy_rating = u_value[1]["U_value"]
        elif panel == 3:
            energy_rating = u_value[2]["U_value"]
        else:
            panel == 4
            energy_rating = u_value[3]["U_value"]
        return energy_rating
        break 


def floor(prompt):
    yes = {'yes' ,'y' , 'ye' , ''}
    no = {'no' ,'n'}
    
    while True:
        try:
            value = input(prompt)
        except ValueError:
            print_with_color("Sorry, I didn't understand that, please enter yes or no.", color=Fore.RED, brightness=Style.BRIGHT)
            continue
        if value in yes:
            value = 0.28
            return value
        elif value in no:
            value = 1.0
            return value
        else:
            print_with_color("Please respond with 'yes' or 'no'", color=Fore.RED, brightness=Style.BRIGHT)


def other_heat_load(prompt):
    yes = {'yes','y', 'ye', ''}
    no = {'no','n'}
    
    while True:
        try:
            value = input(prompt)
        except ValueError:
            print_with_color("Sorry, I didn't understand that, please enter yes or no.", color=Fore.RED, brightness=Style.BRIGHT)
            continue
        if value in yes:
            while True:
                try:
                    value = int(input("How many people are working in this room?\n "))
                except ValueError:
                    print_with_color("Please enter a numerical value for people.\n ", color=Fore.RED, brightness=Style.BRIGHT)
                    continue
                if value < 0:
                    print_with_color("Your input must be a whole number.", color=Fore.RED, brightness=Style.BRIGHT)
                    continue
                else:
                    heat_calc = (value * 6 * 270)/1000
                    return heat_calc
                    break
        elif value in no:
            heat = 1.0
            return heat
            break
        else:
            print_with_color("Please respond with 'yes' or 'no'", color=Fore.RED, brightness=Style.BRIGHT)


def transmission_load_kw(num1, num2, num3, num4, num5):
    wall_area = (num1*num2*num3)*4
    roof_area = (num1*num2)
    area_total = wall_area + roof_area
    load_1 = (num4 * area_total * num5 * 24) / 1000
    return load_1


def floor_load_kw(num1, num2, num3, num4):
    floor_area = num1 * num2
    load_2 = (num3 * floor_area * num4 * 24) / 1000
    return load_2


def product_load_kw(num1, num2, num3):
    temp = 20-num3
    load_3 = ((num1 * 1.9)/3600) + (num1 * (num2-temp)/3600)
    return load_3


def people_load_kw(num1):
    load_4 = (num1 * 6 * 270)/1000
    return load_4


def infiltration_kw(num1, num2, num3, num4, num5):
    volume = num2 * num3 * num4
    load_5 = (num1 * volume * 2 * (20 - num5))/3600
    return load_5


def duty_calc(num1, num2, num3, num4, num5):
    total_duty = ((num1 + num2 + num3 + num4 + num5) * 1.2) / 14
    return round(total_duty, 2)


start_program()
wall_length = num_validator("Please enter length of coldroom in metres.:\n ")
wall_width = num_validator("Please enter width of coldroom in metres.:\n ")
wall_height = num_validator("Please enter internal height of coldroom in metres.:\n ")
energy_rating = insulation("Please select the size of the coldroom panel from options listed :\n ")
room_temp = temperature("Please enter the target temperature, in °C. :\n ")
flooring = floor("Is the floor insulated ? yes or no :\n ")
product_qty = num_validator("Please enter quantity of product in Kg. :\n ")
product_in_temp = num_validator("Please enter the temperature of product going into room, in °C :\n ")
people = other_heat_load("Are there any people working in this room ? yes or no :\n ")
air_changes = num_validator("Please enter an approximate number of door openings in 24hour period.:\n ")
load_1 = transmission_load_kw(wall_length, wall_width, wall_height, energy_rating, room_temp)
load_2 = floor_load_kw(wall_length, wall_width, flooring, room_temp)
load_3 = product_load_kw(product_qty, product_in_temp, room_temp)
load_4 = people_load_kw(people)
load_5 = infiltration_kw(air_changes, wall_height, wall_length, wall_width, room_temp)
total_duty = duty_calc(load_1, load_2, load_3, load_4, load_5)
print(total_duty)



