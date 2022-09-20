from fileinput import filename
import json
from logger import error_log, warning_log
import pathlib
import tempfile
import pandas as pd
import os
tmpdir = tempfile.gettempdir()
filename = pathlib.Path('./notifications.json')


def new_notification(notification_object: dict, engine) -> None:
    if not os.path.exists('./notifications.json'):
        print("file created as it does not exist")
        with open('./notifications.json', 'x') as notification_file:
            notification_file.close()
            print("file closed")
    with open('./notifications.json', 'r') as notification_file:
        try:
            notifications = json.load(notification_file)
        except Exception as error:
            notifications = []
            warning_log(error)

    notifications.append(notification_object.copy())

    with open('./notifications.json', 'w') as notification_file:
        json.dump(notifications, notification_file, indent=2)
    df = pd.DataFrame.from_dict(notifications)
    df.to_sql('notifications', con=engine, if_exists='replace', index=False)

def update_notifications(engine) -> dict:
    with open(tmpdir+'/notifications.json', 'r') as notification_file:
        try:
            notifications = json.load(notification_file)
        except Exception as error:
            notifications = []
            warning_log(error)
    # print(tmpdir,'/notifications.json')
    return notifications