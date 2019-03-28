from models.MusicComposition import MusicComposition
from models.MusicType import MusicType
from models.Genre import Genre

class PopMusic(MusicComposition):

    def __init__(self,
                 name = None,
                 price = 0,
                 music_type = None,
                 length = None,
                 release_year = 0,
                 performer = None,
                 author = None):
        super().__init__(name, price, music_type,
                         length, release_year, Genre.POP, performer)
        self.author = author
