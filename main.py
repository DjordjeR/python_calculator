import re  # regex for parsing command line input


print("My Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True


def do_math():
    global run
    global previous
    equation = ""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))
    if equation == 'quit' or equation == 'EOF':
        print("Good bye!")
        run = False
    else:
        equation = re.sub('[a-zA-z,.:()" "]', '', equation)
        if previous == 0:
            try:
                previous = eval(equation)
            except SyntaxError:
                pass
        else:
            previous = eval(str(previous) + equation)


while run:  # loop breaks when we enter "quit"
    do_math()
