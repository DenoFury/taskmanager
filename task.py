import datetime
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
t2 = Task("Buy groceries", done="Yes")
print(t)
print(t1)
print(t2)