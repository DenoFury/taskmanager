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

  
t = Task("Buy groceries")
t1 = Task("Buy groceries", date="12/25/2026")

print(t)
print(t1)

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


taskmanager = TaskManager()
taskmanager.add_task("Buy groceries")
taskmanager.add_task("Buy groceries",  date="12/25/2026")
print(taskmanager)

taskmanager.complete_task(1)
print(taskmanager)

taskmanager.delete_task(2)
print(taskmanager)

taskmanager.complete_task(99)