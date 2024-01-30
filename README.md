# приложение поварской книги

## Зависимости:

Установить предварительно данное ПО:

1. [Docker Desktop](https://www.docker.com).
2. [Git](https://github.com/git-guides/install-git).
3. [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/download) (optional).

## Установка

Clone проекта с репозитория к себе.

1. Для конфигурации приложения, скопируйте `.env.sample` в `.env` файл:
    ```shell
    cp .env.sample .env
    ```
   
    Этот файл содержит переменные среды, значения которых будут использоваться во всем приложении. Файл примера (`.env.sample`) содержит набор переменных со значениями по умолчанию. Таким образом, его можно настроить в зависимости от среды.


2. Соберите контейнер используя Docker Compose:
    ```shell
    docker compose build
    ```
    Эту команду следует запускать из корневого каталога, где находится `Dockerfile`.
    Вам также необходимо заново собрать Docker-контейнер, если вы обновили `requirements.txt`.
   
3. Теперь можно запустить контейнер:
    ```shell
    docker compose up
    ```
   После старта контейнера можно перейти по ссылкам [http://0.0.0.0:8000](http://0.0.0.0:8000). Вы можете открыть их в браузере

4. Для запуска приложения в bash:
    Присоединяемся к приложению в Docker-container:
    ```shell
    docker compose exec app bash
    ```
   Делаем миграции в БД:
    ```shell
    ./manage.py migrate
    ```

## Использование

1. Для того чтоб попасть в админку нужно создать superuser.
    Коннектимся к нашему приложению Docker-container (если вы вышли из контейнера):
    ```shell
    docker compose exec app bash
    ```
   Создаем superuser:
    ```shell
    ./manage.py createsuperuser
    ```
2. Пройдите по адресу [http://0.0.0.0:8000/admin](http://0.0.0.0:8000/admin) и можете управлять данными через админ панель.

3. чтоб заполнить таблицы тестовыми данными
	```shell
    ./manage.py loaddata products.json
    ```
	```shell
    ./manage.py loaddata recipe_products.json
    ```
	```shell
    ./manage.py loaddata recipes.json
    ```