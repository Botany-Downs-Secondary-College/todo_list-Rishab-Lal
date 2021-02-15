def command_operator(order):
    if order == options_list[0] or order == options_list[3]:
        task = input("what task would you like to add to your list?: ")
        task_list.append(task)
    elif order == options_list[1] or order == options_list[4]:
        print("your tasks:")
        tasks_in_list = len(task_list)
        x = range(0, tasks_in_list, 1)
        b = 0
        for n in x:
            b += 1
            print("{}.".format(b), task_list[n])
        
    


user_name = input("greetings user, what is your name?: ")
print("hello user {}. It's nice to meet you.".format(user_name))

global task_list
global options_list
options_list = ["addtask", "viewtasks", "exitprogram","1","2","3"]
task_list = []

print("what would you like to do out of the following options {}?".format(user_name))
print("1. add a task to your to do list \n2. view current tasks in list \n3. exit the program")
order = input("to select one of the following, please enter the number of your objective or the following comands: ['add task', 'view tasks', 'exit program']: ")
loop = 0
order = str(order).strip().lower().replace(" ","")
while order not in options_list[2] or order not in options_list[5]:
    if order in options_list[2] or order in options_list[5]:
        break
    if loop > 0:
        order = input("please enter the number of your objective or the following comands: ['add task', 'view tasks', 'exit program']: ")
        order = str(order).strip().lower().replace(" ","")
    loop += 1
    while order not in options_list:
        print("command {} unrecognised".format(order))
        order = input("to select one of the following, please enter the number of your objective or the following comands: ['add task', 'view tasks', 'exit program']: ")
        order = str(order).strip().lower().replace(" ","")
    if order in options_list[2] or order in options_list[5]:
        break
    command_operator(order)

    





print("bye bye.")


        
    