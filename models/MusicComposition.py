class MusicComposition:

    def __init__(self,
                 name = None,
                 price = 0,
                 music_type = None,
                 length = None,
                 release_year = 0,
                 genre = None,
                 performer = None):
        self.name = name
        self.price = price
        self.music_type = music_type
        self.length = length
        self.release_year = release_year
        self.genre = genre
        self.performer = performer

    def __str__(self):
        return ("name = {}, price = ${}, music type = {}," +
            "length = {}, release year = {}, genre = {}," +
            "performer = {}").format(self.name, self.price,
            self.music_type, self.length, self.release_year,
            self.genre, self.performer)
