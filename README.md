# Pyonize

convert json|dict to python object

## Setup

```
pip install pyonize
```

## Example
```py
from pyonize import pyonize


def example():
    
    deneme = pyonize({"id":1,"name":"bilal","job":{"id":1,"title":"CTO"}})

    print(type(deneme))
    print(deneme.name)
    print(deneme.job)
    print(deneme.job.title)

example()
```

<br>
<hr>

