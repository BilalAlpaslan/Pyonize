

__all__ = "Pyon", "pyonize"

class Pyon():
    
    def __init__(self, data:dict):
        self.convert_to_obj(data)


    def convert_to_obj(self, data:dict):
        self.creation_string_data = str(data)
        # print(self.__annotations__)
        for i,j in data.items():
            if isinstance(j,dict):
                new_pyon = pyonize(j)
                object.__setattr__(self,i,new_pyon)

            else:
                object.__setattr__(self,i,j)
        
    def __str__(self) -> str:
        return self.creation_string_data



def pyonize(data:dict) -> Pyon:
    if not isinstance(data,dict):
        raise Warning(f"only dict object is pyonizeable :{data}")
    return Pyon(data)
