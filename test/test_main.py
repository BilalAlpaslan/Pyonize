
from pyonize import pyonize, Pyon, PyonList


def test_pyonize():
    pyon = pyonize({"id": 1, "name": "bilal", "job": {"id": 1, "title": "CTO"}, "list": [
                   1, 2, 3], "dictlist": [{"name": "bilal1"}, {"name": "bilal2"}]})

    print(str(type(pyon)))

    assert pyon.name == "bilal"
    assert str(pyon.job) == str({"id": 1, "title": "CTO"})
    assert pyon.job.title == "CTO"


def test_pyon_class():
    pyon = Pyon({"id": 1, "name": "bilal", "job": {"id": 1, "title": "CTO"}, "list": [
                1, 2, 3], "dictlist": [{"name": "bilal1"}, {"name": "bilal2"}]})

    print(str(type(pyon)))

    assert pyon.name == "bilal"
    assert str(pyon.job) == str({"id": 1, "title": "CTO"})
    assert pyon.job.title == "CTO"
    assert str(pyon.list) == str([1, 2, 3])
    assert pyon.list[0] == 1
    assert str(pyon.dictlist) == str([{"name": "bilal1"}, {"name": "bilal2"}])
    assert str(pyon.dictlist[0]) == str({"name": "bilal1"})
    assert pyon.dictlist[0].name == "bilal1"


def test_pyon_list_class():
    pyon = PyonList([{"apple": 1}, {"banana": 5}, {"orange": 9}])

    print(str(type(pyon)))

    assert str(pyon) == str([{"apple": 1}, {"banana": 5}, {"orange": 9}])
    assert str(pyon[0]) == str({"apple": 1})
    assert pyon[0].apple == 1
