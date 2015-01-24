"""
Set of unit tests for Phantomas class
"""
import unittest

from ..client import Phantomas


class PhantomasTestClass(unittest.TestCase):
    """  Unit tests for Phantomas class """
    URL = 'http://foo.bar.net/'

    def test_repr(self):
        """ Test __repr__ helper """
        instance = Phantomas(url=self.URL)

        assert str(instance) == '<Phantomas for {url}>'.format(url=self.URL)

    def test_options_passing(self):
        """ Test constructor options passing """
        instance = Phantomas(url=self.URL)

        assert instance._url == self.URL
        assert instance._options == {
            'reporter': 'json',
            'url': self.URL
        }

    def test_custom_options_passing(self):
        """ Test constructor custom options passing """

        # reporter will be forced to 'json'
        instance = Phantomas(
            url=self.URL, foo=123, bar_test='test', reporter='custom')

        assert instance._url == self.URL
        assert instance._options == {
            'reporter': 'json',
            'url': self.URL,
            'bar_test': 'test',
            'foo': 123
        }
