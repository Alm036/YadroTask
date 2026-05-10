# Скрипт для теста http-запросов


## Раздел 1
Запуск скрипта:
```bash
python3 script.py
```

Также можно передать домен сайта в параметры скрипта:
```bash
python3 script.py tools-httpstatus.pickup-services.com
```

## Раздел 2

Сборка контейнера:
```bash
docker build -t http-checker .
```

Запуск контейнера:
```bash
docker run --name http-checker-container http-checker
```

Проверка работоспособности через docker logs:
```bash
docker logs http-checker-container
```

## Раздел 3

Установка коллекции community.docker:
```bash
ansible-galaxy collection install community.docker
```

Запуск playbook:
```bash
ansible-playbook playbook.yaml -i inventory.ini --ask-become-pass
```
