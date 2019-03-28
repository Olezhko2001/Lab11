from models.MusicComposition import MusicComposition
from models.MusicType import MusicType
from models.Genre import Genre

class FolkMusic(MusicComposition):

    def __init__(self,
                 name = None,
                 price = 0,
                 length = None,
                 release_year = 0,
                 performer = None,
                 nation = None):
        super().__init__(name, price, MusicType.VOCAL,
                         length, release_year, Genre.FOLK, performer)
        self.nation = nation
