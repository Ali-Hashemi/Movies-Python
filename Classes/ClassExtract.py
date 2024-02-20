from Classes.ClassIMDB import *
from Classes.Class30nama import *
from Classes.ClassDoostiha import *
from Classes.ClassHex import *


class ClassExtract:

    @staticmethod
    def extract(item, site_type):
        json_file_path = rename_file_paths_by_os(item) + CustomNames.EXTRACTED_DATA

        html_30nama = rename_file_paths_by_os(item) + CustomNames.HTML_30nama_FILE_NAME
        html_imdb = rename_file_paths_by_os(item) + CustomNames.HTML_IMDB_FILE_NAME

        Print.print_green(get_last_file_or_folder_from_path(item))

        if site_type == 0:
            film_30nama = Film()
            film_imdb = Film()

            if os.path.exists(json_file_path):
                film_30nama = Class30nama.get_data_from_json_file(json_file_path)
                film_imdb = ClassIMDB.get_data_from_json_file(json_file_path)

                if not Class30nama.is_film_complete(film_30nama):
                    film_30nama = Class30nama.get_data_from_html_file(html_30nama)

                if not ClassIMDB.is_film_complete(film_imdb):
                    if os.path.exists(html_imdb):
                        film_imdb = ClassIMDB.get_data_from_html_file(html_imdb)

                    else:
                        if film_30nama.url_imdb:
                            Print.print_white(film_30nama.url_imdb)
                            film_imdb = ClassIMDB.get_all_infos_from_url(film_30nama.url_imdb,
                                                                         folder_path=item)

            else:
                film_30nama = Class30nama.get_data_from_html_file(html_30nama)

                if os.path.exists(html_imdb):
                    film_imdb = ClassIMDB.get_data_from_html_file(html_imdb)

                else:
                    if film_30nama.url_imdb:
                        Print.print_white(film_30nama.url_imdb)
                        film_imdb = ClassIMDB.get_all_infos_from_url(film_30nama.url_imdb,
                                                                     folder_path=item)

            if Class30nama.is_film_complete(
                    film_30nama) and ClassIMDB.is_film_complete(film_imdb):
                film = ClassIMDB.combine_30nama_into_imdb_data(film_30nama, film_imdb)

                ClassExtract.save_to_json(film, 1, json_file_path)

            else:
                Print.print_red("incomplete !!!")

        elif site_type == 1:
            film_30nama = Film()

            if os.path.exists(json_file_path):
                film_30nama = Class30nama.get_data_from_json_file(json_file_path)

                if not Class30nama.is_film_complete(film_30nama):
                    film_30nama = Class30nama.get_data_from_html_file(html_30nama)
            else:
                film_30nama = Class30nama.get_data_from_html_file(html_30nama)

            if Class30nama.is_film_complete(film_30nama):
                ClassExtract.save_to_json(film_30nama, 1, json_file_path)

            else:
                Print.print_red("incomplete !!!")

        elif site_type == 2:
            film_imdb = Film()

            if os.path.exists(json_file_path):
                film_30nama = Class30nama.get_data_from_json_file(json_file_path)
                film_imdb = ClassIMDB.get_data_from_json_file(json_file_path)

                if not ClassIMDB.is_film_complete(film_imdb):
                    if os.path.exists(html_imdb):
                        film_imdb = ClassIMDB.get_data_from_html_file(html_imdb)

                    else:
                        if film_30nama.url_imdb:
                            Print.print_white(film_30nama.url_imdb)
                            film_imdb = ClassIMDB.get_all_infos_from_url(film_30nama.url_imdb,
                                                                         folder_path=item)

            else:
                film_30nama = Class30nama.get_data_from_html_file(html_30nama)

                if os.path.exists(html_imdb):
                    film_imdb = ClassIMDB.get_data_from_html_file(html_imdb)

                else:
                    if film_30nama.url_imdb:
                        Print.print_white(film_30nama.url_imdb)
                        film_imdb = ClassIMDB.get_all_infos_from_url(film_30nama.url_imdb,
                                                                     folder_path=item)

            if ClassIMDB.is_film_complete(film_imdb):
                ClassExtract.save_to_json(film_imdb, 1, json_file_path)

            else:
                Print.print_red("incomplete !!!")

        elif site_type == 3:
            html_hex = rename_file_paths_by_os(item) + CustomNames.HTML_Hex_FILE_NAME

            if os.path.exists(json_file_path):
                film_json = ClassHex.get_data_from_json_file(json_file_path)

                if ClassHex.is_film_complete(film_json):
                    ClassExtract.save_to_json(film_json, 1, json_file_path)
                else:
                    film_hex = ClassHex.get_data_from_html_file(html_hex)

                    film_all = ClassExtract.concatenate_irani_films(film_json, film_hex)

                    if film_all:
                        if ClassHex.is_film_complete(film_all):
                            ClassExtract.save_to_json(film_all, 1, json_file_path)
            else:
                film_hex = ClassHex.get_data_from_html_file(html_hex)

                if film_hex:
                    if ClassHex.is_film_complete(film_hex):
                        ClassExtract.save_to_json(film_hex, 1, json_file_path)
                    else:
                        Print.print_red("incomplete !!!")

        elif site_type == 4:
            html_doostiha = rename_file_paths_by_os(item) + CustomNames.HTML_DOOSTIHA_FILE_NAME

            if os.path.exists(json_file_path):
                film_json = ClassDoostiha.get_data_from_json_file(json_file_path)

                if ClassDoostiha.is_film_complete(film_json):
                    ClassExtract.save_to_json(film_json, 1, json_file_path)
                else:
                    film_doostiha = ClassDoostiha.get_data_from_html_file(html_doostiha)

                    film_all = ClassExtract.concatenate_irani_films(film_json, film_doostiha)

                    if film_all:
                        if ClassDoostiha.is_film_complete(film_all):
                            ClassExtract.save_to_json(film_all, 1, json_file_path)
            else:
                film_doostiha = ClassDoostiha.get_data_from_html_file(html_doostiha)

                if film_doostiha:
                    if ClassDoostiha.is_film_complete(film_doostiha):
                        ClassExtract.save_to_json(film_doostiha, 1, json_file_path)
                    else:
                        Print.print_red("incomplete !!!")

        Print.print_full_line(CustomColor.WHITE)

    @staticmethod
    def concatenate_irani_films(film_json, film_irani):
        film = Film()
        if film_json and film_irani:
            film.per_title = film_json.per_title
            film.eng_title = film_json.eng_title
            film.release = film_json.release

            film.director = film_irani.director
            film.actors = film_irani.actors
            film.per_genre = film_irani.per_genre
            film.per_info = film_irani.per_info

        return film

    @staticmethod
    def save_to_json(film: Film, check_dubbed_status, json_file_path):
        if check_dubbed_status:
            film.dubbed = 1

        Json.write_to_json_file(film, json_file_path)
