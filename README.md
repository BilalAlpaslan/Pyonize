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


this project not available in PyPI now (coming soon). if you want add this library your workspace clone this repo and watch a this steps:

### **First**

Download wheel and setuptools libraries

`pip install wheel setuptools`

### **After** 

Make sure you are in the same folder as setup.py

`python setup.py bdist_wheel --universal`

### **Finally**

Stay in the same directory and copy the name of the .whl file in the dist folder

``pip install ./dist/copied file name`` 

Actually the filename is by default: "pyon-0.1.0-py2.py3-none-any.whl"
