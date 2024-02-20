from Classes.ClassIMDB import *

url = "https://www.imdb.com/title/tt1232829/"
# url = "https://www.imdb.com/title/tt14965934"

# film_imdb = ClassIMDB.get_all_infos_from_url(url)

# open_in_browser(url)

# print(get_root_path() + "temp_imdb_film_page.html")

film_imdb = ClassIMDB.get_data_from_html_file(get_root_path() + "imdb.html")

if film_imdb.eng_title:
    Print.print_white("Eng title : " + film_imdb.eng_title)
else:
    Print.print_red("Eng title : " + "None")

if film_imdb.score:
    Print.print_white("Score : " + film_imdb.score)
else:
    Print.print_red("Score : " + "None")

if film_imdb.release:
    Print.print_white("Release : " + film_imdb.release)
else:
    Print.print_red("Release : " + "None")

if film_imdb.director:
    Print.print_white("Director : " + film_imdb.director)
else:
    Print.print_red("Director : " + "None")

if film_imdb.actors:
    Print.print_white("Cast : " + (" , ").join(film_imdb.actors))
else:
    Print.print_red("Cast : " + "None")

if film_imdb.eng_genre:
    Print.print_white("Eng Genre : " + (" , ").join(film_imdb.eng_genre))
else:
    Print.print_red("Eng Genre : " + "None")

if film_imdb.eng_info:
    Print.print_white("Eng Info : " + film_imdb.eng_info)
else:
    Print.print_red("Eng Info : " + "None")

if film_imdb.country:
    Print.print_white("Country : " + (" , ").join(film_imdb.country))
else:
    Print.print_red("Country : " + "None")

if film_imdb.parent_guide:
    Print.print_white("Parent Guide : " + film_imdb.parent_guide)
else:
    Print.print_red("Parent Guide : " + "None")

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
