from .Reader import Reader
import requests


class HTTPReader(Reader):

    def __init__(self, src=None):
        self.src = src

    def read(self):
        return requests.get(self.src).text
