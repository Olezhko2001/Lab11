from models.MusicComposition import MusicComposition
from models.MusicType import MusicType
from models.Genre import Genre

class ClassicalMusic(MusicComposition):

    def __init__(self,
                 name = None,
                 price = 0,
                 length = None,
                 release_year = 0,
                 performer = None,
                 composer = None):
        super().__init__(name, price, MusicType.INSTRUMENTAL,
                         length, release_year, Genre.CLASSICAL, performer)
        self.composer = composer

    def __str__(self):
        return super().__str__() + ", composer = {}".format(self.composer)
