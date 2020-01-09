from .Packer import Packer as _Packer

if __name__ == "__main__":
    from pprint import pprint
import re

# proto
ATTR_MARK = b"A"
INT = b"I"
BYTE = b"B"
LONG = b"L"
STR = b"S"
LIST = b"l"
DICT = b"d"
CLASS = b"C"

''' proto
|8 bits |16 bits        |           |
|version|description_len|buffer_len |
'''


def dump(obj) -> dict:
    obj_dict = {
        "Class": obj.__class__.__name__,
    }
    if hasattr(obj, "__dict__"):
        obj_dict["Module"] = obj.__module__
        for item in vars(obj).items():
            obj_dict[item[0] + "_Attr"] = dump(item[1])
    else:
        obj_dict["value"] = obj
    return obj_dict
    pass


def load(obj_dict: dict):
    if obj_dict.get("value") is not None:
        value = obj_dict.get("value")
        return value

    module_name = obj_dict["Module"]
    class_name = obj_dict['Class']

    # import module from obj dict
    try:
        temp_module = __import__(module_name)
    # default import __main__ as the module of new class
    except ModuleNotFoundError:
        temp_module = __import__("__main__")

    try:
        temp_class: type = getattr(temp_module, class_name)
    # dynamic create a new class if cannot found from module
    except AttributeError:
        temp_class = type(class_name, (object,), {"__module__": temp_module})
        pass

    instance = temp_class()

    for item in obj_dict.items():
        pattern = "(.*?)_Attr"
        attr_value = item[1]
        if isinstance(attr_value, dict):
            attr_name = re.findall(pattern, item[0])[0]
            attr_value = load(attr_value)
            setattr(instance, attr_name, attr_value)

    # todo  create temp_class by dynamic

    return instance


def pack(obj) -> bytes:
    new_pack = _Packer(obj)
    data = new_pack.pack()
    return data


def unpack(raw_data: bytes):
    """
    :param raw_data:
    :return: python class instance
    """
    # todo load from bytes
    new_pack = _Packer(raw_data)
    instance = new_pack.unpack()
    return instance


if __name__ == "__main__":
    class TestClass:
        def __init__(self):
            self.session = 123


    class TestSubClass(TestClass):
        def __init__(self):
            super().__init__()
            self.se = 456
            self.sub = None

        def set_sub(self, sub):
            self.sub = sub


    a = TestClass()
    temp = TestSubClass()
    temp.set_sub(a)

    temp_dict = dump(temp)
    pprint(temp_dict)

    new_obj = load(temp_dict)
    pprint(dump(new_obj))
