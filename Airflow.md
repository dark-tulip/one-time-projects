Шаг 1
# Проверить версию Python
```
python3 --version
```
# Создать виртуальное окружение
```
mkdir ~/airflow-project && cd ~/airflow-project
python3 -m virtualenv venv
source venv/bin/activate
```
Шаг 2
# Устанавливаем зависимости
```
brew install sqlite postgresql
```
# Устанавливаем переменную окружения
```
export AIRFLOW_HOME=~/airflow
echo 'export AIRFLOW_HOME=~/airflow' >> ~/.zshrc
source ~/.zshrc
```
# Устанавливаем Airflow
```
pip install "apache-airflow==2.7.1" --constraint
"https://raw.githubusercontent.com/apache/airflow/constraints-2.7.1/constraints-3.8.txt"
```
Шаг 3 - 4
# Инициализируем базу данных
```
airflow db init
```
# Создаем админа
```
airflow users create \
--username admin \
--firstname YOUR_NAME \
--lastname YOUR_SURNAME \
--role Admin \
--email your_email@example.com
```
# Запуск
```
airflow webserver --port 8080
```
