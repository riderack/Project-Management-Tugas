from datetime import date, datetime

class Task:
  def __init__(
    self, task_id, title, course, deadline, priority, estimated_hours, status="Belum Mulai"):

    self.task_id = int(task_id)
    self.title = title.strip()
    self.course = course.strip()
    self.deadline = deadline
    self.priority = priority
    self.estimated_hours = float(estimated_hours)
    self.status = status

def days_remaining(self, today=None):
  if today is None:
    today = date.today()
  return (self.deadline - today).days

