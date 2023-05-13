# The asvz bot

This repo contains a script to automatically enroll to ASVZ lessons

## Features

- Enroll to lesson
  - based on lesson ID (for lessons visited once)
  - based on sport ID, day, time, trainer, level, facility (for lessons visited periodically)
- Enroll to lesson that is already full
- Login as a member of
  - ETH
  - UZH
  - ZHAW
  - PHZH
  - ASVZ
- Save your credentials locally and reuse them on the next run
- Note: 
    UZH, ZHAW and PHZH use SWITCH edu-ID as login (*email* + password).
    ETH uses own login (*nethz* + password)
    ASVZ uses own login (*ASVZ-ID* + password)

## Run

### Prerequisites

You need to install the following:

- [Python 3](https://www.python.org/downloads/)
- [Chrome](https://support.google.com/chrome/answer/95346) or [Chromium](https://www.chromium.org/getting-involved/download-chromium)

### First time

```bash
cd src
python3 -m pip install venv
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 asvz_bot.py -h
```

### After the first time

```bash
cd src
source .venv/bin/activate
python3 asvz_bot.py -h
```

### Examples

Enroll by lesson ID and save credentials (locally in `.asvz-bot.json`)

```bash
python3 asvz_bot.py --organisation "ETH" --username "flbuetle" --save-credentials lesson 196346
```

Enroll by lesson ID and use saved credentials

```bash
python3 asvz_bot.py lesson 196346
```

Enroll by lesson attributes and use saved credentials

```bash
python3 asvz_bot.py training \
  --weekday "Mo" \
  --start-time "18:15" \
  --trainer "Karin Hollenstein" \
  --level "Fortgeschrittene" \
  --facility "Sport Center Hönggerberg" \
  45743
```


## Launcher

Enroll by using `asvz_bot_launcher.py`. 
```bash
python3 asvz_bot_launcher.py
```
Edit the lessons list to describe the lessons you would like to be enrolled in.
```
lessons = [
    {
        'weekday': 'Tu',
        'start-time': '17:00',
        'trainer': None,
        'facility': 'Sport Center Winterthur',
        'level': None,
        'sport_id': SPORT_IDS['Muscle Pump']
    },
    {
        'weekday': 'Fr',
        'start-time': '17:00',
        'trainer': None,
        'facility': 'Sport Center Winterthur',
        'level': None,
        'sport_id': SPORT_IDS['Muscle Pump']
    }
]

```
With the list above the bot will try to enroll you into the first Muscle Pump lesson after 17:00 on Tuesday and Friday in the Sport Center Winterthur.

### Running as a service

To run this in the background each time you start your pc add a file named `asvz.service` to `/etc/systemd/system`. 
```
[Unit]
Description=ASVZ Enroller
After=networking.target

[Service]
ExecStartPre=/bin/sleep 60
WorkingDirectory=/home/<user>/
User=<user>
ExecStart=/usr/bin/python3 /<path-to>/asvz-bot/src/asvz_bot_launcher.py

[Install]
WantedBy=multi-user.target
```

Then run 
```bash
sudo systemctl enable asvz
```
to activate the service.



## Development

### Script

TODO

### Mock

```bash
cd mock
docker-compose up --build
```
