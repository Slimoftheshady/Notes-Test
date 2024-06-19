import sys, time

# code to make cool printy text
def output(string='', duration:float=0.6): # time in seconds
    string = str(string)
    averageTime = 0
    if len(string) != 0:
        averageTime = duration/len(string)
    for i in string:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(averageTime)
    print()

value = True
lst = []
counter = 1

def list():
    output("Current List:")
    for item in lst:
        output(str(item), duration=0.6)

    while value != False:
        output("Add or Remove?")
        operator = input(': ')
        if operator.lower() == "add":
            output('What do you want to add?')
            task = input(': ')
            task.append(f"{counter}. {task}")
            counter += 1
            output("Item Added")
            print("\x1b[H\x1b[2J", end="") #clears terminal
            list()
        elif operator.lower() == "remove":
            output("Which task do you want to remove?")
            removal = int(input(": "))
            if (removal + ".") in lst:
                lst.remove(removal + 1)
            else:
                output("Not a valid task")

        else:
            output("Command not recognised, try again")

list()