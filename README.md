# api_final_yatube

## Api для социальной сети yatube

### Технологии

- Python 3.7.0
- Django 2.2.16
- Django REST framework 3.12.4
- Simple JWT 4.7.2

## Запуск проекта
Клонировать репозиторий и перейти в него в командной строке:
```sh
git clone https://github.com/haus2100/api_final_yatube.git
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```sh
python3 -m venv venv
source venv/bin/activate
```
Установить зависимости из файла requirements.txt:
```sh
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:
```sh
python3 manage.py migrate
```
Запустить проект:
```sh
python3 manage.py runserver
```
Обратиться к проекту:
http://127.0.0.1:8000
Доступ к документации:
http://127.0.0.1:8000/redoc
