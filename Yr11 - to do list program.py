#input options
LIST = ["add a task", "view tasks", "exit"]
#task list
task_list = []
exicute = input("what would you like to " + LIST[0] + " or "  + LIST[1] + " or "  + LIST[2] + ": ")
exicute = exicute.lower()
i = 0
while exicute not in "exit":
    while exicute not in LIST:
        print("please enter command correctly.")
        i += 1
        #will exicute again in this loop
        if i > 0:
            exicute = input("what would you like to " + LIST[0] + " or "  + LIST[1] + " or "  + LIST[2] + ".")
            exicute = exicute.lower()
            x = 0
        else:
            #goes back into original loop
            break 
    #won't exicute in the first loop
    if i > 0:
        #if already done in while not in list will skip
        if x > 0: 
            exicute = input("what would you like to " + LIST[0] + " or "  + LIST[1] + " or "  + LIST[2] + ".")
            exicute = exicute.lower()
            while exicute not in LIST:
                print("please enter command correctly.")
                if i > 0:
                    exicute = input("what would you like to " + LIST[0] + " or "  + LIST[1] + " or "  + LIST[2] + ".")
                    exicute = exicute.lower()
    x = 1
    i += 1
    if exicute == LIST[0]:
        task = input("what task would you like to add?: ")
        task_list.append(task)
    if exicute == LIST[1]:
        print(task_list)

print("good bye")