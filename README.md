# urlrap
URL Utility Functinos
#### features

- Parse into fun parts
- Normalize
- Extract Date!

#### examples
```py
from urlrap import urlrap
```
###### parse url
```py
urlrap.path('http://peterdowns.com/posts/first-time-with-pypi.html')

Out[1]: '/posts/first-time-with-pypi.html'
```
###### normalize url
```py
urlrap.normalize('http://www.huffingtonpost.com/oula-a-alrifai-/syrian-refugee-aleppo-education_b_9842414.html?utm_hp_ref=worldpost-global-order')

Out[2]: 'http://wwwhuffingtonpost/oula-a-alrifai-/syrian-refugee-aleppo-education_b_9842414.html'
```
###### find date
```py
urlrap.find_date('http://www.nytimes.com/2016/05/10/sports/at-16-reece-whitley-stands-tall-in-and-out-of-water.html')

Out[3]: datetime.datetime(2016, 5, 10, 0, 0)
```
