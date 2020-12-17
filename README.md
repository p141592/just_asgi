# just_asgi (8508 RPS)

Самый маленький полнофункциональный бекенд на асинхронном Python

### Тестирование нагрузки

Тестировал с помощью [hey](https://github.com/rakyll/hey) (HTTP load generator)

P.S. **8508 RPS** - это очень быстро для Python
```
--- Projects/just_asgi ‹master› » hey -z 60s "http://0.0.0.0:8000/healthz"

Summary:
  Total:	60.0056 secs
  Slowest:	0.1051 secs
  Fastest:	0.0003 secs
  Average:	0.0059 secs
  Requests/sec:	8508.4080


Response time histogram:
  0.000 [1]	|
  0.011 [502754]	|■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
  0.021 [6901]	|■
  0.032 [395]	|
  0.042 [209]	|
  0.053 [101]	|
  0.063 [137]	|
  0.074 [4]	|
  0.084 [12]	|
  0.095 [20]	|
  0.105 [18]	|


Latency distribution:
  10% in 0.0049 secs
  25% in 0.0051 secs
  50% in 0.0055 secs
  75% in 0.0061 secs
  90% in 0.0069 secs
  95% in 0.0079 secs
  99% in 0.0115 secs

Details (average, fastest, slowest):
  DNS+dialup:	0.0000 secs, 0.0003 secs, 0.1051 secs
  DNS-lookup:	0.0000 secs, 0.0000 secs, 0.0000 secs
  req write:	0.0000 secs, 0.0000 secs, 0.0314 secs
  resp wait:	0.0058 secs, 0.0003 secs, 0.1051 secs
  resp read:	0.0000 secs, 0.0000 secs, 0.0317 secs

Status code distribution:
  [200]	510552 responses
```

**Запуск локально:**
1. Установить библиотеки: `poetry install`
2. В папке src выполнить `python app.py`

**Запуск в PyCharm**
![](docs/pycharm.png)

**Запуск на стенде:** `make run`


### TODO:
```
Запускать можно и так, но с этими инструментами будет прям конфетка
```
- [ ] Логирование
- [ ] Сбор метрик для Prometheus
- [ ] Sentry
- [ ] Механика для кеширования
- [ ] Генератор OpenAPI
- [ ] Подключение OpenTrace
- [ ] HTTPException с валидным JSON ответом
- [ ] Сериализация
- [ ] Middleware
- [ ] startapp/stopapp
- [ ] asyncpg pool
- [ ] Настройки для запуска production
- [ ] cli для операций без запуска проекта
- [ ] ipython notebook общения с сервисом 
- [ ] Клиент для тестирования
- [ ] BackgroundTask

---
**Мои контакты и моей команды:**
- https://vk.com/k0d_python
- https://www.linkedin.com/in/p141592/
- https://twitter.com/p141592
- https://t.me/p141592