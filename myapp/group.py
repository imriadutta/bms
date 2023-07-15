class EachGroup:
    def __init__(self, name, admin, created_on, modified_on, task, date, time):
        self.name = name
        self.admin = admin
        self.created_on = created_on
        self.modified_on = modified_on
        self.members = []
        self.task = task
        self.deadline_date = date
        self.deadline_time = time
