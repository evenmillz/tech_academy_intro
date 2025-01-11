def start():
    print('Look at this number:')
# Full operative task list satisfied with the code below    
    Operative_List = 8 + 8 * 8 / 8 % 2
    print(Operative_List)
    print('This is the result of 8 + 8 * 8 / 8 % 2!')
    
# Assign an integer to a variable
    Integer = 11
    
# Assign a string to a variable
    a = 'Hi. I\'m a string that has been assigned to a variable!'
    
# Assign a float to a variable
    z = 3.14
    
# Use the print() function to print out the variable you assigned
    print(a)
    print(z + 11)
    print('...and that is 11 + 3.14')
    
# Use each of these logical operators: and, or, not
    print([Operative_List and Integer] or [a and not z])
    print('Operative_List and Integer or a and not z put 11 in jail up there!')
    print('We got any bail?')

# Use each conditional statement: if, elif, else
    if Operative_List > Integer:
        print('20 dollas!')
    elif Integer == Operative_List:
        print('40 dollas!')
    else:
        print('if has $20, and elif has $40, but it\'s not enough...')
        print('...else you have anything.')
        
# Use a while and if loop
    while Operative_List != Operative_List:
        print('while loop')
        if Operative_List == Operative_List:
            break

# Create a list iterate through that list using a for loop
# to print each item out on a new line
    i = ["l", "i", "s", "t"]
    for x in i:
        if x > "a":
            print(x)

# Create a tuple and iterate through it
# using a for loop to print each item out on a new line
    Tuple_Time =  ("I\'m an element", "i'\'m an element", "I am also an element")
    for item in Tuple_Time:
        print(item)

# Define a function that returns a string variable
# Call the function you defined above and print the result to the shell
    f_string = 'Instructor!'
    def Task_Twelve():
        return 'Peace and blessings, '
    print(Task_Twelve() + f_string)

start()
