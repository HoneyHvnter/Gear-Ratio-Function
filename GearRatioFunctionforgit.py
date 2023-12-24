# this is the function definition it has two parameters, an expression doing calculations and a return
def f_calc_gear_ratio(p_drive_gear,p_driven_gear):
    gear_ratio = p_driven_gear/p_drive_gear # this is just a simple expression we learned in Chapter 2.
    return gear_ratio #returning a value is the most common purpose for a function

# lets give the user input variables a default value before we enter a loop
user_drive_gear = 0
user_driven_gear = 0

# maybe we'd like a counter
counter = 0

# getting input from the user is always better with a while loop because we don't know how many passes we will make
while user_drive_gear >=0:
    #increment the counter variable here at the top of the loop
    counter += 1
    user_drive_gear = int(input('Please enter the drive gear tooth count (-1 to exit):\n'))
    if user_drive_gear < 0: #if the user wants to exit we break out of the loop without getting the 2nd value
        break
    #get the driven gear from the user here
    user_driven_gear = int(input("Please enter the driven gear tooth count:"))
    print(f'Drive Gear has {user_drive_gear} teeth Driven gear has {user_driven_gear} teeth for an effective gear ratio of {f_calc_gear_ratio(user_drive_gear, user_driven_gear):.2f}')
print(f'Thank you for using the gear ratio calculator, you have completed {counter} calculations')