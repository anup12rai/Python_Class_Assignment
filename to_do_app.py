# Create a class named Task with attributes task_name, due_date, and is_completed.
# Implement methods to mark a task as completed and to display task details. 
# Then, create a class named ToDoList that manages a list of tasks using methods 
# like adding tasks, listing tasks, and marking tasks as completed.   

class task:
    def __init__(self, task_name, due_date,is_completed):
        self.task_name = task_name
        self.due_date = due_date
        self.is_completed = is_completed
        
    
    def complete(self):
        self.is_completed = True 
        #print(self.is_completed) 
         
    def display(self):
        print(self.task_name)
        print(self.due_date)
        print(self.is_completed)
            

task1 = task("task1","2081/2/5",False)

task1.complete()
task1.display()
        