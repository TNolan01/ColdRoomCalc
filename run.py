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


def area_calc(num1, num2, num3):
    wall_area = (num1*num2*num3)*4
    roof_area = (num1*num2)
    area_total = wall_area + roof_area
    return area_total


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


def prod_heat_load(product_qty):
    heat_load = (product_qty * 1.9)/3600
    return heat_load


def other_heat_load(prompt):
    yes = {'yes' ,'y' , 'ye' , ''}
    no = {'no' ,'n'}
    
    while True:
        try:
            value = input(prompt)
        except ValueError:
            print_with_color("Sorry, I didn't understand that, please enter yes or no.", color=Fore.RED, brightness=Style.BRIGHT)
            continue
        if value in yes:
            while True:
                try:
                    value = int(input("How many people are working in this room?\n"))
                except ValueError:
                    print_with_color("Please enter a numerical value for people.\n", color=Fore.RED, brightness=Style.BRIGHT)
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









start_program()
wall_length = num_validator("Please enter length of coldroom in metres.:\n ")
wall_width = num_validator("Please enter width of coldroom in metres.:\n ")
wall_height = num_validator("Please enter internal height of coldroom in metres.:\n ")
room_area = area_calc(wall_length, wall_width, wall_height)
energy_rating = insulation("Please select the size of the coldroom panel from options listed :\n ")
room_temp = temperature("Please enter the target temperature on °C :\n ")
flooring = floor("Is the floor insulated ? yes or no :\n")
product_qty = num_validator("Please enter quantity of product in Kg :\n")
prod_heat_load(product_qty)
people = other_heat_load("Are there any people working in this room ? yes or no :\n")
print(people)



