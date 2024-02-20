from Classes.ClassUtility import *
from Classes.Class30nama import *
from Classes.ClassIMDB import *
from Base import *


class ExtractFromHtmlFiles:
    def __init__(self, name, location):
        html_file_30nama_path = location + name

        soup = Html.get_soup_from_file(html_file_30nama_path)

        if soup:
            full_title = filter_name(Class30nama.get_full_title(soup))

            if full_title:
                Print.print_green(full_title)
                each_film_folder = rename_file_paths_by_os(location + "/" + full_title)
                # each_film_folder = rename_file_paths_by_os(location)

                new_name = full_title + ".html"

                move_or_rename_files(html_file_30nama_path, location, new_name)

                # if not os.path.exists(each_film_folder):
                #     os.makedirs(each_film_folder)
                #
                #     if film.url_30nama:
                #         copy_files_to_folder(html_file_30nama_path, each_film_folder,
                #                              CustomNames.HTML_30nama_FILE_NAME)

                # Html.html2png(html_file_30nama_path, (each_film_folder + CustomNames.SOUP_SCREENSHOT))
                # if film.url_imdb:
                #     imdb = ClassIMDB()
                #     data_imdb = imdb.get_all_infos_from_url(film.url_imdb, each_film_folder)
                #     film = imdb.combine_30nama_into_imdb_data(film, data_imdb)
                #
                #     check_empty_values = Film().get_empty_values(film)
                #     if check_empty_values:
                #         Print.print_cyan("Empty Attributes :")
                #         for x in check_empty_values:
                #             Print.print_red(x + " not found !!!")
                #
                #     if not imdb.check_film_for_empty_fields(data_imdb):
                #         Json.write_to_json_file(film, each_film_folder + CustomNames.EXTRACTED_DATA)
                #         Print.print_full_line(CustomColor.CYAN)

            #     if os.path.exists(each_film_folder + CustomNames.HTML_30nama_FILE_NAME):
            #         if os.path.exists(html_file_30nama_path):
            #             send2trash(html_file_30nama_path)
            #
            # else:
            #     if os.path.exists(each_film_folder + CustomNames.HTML_30nama_FILE_NAME):
            #         if os.path.exists(html_file_30nama_path):
            #             send2trash(html_file_30nama_path)
