#import mysql.connector as connector

"""database = connector.connect(user='xanta',
                             password='0mn1v35s4',
                             host='127.0.0.1',
                             database='Notes',
                             auth_plugin="mysql_native_password",
                             autocommit="True")
"""

from datetime import timedelta, datetime
import re

def dist(time):
    distance = (time.replace(microsecond=0) - datetime.now().replace(microsecond=0))/2
    print(datetime.now().replace(microsecond=0) + distance)
    return datetime.now().replace(microsecond=0) + distance


def norm_time(datetimeobj):
    return datetimeobj.strftime(("%d/%m/%Y, %H:%M:%S"))

def norm(string):
    if ',' in string: # if time/date given manually then;
        task, timedetails = string.split(',')
        # in order to set dd/mm/year instead of stupid format.
        task, timedetails = task.strip(), timedetails.replace(',', '').strip()

        print(timedetails)
        format = ["%d/%m/%Y %H:%M:%S"]
        temporal = datetime.strptime(re.sub(" +", " ", timedetails), format[0])

    else: # default. set time/date split = 1;
        task = string
        temporal = datetime.now().replace(microsecond=0) + timedelta(days=1)

    return task.strip(), temporal


def filter_(list, element):
    return [item for item in list if item != element]

class clsmemory:
    def __init__(self):
        self.list = []