from unittest import TestCase

# Design Pattern Files
from bridge import Circle, ApiV1, ApiV2
from adapter import Chinese, Dari, English, Adapter


class TestAdapterPattern(TestCase):
    def test_chinese_thankyou(self):
        chinese = Chinese
        self.assertTrue(Adapter(chinese, speak=chinese.thankyou(self)))

    def test_dari_thankyou(self):
        dari = Dari
        self.assertTrue(Adapter(dari, speak=dari.thankyou(self)))

    def test_english_thankyou(self):
        english = English
        self.assertTrue(Adapter(english, speak=english.thankyou(self)))


class TestBridgePattern(TestCase):
    def test_v1_circle_init(self):
        self.assertTrue(Circle(1, 2, 3, ApiV1()))

    def test_v2_circle_init(self):
        self.assertTrue(Circle(1, 2, 3, ApiV2()))

    def test_v1_circle_draw(self):
        v1_circle = Circle(1, 2, 3, ApiV1())
        self.assertTrue(v1_circle.draw())

    def test_v2_circle_draw(self):
        v2_circle = Circle(1, 2, 3, ApiV2())
        self.assertTrue(v2_circle.draw())

class TestBuilderPattern(TestCase):
    def test_cheap_edu_laptop(self):
        self.assertTrue()