### Setup

Pls use python 3.6.*

```bash
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

### Start server ML-model

```bash
./start.sh
```

### Send http-post request with payload

```python
import requests

response = requests.post("http://127.0.0.1:8080/predict", json={"key":"value"})
print(respopnse.json())
```

### Process
![](img/Diagram.png)
