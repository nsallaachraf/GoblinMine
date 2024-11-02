[![Static Badge](https://img.shields.io/badge/Telegram-Bot%20Link-Link?style=for-the-badge&logo=Telegram&logoColor=white&logoSize=auto&color=blue)](https://t.me/GoblinMine_bot/start?startapp=6218943204)

# Бот для GoblinMine

# 🔥🔥 Используйте Python 3.10 - 3.11.5 🔥🔥

> 🇪🇳 README in english available [here](README-EN)

## Функционал  
|                   Функционал                   | Поддерживается |
|:----------------------------------------------:|:--------------:|
|                Многопоточность                 |       ✔️       | 
|                   Ночной мод                   |       ✔️       | 
| Авто-регистрация аккаунта по вашей реф. ссылке |       ✔️       |
|             Автообновление шахты               |       ✔️       |
|            Автообновление шахтеров             |       ✔️       |
|      Автоматическое обновление инвентаря       |       ✔️       |
|              Автоапгрейд тележки               |       ✔️       |
|          Поддержка pyrogram .session           |       ✔️       |


## [Настройки](https://github.com/nsallaachraf/GoblinMine/blob/main/.env-example/)
| Настройки                   |                Описание                                                               |
|-----------------------------|:-------------------------------------------------------------------------------------:|
| **API_ID / API_HASH**       | Данные платформы, с которой будет запускаться сеанс Telegram (по умолчанию — Android) |       
| **REF_ID**                  |                                  Укажите свой реф ID                                  |
| **NIGHT_MOD**               |                            Ночной мод (по умолчанию: True)                            |
| **NIGHT_TIME**              |                      Время ночного мода (по умолчанию: [23, 6])                       |
| **SLEEP_BETWEEN_START**     |            Задержка перед запуском каждого сеанса (по умолчанию: [10, 20])            |
| **BOT_SLEEP_TIME**          |      Время сна после завершения всех действий бота (по умолчанию: [3000, 3500])       |
| **AUTO_UPGRADE_MINE_LEVEL** |              Автоматическое повышение уровня шахты (по умолчанию: True])              |
| **AUTO_UPGRADE_MINERS**     |                Автоматическое обновление майнеров (по умолчанию: True)                |
| **AUTO_UPGRADE_MINE**       |                 Автоматическое обновление шахты (по умолчанию: True)                  |
| **UPGRADE_INVENTORY**       |               Автоматическое обновление инвентаря (по умолчанию: True)                |
| **AUTO_UPGRADE_CART**       |                Автоматическое обновление корзины (по умолчанию: True)                 |
| **SEND_EXPEDITION**         |                Автоматическая отправка экспедиции (по умолчанию: True)                |
| **USE_PROXY_FROM_FILE**     |          Использовать ли прокси из файла /proxies.txt (по умолчанию: False)           |

## Быстрый старт 📚

Для быстрой установки и последующего запуска - запустите файл `run.bat` на **Windows** или `run.sh` на **Линукс**

## Предварительные условия
Прежде чем начать, убедитесь, что у вас установлено следующее:
- [**Python**](https://www.python.org/downloads/release/python-3115/) **ВАЖНО**: Убедись что используешь **3.11.5**

## Получение API ключей
1. Перейдите на сайт [**my.telegram.org**](https://my.telegram.org/auth) и войдите в систему, используя свой номер телефона.
2. Выберите `API development tools` и заполните форму для регистрации нового приложения.
3. Запишите `API_ID` и `API_HASH` в файле `.env`, предоставленные после регистрации вашего приложения.

## Установка
Вы можете скачать [**Репозиторий**](https://github.com/nsallaachraf/GoblinMine) клонированием на вашу систему и установкой необходимых зависимостей:
```shell
git clone https://github.com/nsallaachraf/GoblinMine.git
cd GoblinMine
```

Затем для автоматической установки введите:

Windows:
```shell
run.bat
```

Linux:
```shell
run.sh
```

# Linux ручная установка
```shell
sudo sh install.sh
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cp .env-example .env
nano .env  # Здесь вы обязательно должны указать ваши API_ID и API_HASH , остальное берется по умолчанию
python3 main.py
```

Также для быстрого запуска вы можете использовать аргументы, например:
```shell
~/GoblinMine >>> python3 main.py --action (1/2)
# Or
~/GoblinMine >>> python3 main.py -a (1/2)

# 1 - Запускает кликер
# 2 - Создает сессию
```


# Windows ручная установка
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env-example .env
# Указываете ваши API_ID и API_HASH, остальное берется по умолчанию
python main.py
```

Также для быстрого запуска вы можете использовать аргументы, например:
```shell
~/GoblinMine >>> python main.py --action (1/2)
# Или
~/GoblinMine >>> python main.py -a (1/2)

# 1 - Запускает кликер
# 2 - Создает сессию
```