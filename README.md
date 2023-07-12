# Booking app

Steps to launch the application

    1.Copy the repository
    2.git clone https://github.com/Alexandrhub/test_fastapi.git
    3.Go to the cd test_fastapi folder, copy the configuration files cd .env.example .env-non-dev and fill them in.
    4.Choose your virtual environment and run the make install-deps command to install all dependencies.
    5.To run make migrate
    6.Linters and formatter make black and make flake8
    7. For local startup, enter the make run command 
    8.For startup problems, try the make clean command
    9.To start all services (DB, Redis, web server (FastAPI), Celery, Flower, Grafana, Prometheus) use the docker-compose.yml file and the make up or make down commands to start and stop respectively



### Celery & Flower
The command used to start Celery is

celery --app=app.tasks.celery:celery worker -l INFO -P solo

Note that -P solo is only used on Windows, as Celery has problems running on Windows.
The command used to start Flower is

celery --app=app.tasks.celery:celery flower
These are already included in the docker container startup settings

### Dockerfile
If you have changed something inside Dockerfile, that is, changed the logic for composing the image Run the docker build command .
Sentry

To configure logging, register on the off.site or google/github Select the framework of your project and copy sentry_dns that you are offered and enter it in the .env-non-dev file.
### Sentry
To configure logging, register on the off.site or google/github Select your project framework and copy the sentry_dns you are prompted for and enter it in the .env-non-dev file.


### Grafana / Prometheus
(https://grafana.com//tutorials/grafana-fundamentals/)

To enter the cabinet you need to specify username: admin, password: admin
    Then override the password
    To make the charts work you have to specify your uid in grafana-dashboard in the following piece of code: "datasource":{"type": "prometheus", "uid": "YOUR UID"} 
    You can get it from the json schema of the preset dashboards
    (in settings add data source -> prometheus -> "choose name"). Then in Dashboards -> import -> Paste the contents of grafana-dashboard.json and choose some random uuid(and name for the dashboard)
    If you don't care about metrics / logging you can disable it by commenting out the sentry and instumentator lines in app/main.py and docker-compose file

### Документация

- [x] Swagger UI <localhost:8000/docs>
- [x] ReDoc <localhost:8000/redoc>
- [x] Api routes <localhost:8000/api/v1/docs>

## Обратная связь
Любые комментарии, исправления, замечания пишите мне в [телеграм](https://t.me/alex_cherr).
