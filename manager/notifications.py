from fileinput import filename
import json
from logger import error_log, warning_log
import pathlib
import tempfile
import os
tmpdir = tempfile.gettempdir()
filename = pathlib.Path('./notifications.json')


def new_notification(notification_object: dict):
    '''
    This function is used to create a new notification and storing it in the database 
    using the engine object.
    '''
    if not os.path.exists('./notifications.json'):
        with open('./notifications.json', 'x') as notification_file:
            notification_file.close()
    with open('./notifications.json', 'r') as notification_file:
        try:
            notifications = json.load(notification_file)
        except Exception as error:
            notifications = []
            warning_log(error)

    notifications.append(notification_object.copy())

    with open('./notifications.json', 'w') as notification_file:
        json.dump(notifications, notification_file, indent=2)
    return notifications
