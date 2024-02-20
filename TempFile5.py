from Classes.ClassDoostiha import *
from Classes.ClassHex import *
from Classes.ClassIMDB import *

# url = "https://subscene.com/subtitles/shameless-us-tenth-season"
# #
# soup = Html.get_soup_for_subscene(url, timer=3)
#
# pass

# soup = Html.get_soup_from_file(get_root_path() + "\\temp_doostiha_film_info_page.html")
# film = ClassHex.get_all_infos_from_soup(soup)

# film = ClassHex.get_all_infos_from_url("https://hexdownload.co/22243/katyusha-film/")

# if ClassHex.is_film_complete(film):
#     print("OK")

# soup2 = Html.get_soup_from_file(get_root_path() + "\\temp_doostiha_film_info_page.html")
# print(ClassDoostiha.get_release_date(soup2))

# url = 'https://subscene.com/subtitles/farsi_persian-text/sVckMQ82gZArmJz2IJUWZEWbAMQ_8x0gUzTpokLQ-rZIdZypAF7tkyYo4dVcS8oUcVcaE0ZZIMU7D0jmkrmGZp2UQe-y7s-DKplRnuXncSigxgcjxxaGgUdfpXL0TcIc0'

# Html.get_soup_with_chrome_driver_undetected(url)


# soup = Html.get_soup_from_file(get_root_path() + "\\temp_imdb_film_page.html")
soup = Html.get_soup_from_file(get_root_path() + "\\temp_imdb_tv_page.html")

# film = ClassIMDB.get_all_infos_from_soup(soup)

# print(is_contain_hour_or_minute("100h"))
