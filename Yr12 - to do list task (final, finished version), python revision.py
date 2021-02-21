def command_operator(order):
    if order == options_list[0] or order == options_list[3]:
        task = input("what task would you like to add to your list?: ")
        if task == "exit_task_list":
            return "exit_the_task_list"
        task_list.append(task)
        if task != "exit_task_list":
            return "running"
    elif order == options_list[1] or order == options_list[4]:
        print("your tasks:")
        tasks_in_list = len(task_list)
        x = range(0, tasks_in_list, 1)
        b = 0
        for n in x:
            b += 1
            print("{}.".format(b), task_list[n])
        Y_or_N = input("would you like to change or remove or add completion confirmation to a task from the list? Enter ['Y'] or ['N']: ").strip().upper()
        while Y_or_N != "Y" or Y_or_N != "N":
            if  Y_or_N == "Y" or Y_or_N == "N":
                break
            print("please answer ['Y'] or ['N']")
            Y_or_N = input("would you like to change or remove or add completion confirmation to a task from the list?: ").strip().upper()
            if  Y_or_N == "Y" or Y_or_N == "N":
                break
        if Y_or_N == "Y":
            xtra  = 0
            task_number = 1000**10
            while type(task_number) != int or task_number > tasks_in_list or type(task_number) != int and task_number > tasks_in_list:
                xtra += 1

                if xtra == 1:
                    task_number = input("select the number of the task (please use numericals e.g. 1, 2, 3, etc): ")
                else:
                    task_number = input("please use valid numericals (e.g. 1, 2, 3, etc): ")
                if type(task_number) != int:
                    try:
                        task_number = int(task_number)
                    except:
                        task_number = input("please use valid numericals (e.g. 1, 2, 3, etc): ")
                    else:
                        task_number = int(task_number)

            task_change = input("type what you want to change your task to or if you want to remove or confirm a task, type the command [remove]/[completion]/[change]: ").strip().lower()
            edit_commands = ["remove", "completion", "change"]
            while task_change not in edit_commands:
                task_change = input("please type the command [remove]/[completion]/[change]: ").strip().lower()

            task_number -= 1
            if task_change.lower().strip() == "change":
                task_list[task_number] = input("please type what you would like to change this task to: ")
            elif task_change.lower().strip() == "completion":
                task_list[task_number] = "{} - completed".format(task_list[task_number])
            elif task_change.lower().strip() == "remove":
                task_list.remove(task_list[task_number])
        else:  
            return "halt"
        
        
    


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
    if order in options_list[0] or order in options_list[3]:
        print("type command ['exit_task_list'] if you want to stop adding tasks.")
    if order in options_list[1] or order in options_list[4]:
        program_status = command_operator(order)
    else:
        command_operator(order)
        program_status = "running"
    while program_status != "exit_the_task_list" and program_status == "running":
        program_status = command_operator(order)

    





print("bye-bye.")


        
    