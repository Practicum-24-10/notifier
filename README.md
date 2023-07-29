# Notification Service

### Запуск приложения
- Создать файл .env в директории backend/ по примеру backend/.env.example и из корня проекта выполнить команду:
```
docker compose -f backend/docker-compose.yml up
```

### Запуск приложения для разработки (с проброской портов и монтированием директории приложения)
- Создать файл .env в директории backend/ по примеру backend/.env.example и из корня проекта выполнить команду:
```
docker compose -f backend/docker-compose.yml -f backend/docker-compose.override.yml up
```

### Запуск тестов pytest
- Выполнить команду:
```
docker compose -f backend/tests/functional/docker-compose.yml up
```


### pre-commit
```
pip install -r requirements.txt
pre-commit install
```
