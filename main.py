from models.ClassicalMusic import ClassicalMusic
from models.FolkMusic import FolkMusic
from models.PopMusic import PopMusic
from models.Time import Time
from models.Genre import Genre
from models.MusicType import MusicType
from managers.MusicStoreManager import MusicStoreManager

fur_elise = ClassicalMusic("Fur Elise",
                          2.5,
                          Time(3, 40),
                          1810,
                          "Beethoven")

winter = ClassicalMusic("Winter",
                        1.9,
                        Time(3, 51),
                        1723,
                        "Vivaldi")

dva_dubky = FolkMusic("Ой, на горі два дубки",
                     3.5,
                     Time(3, 10),
                     2013,
                     "Тоня Матвієнко",
                     "Україна")

dragostea_din_tei = PopMusic("Dragostea Din Tei",
                           2.7,
                           MusicType.VOCAL,
                           Time(4, 10),
                           1998,
                           "O-Zone",
                           "Dan Balan")

natural = PopMusic("Natural",
                       4.5,
                       MusicType.VOCAL,
                       Time(3, 9),
                       2018,
                       "Imagine Dragons")

music_compositions = [dva_dubky, natural, winter, fur_elise, dragostea_din_tei]
manager = MusicStoreManager(music_compositions)

print(manager.find_by_genre(Genre.CLASSICAL))
print(manager.sort_by_length(music_compositions))
print(manager.sort_by_release_year(music_compositions, True))
