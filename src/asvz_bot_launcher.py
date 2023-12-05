from asvz_bot import *
import subprocess
import os
import time

SPORT_IDS = {
    'Muscle Pump': 45686
}

lessons = [
    {
        'weekday': 'Tu',
        'start-time': '17:55',
        'trainer': None,
        'facility': 'Sport Center Winterthur',
        'level': None,
        'sport_id': SPORT_IDS['Muscle Pump']
    },
    {
        'weekday': 'Fr',
        'start-time': '18:00',
        'trainer': None,
        'facility': 'Sport Center Winterthur',
        'level': None,
        'sport_id': SPORT_IDS['Muscle Pump']
    }
]

if __name__ == '__main__':
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    for lesson in lessons:
        keys = list(lesson)
        command = "python3 asvz_bot.py training"
        for key in keys:
            value = lesson[key]
            if value != None and key != 'sport_id':
                command += f" --{key} \"{value}\""
        command += f" {lesson['sport_id']}"
        print(command)
        process = subprocess.Popen(command, shell=True)
    
    time.sleep(604800)