from Data.Film import Film
from Classes.ClassUtility import *
from Classes.Class30nama import *


class ClassCategorize:
    location = None
    folder_name = None
    name_without_date = None
    release_date = None

    def __init__(self, name, location):

        self.location = rename_file_paths_by_os(location)

        self.folder_name = name

        json_file = rename_file_paths_by_os(location + name) + CustomNames.EXTRACTED_DATA

        if os.path.exists(json_file):

            film = Class30nama.get_data_from_json_file(json_file)

            if film:
                genre = film.per_genre

                if genre:
                    Print.print_green(str(name))
                    Print.print_yellow(" , ".join(genre))
                    found_correct_folder = self.categorize(genre)
                    if found_correct_folder:
                        Print.print_cyan(found_correct_folder)
                    Print.print_full_line(CustomColor.WHITE)

    def categorize(self, genre):
        # genre = str(genre).split(sep=",")

        found = None

        multi_dict = {
            "Comedy-Romance": "کمدی عاشقانه",
            "Comedy-Romance2": "عاشقانه کمدی",
            "Sci-Fi-Action": "اکشن علمی-تخیلی",
            "Sci-Fi-Action2": "علمی-تخیلی اکشن"
        }

        second_dict = {
            "Western": "وسترن",
            "War": "جنگی",
            "Superhero": "ابر قهرمانی",
            "Biography": "زندگینامه",
            "Sport": "ورزشی",
            "Horror": "ترسناک",
            "History": "تاریخی",
            "War": "دفاع مقدس"
        }

        third_dict = {
            "Sci-Fi": "علمی-تخیلی",
            "Mystery": "معمایی",
            "Fantasy": "فانتزی",
            "Romance": "عاشقانه",
            "Family": "خانوادگی",
            "Comedy": "کمدی",
            "Action": "اکشن",
            "Crime": "جنایی",
            "Adventure": "ماجراجویی",
            "Thriller": "هیجان انگیز",
            "Drama": "درام"
        }

        if len(genre) > 1:
            if genre[0] == "اکشن" and genre[1] == "کمدی":
                found = "Action"
            elif genre[0] == "کمدی" and genre[1] == "اکشن":
                found = "Comedy-Action"
            elif genre[0] == "درام" and genre[1] == "عاشقانه":
                found = "Romance"
            elif genre[0] == "عاشقانه" and genre[1] == "درام":
                found = "Romance"
            elif genre[0] == "اکشن" and genre[1] == "علمی-تخیلی":
                found = "Sci-Fi-Action"
            elif genre[0] == "اکشن" and genre[1] == "جنگی":
                found = "War"

            if len(genre)>2:
                if genre[0] == "اکشن" and genre[1] == "تاریخی" and genre[2]=="جنگی":
                    found = "War"


        if not found:
            for idx, item in multi_dict.items():
                condition = False
                for x in genre:
                    if x.find(item.strip()) != -1:
                        condition = True

                if condition:
                    found = idx
                    break

        if not found:
            for idx, item in second_dict.items():
                condition = False
                for x in genre:
                    if x.find(item.strip()) != -1:
                        condition = True

                if condition:
                    found = idx
                    break

        if not found:
            for idx, item in third_dict.items():
                condition = False
                for x in genre:
                    if x.strip().find(item.strip()) != -1:
                        condition = True

                if condition:
                    found = idx
                    break

        found = str(found).replace("2", "")

        found = "0-" + found

        if found:
            old_dest = self.location + self.folder_name
            new_dest = rename_file_paths_by_os(self.location + found)
            move_or_rename_files(old_dest, new_dest, self.folder_name)

        return found
