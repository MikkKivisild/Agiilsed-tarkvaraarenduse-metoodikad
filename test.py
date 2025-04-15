class Task:
    def __init__(self, title, status="to-do"):
        self.title = title
        self.status = status

    def mark_done(self):
        self.status = "done"