
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    priority = models.IntegerField(default=1)  # 1 for low, 2 for medium, 3 for high
    completed = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField(null=True)

    def __str__(self):
        return self.title

    def delete_task(self):
        self.delete()

    def update_task(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.save()
