class Decoder:
    def __init__(self, src=None):
        self.src = src

    def decode(self, src=None):
        if self.src is None:
            return type(None)

    def _functions_decode(self):
        # todo function decoder
        pass

    def _int_decode(self):
        # todo integer decoder
        pass

    def _str_encode(self):
        # todo string decoder
        pass

    def _list_encode(self):
        # todo list decoder
        pass

    def _dict_decode(self):
        pass

    def _tuple_decode(self):
        pass

    def _set_decode(self):
        pass

    def _instance_decode(self):
        pass
