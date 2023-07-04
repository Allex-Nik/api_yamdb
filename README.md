# api_yamdb
api_yamdb 
 
Для того чтобы открыть проект: 
1. Клонируйте репозиторий себе на ПК.  
Например командой 'git clone' в терминале. Ссылка для команды расположена на закладке Code->Local->SSH 
2. Установите и активируйте виртуальное окружение. Пример для macOS: 
Установить: python3 -m venv venv 
Активировать: source venv/bin/activate 
3. Установите зависимости 
pip install -r requirements.txt 
При необходимости обновите pip (инструкция отобразится в терминале) 
4. Выполните миграции (в директории с manage.py): 
python3 manage.py migrate 
5. Запустите сервер (в директории с manage.py): 
python3 manage.py runserver 