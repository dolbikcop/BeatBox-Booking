# BeatBox Booking

BeatBox Booking - сервис бронирования комнат в музыкальных студиях. Предназначен
для улучшения процесса
бронирования путем понятного представления информации о студиях, решения
проблемы оформления брони напрямую у владельца
помещений.

### Разработка

#### Запуск

Убедитесь в том, что в backend есть **.env** файл с корректными переменными.
Требуемые переменные можно увидеть в файле **test.env**

```bash
docker compose --env-file ./backend/.env up
```

Frontend: http://localhost

Backend: http://localhost/api/docs

#### Работа с репозиторием

Получение изменений в подмодулях и соответствующее обновление файлов в
репозитории

Если вы работаете с этими подмодулями впервые, то к команде необходимо
добавить флаг --init

```bash
git submodule update --remote
```