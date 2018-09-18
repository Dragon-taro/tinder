# Tinder いいね自動化

## 使い方

[pynder を install](https://github.com/charliewolf/pynder)

[このサイト](https://gist.github.com/taseppa/66fc7239c66ef285ecb28b400b556938)のやり方に沿って facebook の access_token を取得

適当に facebook の id を取得（ググれば出てくる）

そいつらを`variable.py`にぶち込む（git 管理から外してる）

```python:variable.py
LAT = [緯度]
LON = [経度]
facebook_id = [your id] // int
facebook_auth_token = "your token" // string
```

あとは適当に実行したら ok

無限ループするから 100 人で切ってます w
