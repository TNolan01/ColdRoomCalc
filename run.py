def start_program():
    user_name=input("Please enter your name: \n")
    if user_name =='':
        print("Please enter your name to continue.\n")
    else:
        print("Welcome to Coldroom Calculator {user_name}. Please input required data to calculate your refrigeration demand")

def area_calc(num1, num2, num3):
    wall_area = (num1*num2*num3)*4
    roof_area = (num1*num2)
    area_total = wall_area + roof_area
    return area_total
    

def surface_area(prompt):
    while True:
        try:
            value=float(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that, please enter a numerical value.")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            return value
            break

""" def insulation_spec():
    print("A = 80mm PIR Insulated Panel. ")
    print("B = 100mm PIR Insulated Panel.")
    print("B = 150mm PIR Insulated Panel.")
    print("C = 200mm PIR Insulated Panel.")
    while True:
        try:
            data=input("Please pick thickness of insulated panels from A to D:")
        except ValueError:
                print("Invalid option")
                continue      
        if data.lower() =a:
            u_value = 0.26
        elif data.lower() =b:
            u_value = 0.21
        elif data.lower() =c:
            u_value = 0.15
        else data.lower(): =d:
            u_value = 0.10
    
        return u_value  """
    

start_program()
wall_length = surface_area("Please enter length of coldroom in metres.:\n ")
wall_width = surface_area("Please enter width of coldroom in metres.:\n ")
wall_height = surface_area("Please enter internal height of coldroom in metres.:\n ")
wall_area = area_calc(wall_length, wall_width, wall_height)
print(wall_area)









