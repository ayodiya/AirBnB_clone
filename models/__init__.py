from models.base_model import BaseModel


class Classes(dict):
    """classes"""

    def __getitem__(self, key):
        """get item"""
        try:
            return super(Classes, self).__getitem__(key)
        except Exception as e:
            raise Exception("** class doesn't exist **")


models = [BaseModel]
classes = Classes(**{x.__name__: x for x in models})
