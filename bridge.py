class ApiV1(object):
    def draw_circle(self, x, y, radius):
        return "v1: drawing circle at {},{} - with radius = {}".format(x, y, radius)


class ApiV2(object):
    def draw_circle(self, x, y, radius):
        return "v2: drawing circle at {}.{} - with radius = {}".format(x, y, radius)


class Circle(object):
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        draw = self._drawing_api.draw_circle(self._x, self._y, self._radius)
        return draw

    def scale(self, percent):
        scale = self._radius * percent
        return scale
