# Pyon
convert json|dict to python object


```py
from pyon import pyonize


def example():
    
    deneme = pyonize({"id":1,"name":"bilal","job":{"id":1,"title":"CTO"}})

    print(type(deneme))
    print(deneme.name)
    print(deneme.job)
    print(deneme.job.title)

example()
```


this project not available in PyPI now (coming soon). if you want add this library your workspace clone this repo and run in this folder:

```pip install .```
