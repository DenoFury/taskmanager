import datetime
import sys
class Task:
 
  def __init__(self, title, description=" ", done=False, date=None):
    if not title:
      raise ValueError("Invalid title")
    self.title = title
    self.description = description
    if date == None:
      x = datetime.datetime.now()
      self.date = x.strftime("%x")
    else:
      self.date = date
    self.done = done

  def __str__(self):
    return f"Your task {self.title} is {self.done} due {self.date}"

  @property
  def done(self):
    return self._done

  @done.setter
  def done(self, done):
    if type(done) != bool:
      raise ValueError("Error setting done")
    self._done = done

  @property
  def title(self):
    return self._title

  @title.setter
  def title(self, title):
    if not title:
      raise ValueError("Error setting title")
    self._title = title

  @property
  def description(self):
    return self._description

  @description.setter
  def description(self, description):
    self._description = description

  @property
  def date(self):
    return self._date

  @date.setter
  def date(self, date):
    self._date = date



class TaskNotFoundError(Exception):
  pass


class TaskManager:
  def __init__(self):
    self.next_id = 1 
    self.taskDict = {}

  def __str__(self):
    text = ""
    for id,task in self.taskDict.items():
      text += f"\nTask id: {id} - {task}"
    return text
  def add_task(self, title, description=" ", done=False, date=None):
    t = Task(title, description, done, date)
    self.taskDict[self.next_id] = t
    self.next_id += 1

  def complete_task(self, id):
    try:
      if id not in self.taskDict:
        raise TaskNotFoundError("Task doesn't exist!")
      else:
        self.taskDict[id].done = True
    except TaskNotFoundError:
      print("Task doesn't exist!")

      
  def delete_task(self, id):
    try:
      if id not in self.taskDict:
        raise TaskNotFoundError("Task doesn't exist!")
      else:
        self.taskDict.pop(id)
    except TaskNotFoundError:
      print("Task doesn't exist!")                     


def main():
  quit = False
  taskManager = TaskManager()
  while(not quit):
    try:
      choice = int(input("\nWhat would you like to do: \n 1. Create task \n 2. View tasks \n 3. Delete Task \n 4. Complete task \n 5. Quit \n"))
    except ValueError:
      print("Please write a number from 1 to 5")
      continue
    match choice:
      case 1:
        taskName = input("Name of your task: ")
        taskDescription = input("Description of task (optional) ")
        taskDate = input("Choose a date ")
        taskManager.add_task(title=taskName, description=taskDescription, date=taskDate)
        print("Task created successfully! Going back to main menu.... \n")
      case 2:
        print(taskManager)
      case 3:
        try:
          taskId = int(input("Provide ID of the task to remove: "))
        except ValueError:
          print("Invalid task ID, going back to main menu...")
          continue
        taskManager.delete_task(taskId)
        print("Task deleted successfully! \n Going back to main menu.... \n")
        
      case 4:
        try:
          taskId = int(input("Provide ID of the task to mark as complete: "))
        except ValueError:
          print("Invalid task ID, going back to main menu...")
          continue
        taskManager.complete_task(taskId)
        print("Task completed successfully!\n Going back to main menu.... \n")
      case 5: 
        quit = True
      case _:
        print("Invalid number, write a number from 1 to 5")
        continue  


if __name__ == "__main__":
  main()