# Веб-приложение для Funtech
## I. Сведения о команде

| роль в проекте | имя и фамилия | контакты 
| ------ | ------ |  ------ |
| Project Manager |  Мария Уракова  | https://t.me/uramasha
| Product Manager | Александр Леванов  | https://t.me/Aleksandr_Levanov
| UX/UI Designer | Елена Отт | https://t.me/lena_ott
| UX/UI Designer | Анна Ненашева | https://t.me/AnnaNenashevaNL
| Systems Analyst | Екатерина Васильева | https://t.me/tiramisuspb
| Systems Analyst | Наталья Баптиданова  | https://t.me/texdecor
| Systems Analyst | Василиса Беспалая  | https://t.me/Lisadereza
| Business Analyst | Елена Сафонова  | https://t.me/ElenaS_SEA
| Frontend Developer | Владислав Сердюков | https://t.me/VladisSerd
| Backend Developer | Сергей Барышевский  | https://t.me/Rexten
| Backend Developer | Станислав Андрющенко | https://t.me/StAndSt
| Backend Developer | Дмитрий Печенков | https://t.me/imperatorObi1Kenobi


## II. Ссылка на Swagger
*http://funtech.b2k.me/api/v1/swagger/
*http://funtech.b2k.me/api/v1/redoc/
## III. Инструкция по сборке и запуску
![GitHub repo size](https://img.shields.io/github/repo-size/StAndUP-ru/events)
![Static Badge](https://img.shields.io/badge/test_coverage-95%25-FFDF00)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/StAndUP-ru/events)

### Клонирование
Клонировать репозиторий
```
git clone git@github.com:StAndUP-ru/events.git
```
Перейти в директорию events
```
cd events
```
Создать виртуальное окружение
```
python3.11 -m venv venv
```
Активировать виртуальное окружение
```
. ./venv/bin/activate
```
Обновить установщик пакетов pip
```
pip install --upgrade pip
```
Установить зависимости
```
pip install -r requirements.txt
```
В директории events_app скопировать файл `.env.example` в `.env` и задать значения переменным

### Сборка в Docker

## IV. Cтэк технологий 
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
## V. Cсылки на сторонние фреймворки, библиотеки, иконки и шрифты если использовались


![Иллюстрация к проекту](https://github.com/author2020/events/blob/sa/image2.png)


## Docker

```sh
docker pull standup1990/event
```

## License

MIT
