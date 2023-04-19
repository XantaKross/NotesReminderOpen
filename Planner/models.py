from django.db import models
from django.db import connection

# Create your models here.
class Planner(models.Model):
    Priority = models.AutoField(primary_key=True)
    Task = models.CharField(max_length=300)
    Add_On = models.DateTimeField(auto_now_add=True)
    DeadLine = models.DateTimeField(default="1900-12-12 12:12:12")
    NextUpdate = models.DateTimeField(default="1900-12-12 12:12:12")
    Username = models.ForeignKey("User_Interaction_Details", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Priority}, {self.Task}, {self.Add_On}, {self.Deadline}"

    @staticmethod
    def change_auto_increment_value(size):
        with connection.cursor() as cursor:
            cursor.execute(f"ALTER TABLE Planner_planner AUTO_INCREMENT = {size+1}")

class User_Interaction_Details(models.Model):
    Username = models.CharField(primary_key=True, max_length=30, default="AddedBefore")
    LLogin = models.DateTimeField()
    LInteract = models.DateTimeField(blank=True)
    
    def __str__(self):
        return f"{self.Username} {self.LLogin} {self.LInteract})"

