from Classes.Class30nama import *

url = "https://www.imdb.com/title/tt1232829/"
# url = "https://www.imdb.com/title/tt14965934"

# film_imdb = ClassIMDB.get_all_infos_from_url(url)

# open_in_browser(url)

# print(get_root_path() + "temp_imdb_film_page.html")

film_30nama = Class30nama.get_data_from_html_file(get_root_path() + "30nama.html")

if film_30nama.per_title:
    Print.print_white("Per title : " + film_30nama.per_title)
else:
    Print.print_red("Per title : " + "None")

if film_30nama.per_genre:
    Print.print_white("Per Genre : " + (" , ").join(film_30nama.per_genre))
else:
    Print.print_red("Per Genre : " + "None")

if film_30nama.per_info:
    Print.print_white("Per Info : " + film_30nama.per_info)
else:
    Print.print_red("Per Info : " + "None")

if film_30nama.url_imdb:
    Print.print_white("IMDB URL : " + film_30nama.url_imdb)
else:
    Print.print_red("IMDB URL : " + "None")

if film_30nama.url_30nama:
    Print.print_white("30nama URL : " + film_30nama.url_30nama)
else:
    Print.print_red("30nama URL :" + " None")

Print.print_white("")
os.system("pause")
