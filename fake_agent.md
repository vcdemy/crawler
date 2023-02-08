# 將爬蟲偽裝成Browser

主要是要在headers中，加入特定Browser的User Agent String。

```python
import requests

# ...

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers=headers)
```

### 參考連結：

* https://en.wikipedia.org/wiki/User_agent
* [List of User Agent Strings](http://www.useragentstring.com/pages/useragentstring.php)