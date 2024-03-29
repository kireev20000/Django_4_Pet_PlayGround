# Django 4 Pet PlayGround

Pet-проект для экспериментов с Django 4.
 
***
## Особенности проекта
- Отрабатываю полученные знание на практике.
- Использую по возможности самые современные технологии.

***
## Текущий прогресс
- приложение для ведения блога на Django 4 (Done);
- веб-сайт по управлению визуальными закладками (Done);

### Особенности приложения Blog
- использование канонических URL-адресов для моделей;
- создание дружественных для поисковой оптимизации URL-адресов
постов;
- добавление постраничной разбивки в представление списка постов;
- разработка представлений на основе классов;
- отправка электронных писем с помощью Django;
- использование форм Django, позволяющих делиться постами по электронной почте;
- добавление комментариев к постам с использованием форм из моделей.
ующие темы:
- использование приложения django-taggit для реализации системы тегирования;
- сложные запросы для рекомендации схожих постов;
- создание карты сайта с использованием фреймворка карт сайтов;
- формирование новостной RSS-ленты с использованием фреймворка
 новостных лент;
- реализация полнотекстового поискового механизма с использованием
Django и PostgreSQL

### Особенности приложения с визуальными закладками
- использование JavaScript вместе с Django;
- формирование букмарклета JavaScript;
- генерирование миниатюр изображений с помощью easy-thumbnails;
- реализация асинхронных HTTP-запросов с помощью JavaScript
и Django;
- разработка бесконечной постраничной прокрутки
- разработана системы подписки;
- создание приложения потока активности;
- ведение подсчета просмотров изображений с помощью хранилища
Redis;
- создание рейтинга самых просматриваемых изображений с помощью
хранилища Redis

## Подготовка и запуск проекта
### Склонировать репозиторий на локальную машину:
```
git clone git@github.com:kireev20000/Django_4_Pet_PlayGround.git
```
***- Установите зависимости из файла requirements.txt:***
```
pip install -r requirements.txt
```

***- Примените миграции:***
```
python manage.py migrate
```

### Запускаем внешние БД в докере:
Установить и настроить PostgreSQL и Redis в докере

```
docker pull redis
docker run -it --rm --name redis -p 6379:6379 redis
```
***- В папке с файлом manage.py выполните команду для запуска локально:***
```
python manage.py runserver
```
Cоздать и заполнить .env файл в корневой директории
```
SECRET_KEY = "ваш_ключ_Django"
```


## Об авторе <a id=7></a>

Киреев Александр Олегович  
Python-разработчик (Backend)  
E-mail: kireev20000@yandex.ru
Telegram: @kireev20000

# Инструкция по запуску
