from .Packer import Packer


def dump(obj) -> dict:
    # todo dump to dict
    pass


def pack(obj) -> bytes:
    # todo pack from object
    pass


def load_json(obj_dict: dict):
    module_name = obj_dict['module_name']
    class_name = obj_dict['classname']
    temp_module = __import__(module_name)
    temp_class: type = getattr(temp_module, class_name)

    # todo  create temp_class by dynamic

    instance = temp_class()
    return temp_class


def load(raw_data: bytes):
    # todo
    pass
