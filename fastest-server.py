import threading
import time
import requests

# Список серверов для тестирования (можно заменить своими)
servers = [
    "https://mirror.yandex.ru/",
    "https://ftp.gnu.org/",
    "https://mirrors.edge.kernel.org/",
    "https://mirror.centos.org/",
    "https://download.opensuse.org/",
]

# Количество тестовых запросов к каждому серверу
NUM_REQUESTS = 3

# Словарь для хранения результатов
results = {}

# Функция тестирования скорости сервера
def test_server_speed(server):
    times = []
    for _ in range(NUM_REQUESTS):
        try:
            start = time.time()
            response = requests.get(server, timeout=5)  # Делаем запрос с таймаутом 5 сек
            response.raise_for_status()  # Проверяем успешность запроса
            times.append(time.time() - start)  # Записываем время запроса
        except requests.RequestException:
            times.append(float('inf'))  # Если ошибка — ставим бесконечное время
    avg_time = sum(times) / len(times)  # Среднее время запроса
    results[server] = avg_time  # Сохраняем в словарь


# Запускаем тестирование в нескольких потоках
threads = []
for server in servers:
    thread = threading.Thread(target=test_server_speed, args=(server,))
    threads.append(thread)
    thread.start()

# Ждем завершения всех потоков
for thread in threads:
    thread.join()

# Сортируем серверы по скорости
sorted_results = sorted(results.items(), key=lambda x: x[1])

# Выводим результаты
print("\nРезультаты тестирования серверов:")
for server, time in sorted_results:
    print(f"{server} — {time:.3f} сек")

# Выводим самый быстрый сервер
best_server = sorted_results[0][0]
print(f"\n🔹 Самый быстрый сервер: {best_server} 🚀")
