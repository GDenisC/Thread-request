# Thread-request
addes function ThreadRequest(url, callback) to python

-----------------

# Example
```python
import requests
from threq import *

def callback(res: requests.Response):
    json: dict[str, str] = res.json()

    if json.get('error'):
        raise Exception('Wrong request')

    print(json)

ThreadRequest('http://localhost:8080/?string=request', callback, method=MethodType.GET)
print('sended')
```

Response:
```
sended
{'encoded': 'cmVxdWVzdA==', 'decoded': 'request', 'sha1': '122f6d219a5cbc201624b1287641220a7cc0e507'}
```
