class MusicStoreManager:

    def __init__(self, music_compositions = None):
        self.music_compositions = music_compositions

    def find_by_genre(self, genre):
        return list(filter(lambda music: music.genre == genre,
                           self.music_compositions))

    def sort_by_release_year(self, music_compositions, reverse = False):
        return sorted(music_compositions, key = lambda music:
                music.release_year, reverse = reverse)

    def sort_by_length(self, music_compositions, reverse = False):
        return sorted(music_compositions, key = lambda music:
                music.length.convert_to_seconds(),
                reverse = reverse)
