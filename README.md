# Pyonize

convert json|dict to python object

## Setup

```
pip install pyonize
```

## Examples
```py
from pyonize import pyonize

deneme = pyonize({"id": 1, "name": "jhon", "job": {"id": 1, "title": "CTO"}, "list": [
                1, 2, 3], "dictlist": [{"name": "foo"}, {"name": "bar"}]})

print(deneme.name)
print(deneme.job)
print(deneme.job.title)
```

##

```py
from pyonize import Pyon

class Foo(Pyon):
    def bar(self):
        ...

data = {"id": 1, "name": "jhon", "job": {"id": 1, "title": "CTO"},
    "list": [1, 2, 3], "dictlist": [{"name": "foo"}, {"name": "bar"}]}

foo = Foo(data)

print(foo.id)
print(foo.dictlist[1].name)

```

<br>
<hr>

