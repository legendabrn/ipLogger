from socket import *

# Данные сервера, айпи сервера, открытый порт сервера
addr = ('127.0.0.1', 7777)

# Лист для хранения всех IP
logIP = []

# Инициализация сокета
logger = socket(AF_INET, SOCK_DGRAM)

# Бинд сокета
logger.bind(addr)

# Бесконечный цикл
while True:
    
    # Получаем сообщение и айпи клиента
    conn, addr = logger.recvfrom(1024)
    
    # Делаем обработчик ошибок, дабы logIP.index не вывел "ValueError: '' is not in list"
    try: 
        # Если айпи найден в листе, продолжит данный код
        index = logIP.index(addr[0])
    except ValueError:
        # Если айпи не найден, то добавим его в лист и выведем в консоль
        logIP.append(addr[0])
        print('[IP LOGGER]', addr[0])

    
# Закрываем сокет
logger.close()
