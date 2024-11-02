[![Static Badge](https://img.shields.io/badge/Telegram-Bot%20Link-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/GoblinMine_bot/start?startapp=6218943204)


#  Bot for GoblinMine

![start-goblinmine](https://github.com/user-attachments/assets/a4d30be3-0a47-4b29-9666-bb3402a6d97d)


# 🔥🔥 Use PYTHON 3.10 - 3.11.5 🔥🔥

> 🇷 🇺 README in russian available [here](README-RU.md)

## Features  
| Feature                        | Supported |
|--------------------------------|:---------:|
| Multithreading                 |     ✔     |
| Auto ref                       |     ✔     |
| Night mod                      |     ✔     |
| Auto upgrade mine              |     ✔     |
| Auto upgrade miners            |     ✔     |
| Auto upgrade inventory         |     ✔     |
| Auto upgrade cart              |     ✔     |
| Auto expedition                |     ✔     |
| Support for pyrogram .session  |     ✔     |

## [Settings](https://github.com/nsallachraf/GoblinMine/blob/main/.env-example)
| Settings                    |                               Description                                |
|-----------------------------|:------------------------------------------------------------------------:|
| **API_ID / API_HASH**       | Platform data from which to run the Telegram session (default - android) |       
| **REF_ID**                  |                             Put your ref ID                              |
| **NIGHT_MOD**               |                        Night mod (default: True)                         |
| **NIGHT_TIME**              |                  Time for night mod (default: [23, 6])                   |
| **SLEEP_BETWEEN_START**     |         Delay before launching each session (default: [10, 20])          |
| **BOT_SLEEP_TIME**          |  Sleep time after all bot actions are completed (default: [3000, 3500])  |
| **AUTO_UPGRADE_MINE_LEVEL** |              Automatic mine level upgrade (default: True])               |
| **AUTO_UPGRADE_MINERS**     |               Automatic upgrade of miners (default: True)                |
| **AUTO_UPGRADE_MINE**       |                  Automatic mine upgrade (default: True)                  |
| **UPGRADE_INVENTORY**       |               Automatic inventory upgrade (default: True)                |
| **AUTO_UPGRADE_CART**       |                  Automatic cart upgrade (default: True)                  |
| **SEND_EXPEDITION**         |               Automatic expedition sending (default: True)               |
| **USE_PROXY_FROM_FILE**     |   Whether to use a proxy from the /proxies.txt file (default: False)     |



## Quick Start

To install libraries and run bot - open run.bat on Windows

## Prerequisites
Before you begin, make sure you have the following installed:
- [**Python**](https://www.python.org/downloads/release/python-3115/) **IMPORTANT**: Make sure to use **3.11.5**. 

## Obtaining API Keys
1. Go to [**my.telegram.org**](https://my.telegram.org/auth) and log in using your phone number.
2. Select `API development tools` and fill out the form to register a new application.
3. Record the `API_ID` and `API_HASH` provided after registering your application in the `.env` file.

## Installation
You can download the [**repository**](https://github.com/nsallaachraf/GoblinMine) by cloning it to your system and installing the necessary dependencies:
```shell
git clone https://github.com/nsallaachraf/GoblinMine.git
cd GoblinMine
```

Then you can do automatic installation by typing:

Windows:
```shell
run.bat
```

Linux:
```shell
run.sh
```

# Linux manual installation
```shell
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Here you must specify your API_ID and API_HASH, the rest is taken by default
python3 main.py
```

You can also use arguments for quick start, for example:
```shell
~/GoblinMine >>> python3 main.py --action (1/2)
# Or
~/GoblinMine >>> python3 main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
```

# Windows manual installation
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Here you must specify your API_ID and API_HASH, the rest is taken by default
python main.py
```
You can also use arguments for quick start, for example:
```shell
~/GoblinMine >>> python3 main.py --action (1/2)
# Or
~/GoblinMine >>> python3 main.py -a (1/2)

# 1 - Run clicker
# 2 - Creates a session
```
