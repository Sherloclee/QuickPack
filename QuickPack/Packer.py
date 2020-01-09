from .decoder import *
from .encoder import *


class Packer(object):
    def __init__(self, obj=None):
        self.src = obj

    def __dump(self, obj):
        pass

    def __load(self, data):
        pass

    def pack(self):
        if self.src is None:
            return None

    def unpack(self):
        pass
