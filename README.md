# just_asgi

Самый маленький полнофункциональный бекенд на асинхронном Python

`make run`


```
hey -z 60s "http://0.0.0.0:8000/healthz"

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