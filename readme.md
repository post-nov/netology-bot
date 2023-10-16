# Бот школы нетологии "Как преподавать в онлайне?"

Бот:
https://t.me/netology_teaching_bot

Написан с использованием python библиотеки **python-telegram-bot**. Включен режим асинхронной обработки команд,
т.е. имеется поддержка работы с несколькими пользователями одновременно. 

Все медийные файлы (видео, фото) содержатся в отдельном канале, пересылаются из него в бота по необходимости. 
Т.е. бот отправляет только текстовые сообщения, нагрузка на канал минимальная.

### Переменные окружения, необходимые для работы бота
- *TOKEN* - токен к основному боту
- *TOKEN2* - токен к боту для дебага
- *MEDIA_CHANNEL_ID* - идентификатор канала, содержащего медийные сообщения (фото, видео)
- *DEBUG* - режим дебага

### Структура проекта
- main.py - Точка входа. Через него запускается проект, в нем описаны команды бота
- constants.py - Константы
- utils.py - Вспомогательные методы
- blocks/* - Смысловые блоки 

### Режим дебага
В режиме дебага подключение выполняется через альтернативный токен, а задержка между сообщениями отсутствует. 
Сделан для того, чтобы можно было быстро отлаживаться через отдельный процесс, не
блокируя работу основного бота

### Сохранение пользовательских данные
Выполняется методом utils.process_user_data. Вызывается при окончании курса и после выполнения команды /support.
Метод - заглушка. На вход приходят телеграмовский идентификатор пользователя и user_data 