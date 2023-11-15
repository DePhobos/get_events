from kubernetes import client, config
import json
import time

# Загрузка конфигурации Kubernetes
config.load_kube_config()

# Создание объекта для работы с API событий Kubernetes
v1 = client.CoreV1Api()

# Определение типов событий, которые необходимо получить
event_types = ['Warning', 'Error']

# Получение всех событий Kubernetes с указанными типами
events = v1.list_event_for_all_namespaces(field_selector=f"type=Warning,type=Error").items

# Создание имени файла с временной меткой
current_timestamp = str(int(time.time()))
filename = f'events_{current_timestamp}.json'

# Запись событий в JSON-файл
with open(filename, 'w') as file:
    event_list = [event.to_dict() for event in events]
    json.dump(event_list, file, indent=4)

print(f'События записаны в файл {filename}')
