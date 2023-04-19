from __future__ import absolute_import, unicode_literals
from celery import shared_task
from wa_automate_socket_client import SocketClient
from Planner.models import User_Interaction_Details, Planner
from Accounts.models import CustomUser
from datetime import datetime, timedelta
from Planner.common_ import dist

@shared_task()
def run_whats_interface():
    client = SocketClient('http://localhost:8085/', 'secure_api_key')
    today = str(datetime.now().date() + timedelta(days=1))
    four_days_ago = str(datetime.now().date() - timedelta(days=4))
    current_time = datetime.now().replace(microsecond=0)

    users_in_queue = list(User_Interaction_Details.objects.filter(LLogin__range=[four_days_ago, today]).values_list("Username", flat=True))
    reminders_in_queue = {name : Planner.objects.filter(Username=name).values_list("Task", "DeadLine", "NextUpdate") for name in users_in_queue}

    for username in users_in_queue:
        string_ph = CustomUser.objects.filter(username=str(username)).values_list("phone_number", flat=True)  # number to send message to. # view function.
        phone_number = f"91{str(string_ph[0])}@c.us"

        if len(reminders_in_queue) >= 1:
            for row in reminders_in_queue[username]:
                # [task, deadline, update/reminder time]
                if row[2].replace(microsecond=0) <= current_time:
                    client.sendText(phone_number, f"Your Task: {str(row[0])}\nDeadline: {row[1]}")
                    row = Planner.objects.get(Task=str(row[0]))
                    row.NextUpdate = dist(datetime.now().replace(microsecond=0))
                    row.save()
        else: continue



    client.disconnect()