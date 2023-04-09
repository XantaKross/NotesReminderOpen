from django.db import models
from django.db import connection

# Create your models here.
class Planner(models.Model):
    Priority = models.AutoField(primary_key=True)
    Task = models.CharField(max_length=300)
    Add_On = models.DateTimeField(auto_now_add=True)
    Deadline = models.DateTimeField()
    Username = models.CharField(max_length=30, default="AddedBefore",blank=False)

    def __str__(self):
        return f"{self.Priority}, {self.Task}, {self.Add_On}, {self.Deadline}"

    @staticmethod
    def change_auto_increment_value(size):
        with connection.cursor() as cursor:
            cursor.execute(f"ALTER TABLE Planner_planner AUTO_INCREMENT = {size+1}")
