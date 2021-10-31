

__all__ = "Pyon", "pyonize"


from typing import Union


class Pyon:
    def __init__(self, data: dict):
        self.convert_to_obj(data)

    def convert_to_obj(self, data: dict):
        self.creation_string_data = str(data)

        for i, j in data.items():

            if not isinstance(i, str):
                raise Warning(f"ops, ı m not understand this object :{i}")

            if isinstance(j, dict):
                new_pyon = pyonize(j)
                object.__setattr__(self, i, new_pyon)
            elif isinstance(j, list):
                new_pyon_list = PyonList(j)
                object.__setattr__(self, i, new_pyon_list)
            else:
                object.__setattr__(self, i, j)

    def __str__(self) -> str:
        return self.creation_string_data


class PyonList:
    def __init__(self, data: list) -> None:
        self.convert_to_obj(data)

    def convert_to_obj(self, data: dict):
        self.creation_string_data = str(data)
        self.pyon_list = []
        for i in data:
            if isinstance(i, dict):
                self.pyon_list.append(Pyon(i))
            elif isinstance(i, list):
                self.pyon_list.append(PyonList(i))
            else:
                self.pyon_list.append(i)

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.pyon_list[index]
        raise Warning(f"only int not :{index}")

    def __str__(self) -> str:
        return self.creation_string_data


def pyonize(data: dict) -> Union[Pyon, PyonList]:
    if isinstance(data, dict):
        return Pyon(data)
    if isinstance(data, dict):
        return PyonList(data)
    raise Warning(f"only dict/list object is pyonizeable :{data}")
