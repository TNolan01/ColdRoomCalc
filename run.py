def start_program():
    project_ref = input("Please enter your project name or reference: \n")
    if project_ref == '':
        print("Please enter your name to continue.\n") 
    else:
        print(f"Welcome to Coldroom Calculator. Please input required data to calculate your refrigeration demand for {project_ref}")


def area_calc(num1, num2, num3):
    wall_area = (num1*num2*num3)*4
    roof_area = (num1*num2)
    area_total = wall_area + roof_area
    return area_total


def surface_area(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that, please enter a numerical value.")
            continue
        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            return value
        
        
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
            print("Please select an option between 1 and 4.")
            continue
        if panel not in range(1, 4):
            print("Please enter an option between 1 and 4:")
            continue
        elif panel == 1:
            energy_rating = u_value[0]["U_value"]
        elif panel == 2:
            energy_rating = u_value[1]["U_value"]
        elif panel == 3:
            energy_rating = u_value[2]["U_value"]
        else: 
            energy_rating == u_value[3]["U_value"]
        return energy_rating
        break 


start_program()
wall_length = surface_area("Please enter length of coldroom in metres.:\n ")
wall_width = surface_area("Please enter width of coldroom in metres.:\n ")
wall_height = surface_area("Please enter internal height of coldroom in metres.:\n ")
room_area = area_calc(wall_length, wall_width, wall_height)
print(room_area)
energy_rating = insulation("Please select the size of the coldroom panel from options listed : ")
print(energy_rating)

