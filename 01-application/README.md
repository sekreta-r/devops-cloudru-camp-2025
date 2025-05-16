# Echo Server

Простейший echo-сервер, разработанный на Python с использованием FastAPI, который отображает:

* имя хоста
* IP-адрес хоста
* имя автора, передаваемое через переменную окружения `$AUTHOR`

## Используемые технологии

* **Язык программирования:** Python 3.12.9
* **Управление зависимостями:** Poetry 2.1.3
* **Веб-фреймворк:** FastAPI 0.115.12
* **Инструменты разработки:** DevContainer с предустановленным `hadolint` для удобной проверки Dockerfile

## Запуск контейнера

Для запуска сервера локально из Docker-образа:

```bash
docker run --rm -e AUTHOR="Sekretaria" -p 8000:8000 sekretaria/echo-server:0.1.0
```

После запуска приложение будет доступно по адресу:
[http://localhost:8000](http://localhost:8000)

Репозиторий: [sekretaria/echo-server on Docker Hub](https://hub.docker.com/r/sekretaria/echo-server)

## Сборка и публикация Docker-образа

Сборка production-образа:

```bash
docker build --target prod -t sekretaria/echo-server:0.1.0 .
```

Публикация в **приватный Docker Hub-репозиторий**:

```bash
docker push sekretaria/echo-server:0.1.0
```

## Разработка и линтинг

Разработка велась в DevContainer на базе `dockerfile` с отдельным `dev`-слоем.

В `dev`-сборке установлены:

* `curl`
* `hadolint` — для анализа Dockerfile на предмет ошибок и несоответствий best practices

