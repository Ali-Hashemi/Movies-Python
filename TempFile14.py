import re
from PIL import Image

from Classes.ClassUtility import rename_file_paths_by_os, File, get_last_file_or_folder_from_path
from Config import CustomNames
from Data import Film

import pyperclip

path = rename_file_paths_by_os("D:\Python Projects\Movies-Python\Temp\(0)-Previously\(DA1000) - 2 Guns (2013)")

json_path = rename_file_paths_by_os(
    "D:\Python Projects\Movies-Python\Temp\(0)-Previously\(DA1000) - 2 Guns (2013)") + CustomNames.EXTRACTED_DATA

film = Film.json_file_to_class(json_path)

temp_actors = []
temp_genre = []

for idx, item in enumerate(film.actors):
    if idx >= 3:
        break
    item = re.sub("\s+", "_", item.strip())
    temp_actors.append("#" + item)

for idx, item in enumerate(film.per_genre):
    if idx >= 5:
        break
    item = re.sub("\s+", "_", item.strip())
    temp_genre.append("#" + item)

poster_code = (File.trim_poster_code(get_last_file_or_folder_from_path(path)))

film.per_title = "«" + film.per_title + "»"
film.eng_title = film.eng_title + " #" + film.release + ""
film.actors = temp_actors
film.per_genre = temp_genre
film.director = "#" + re.sub("\s+", "_", film.director.strip())
film.country = "#" + re.sub("\s+", "_", film.country[0].strip())
film.score = film.score + "/10"

is_dubbed = ""

if film.dubbed:
    is_dubbed = "#دوبله_بدون_سانسور"
else:
    is_dubbed = "#زیرنویس_فارسی_چسبیده"

film_khareji_array = {
    "🏅 کد": poster_code,
    "📺 #فیلم_خارجی": film.per_title,
    "💬": is_dubbed,
    "🎬": film.eng_title,
    "🏆 امتیاز": film.score,
    "👔 کارگردان": film.director,
    "💎 ستارگان": " , ".join(film.actors),
    "🎭 ژانر": " , ".join(film.per_genre),
    "کشور": film.country,
    "🗯 خلاصه داستان": film.per_info,
}

full_text = ""

for i in film_khareji_array:
    full_text += i + " : " + film_khareji_array[i] + "\n"

# print(full_text)

pyperclip.copy(full_text)

image_path = path + 'Folder.jpg'
image = Image.open(image_path)

pyperclip.copy(image)

spam = pyperclip.paste()
