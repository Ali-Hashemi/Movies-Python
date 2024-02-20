from Classes.ClassDoostiha import *

url = "https://www.imdb.com/title/tt1232829/"
# url = "https://www.imdb.com/title/tt14965934"

# film_imdb = ClassIMDB.get_all_infos_from_url(url)

# open_in_browser(url)

# print(get_root_path() + "temp_imdb_film_page.html")

film_imdb = ClassDoostiha.get_data_from_html_file(get_root_path() + "doostiha.html")

if film_imdb.release:
    Print.print_white("Release Date : " + film_imdb.release)
else:
    Print.print_red("Release Date :" + "None")

if film_imdb.director:
    Print.print_white("Director : " + film_imdb.director)
else:
    Print.print_red("Director : " + "None")

if film_imdb.actors:
    Print.print_white("Cast : " + (" , ").join(film_imdb.actors))
else:
    Print.print_red("Cast : " + "None")

if film_imdb.per_info:
    Print.print_white("Per Info : " + film_imdb.per_info)
else:
    Print.print_red("Per Info :" + "None")

Print.print_white("")
os.system("pause")

# film_30nama = Class30nama.get_data_from_html_file("D:/After Earth (2013)/30nama.html")
#
# if not Class30nama.check_film_for_empty_fields(film_30nama):
#    Print.print_white("Per title : " + film_30nama.per_title)
#    Print.print_white("Per genre : " + " , ".join(film_30nama.per_genre))
#    Print.print_white("Per info : " + film_30nama.per_info)
#    Print.print_white("Imdb Url : " + film_30nama.url_imdb)
#    Print.print_white("30nama Url : " + film_30nama.url_30nama)
