from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Classes.ClassIMDB import ClassIMDB
from Data import Film
import re
from Forms.CreateCovers.FormCreateCover import Table
from Classes.ClassUtility import Json

# def insert_or_edit_json_file(item, value, json_file_path):
#     json_data = Json.read_from_json_file(json_file_path)
#
#     found = False
#
#     for key in json_data:
#         if key == item:
#             json_data[key] = value
#             found = True
#             break
#
#     if not found:
#         json_data[item] = value
#
#     json_data = Json.sort_json(json_data)
#
#     Json.write_to_json_file(json_data, json_file_path)


# king_link = "https://king-movie.net"

# insert_or_edit_json_file("imdb_link", king_link, "zzlooo.json")

# print(platform.system())

# film = ClassIMDB().get_all_infos("https://www.imdb.com/title/tt12593682")
# Film().check_empty_values(film)

mode = 1
film_type = 0
films_array = []

all_details = []

all_details.append('D:\\(A1222) - Bullet Train (2022)\\')

film = Film()
film.actors = ['Brad Pitt', 'Joey King', 'Aaron Taylor-Johnson', 'Brian Tyree Henry', 'Andrew Koji', 'Hiroyuki Sanada']
film.country = ['Japan', 'United States']
film.director = 'David Leitch'
film.dubbed = 0
film.eng_genre = ['Action', 'Comedy', 'Thriller']
film.eng_info = 'Five assassins aboard a swiftly-moving bullet train find out that their missions have something in common'
film.eng_title = 'Bullet Train'
film.per_genre = ['اکشن']
film.per_info = 'پنج آدمکش در قطاری سریع السیر متوجه می‌شوند که در ماموریتشان نقاط مشترکی وجود دارد'
film.per_title = 'قطار سریع‌السیر'
film.release = '2022'
film.score = '7.3'
film.url_30nama = 'https://30nama.com/movie/278062/Bullet-Train-2022'
film.url_imdb = 'https://www.imdb.com/title/tt12593682'

all_details.append(film)

films_array = []
films_array.append(all_details)

# Table(mode, film_type, films_array)

# name = get_last_file_or_folder_from_path("D:\\Bullet Train (2022)\\")

# name = "(AB2008) (A1998) - Bullet Train (2022) (B2021)"
#
# regex = "[(][a-zA-Z]+\d+[)] - "
#
# j = re.findall(regex, name)
#
# print(j)

name = "Bullet Train (2022-2025)"
# name = "(AB2008) (A1998) - Bullet Train (2022) (B2021)"

# print(File.trim_released_date(name))


# imdb = ClassIMDB()

# film = imdb.get_all_infos('https://www.imdb.com/title/tt12593682')


# myFilm = Film()
#
# if Film().get_empty_values(myFilm):
#     print("myFilm has values")
# else:
#     print("myFilm is empty")

film = Film.json_file_to_class("D:\(A1222) - Bullet Train (2022)\zza.json")

# print(film.per_title)


