
from pyon import pyonize, Pyon

def test_pyonize():
    pyon = pyonize({"id":1,"name":"bilal","job":{"id":1,"title":"CTO"}})

    print(str(type(pyon)))

    assert pyon.name == "bilal"
    assert str(pyon.job) == str({"id":1,"title":"CTO"})
    assert pyon.job.title == "CTO"


def test_pyon_class():
    pyon = Pyon({"id":1,"name":"bilal","job":{"id":1,"title":"CTO"}})

    print(str(type(pyon)))

    assert pyon.name == "bilal"
    assert str(pyon.job) == str({"id":1,"title":"CTO"})
    assert pyon.job.title == "CTO"