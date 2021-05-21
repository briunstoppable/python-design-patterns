class Adapter:
    def __init__(self, object, **adapted_method):
        self._object = object
        self.__dict__.update(adapted_method)

    def __getattr__(self, attr):
        return getattr(self._object, attr)


class Chinese:
    def __init__(self):
        self.name = "Chinese"

    def thankyou(self):
        return "xie xie"


class Dari:
    def __init__(self):
        self.name = "Dari"

    def thankyou(self):
        return "tashakur"


class English:
    def __init__(self):
        self.name = "English"

    def thankyou(self):
        return "thanks"
