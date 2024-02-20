from pymediainfo import MediaInfo
from Forms.ExtractWebPage import *
from Base import *
from Classes.ClassIMDB import ClassIMDB

name = "6 Underground"
released_date = "2019"
FILM_TYPE_FINAL = 1
DUBBED_TYPE_FINAL = 1

cla = ClassExtract30nama()
data_30nama = cla.get_data_from_folder(name, released_date, FILM_TYPE_FINAL, DUBBED_TYPE_FINAL)

imdb = ClassIMDB()
data_imdb_from_url = imdb.get_all_infos_from_url("\\temp_imdb_tv_page.html")
data_imdb_from_url = imdb.combine_30nama_into_imdb_data(data_30nama, data_imdb_from_url)
# data_imdb_from_url = imdb.get_all_infos("https://www.imdb.com/title/tt8106534/?ref_=nv_sr_srsg_0")

dictionary = data_imdb_from_url.__dict__

for i in dictionary:
    if not dictionary[i]:
        Print.print_red(i + " not found !!!")

Json.write_to_json_file(data_imdb_from_url, "", "zza.json")
