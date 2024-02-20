import subprocess

from pymediainfo import MediaInfo

from Base import *
from Classes.ClassUtility import *


class FixDubbed:
    # ------------- Absolutes --------------- #

    suffix_word_final = ".Fixed"
    TEMP_ARRAY = {
        "Video": None,
        "Per-Audio": None,
        "Eng-Audio": None,
        "Subtitle": None
    }

    root = None
    fixed_dubbed_folder = "000-Fixed-Dubbed"
    multiple_audios_folder = "Multiple-Audios"
    remux_folder = "0-Remuxed"
    remux_no_sub_folder = "0-Remuxed-No-Sub"
    sorted_out_folder = "Sorted-Out"
    final_folder = "Final"

    selected_audio = None
    selected_sub = None

    # ------------- Absolutes --------------- #

    def __init__(self, name, location, selected_audio=None, selected_sub=None):
        if selected_audio and selected_sub:
            self.selected_audio = str(selected_audio).split(",")
            self.selected_sub = str(selected_sub).split(",")

        letters = ["Seagate Backup Plus",
                   "My Book 6TB", "My Book 4TB", "Others"]
        username = str(os.getlogin())
        desktop_path_windows = rename_file_paths_by_os(
            "C:/Users/" + username + "/Desktop")
        desktop_path_linux = rename_file_paths_by_os(
            "home/" + username + "/Desktop")

        if str(location).lower().find("desktop") != -1:
            self.root = rename_file_paths_by_os(
                str(location[:location.find(":")]) + ":/Users/" + username + "/Desktop")
        else:
            self.root = rename_file_paths_by_os(
                str(location[:location.find(":")]) + ":")

        for i in letters:
            if find_in_text(location, i):
                text = rename_file_paths_by_os(
                    str(location[:location.find(str(i))]))
                self.root = rename_file_paths_by_os(text + i)

        self.root = rename_file_paths_by_os(
            self.root + self.fixed_dubbed_folder)

        # Desktop
        # if is_os_linux():
        #     self.root = rename_file_paths_by_os(
        #         desktop_path_linux + self.fixed_dubbed_folder)
        # else:
        #     self.root = rename_file_paths_by_os(
        #         desktop_path_windows + self.fixed_dubbed_folder)

        self.multiple_audios_folder = rename_file_paths_by_os(
            self.root + self.multiple_audios_folder)
        self.remux_folder = rename_file_paths_by_os(
            self.root + self.remux_folder)
        self.remux_no_sub_folder = rename_file_paths_by_os(
            self.root + self.remux_no_sub_folder)
        self.sorted_out_folder = rename_file_paths_by_os(
            self.root + self.sorted_out_folder)
        self.final_folder = rename_file_paths_by_os(
            self.root + self.final_folder)

        self.name = name
        self.location = location
        self.full_path = location + name

        if self.root:
            if not os.path.exists(self.root):
                os.makedirs(self.root)

            self.fix_films()

            self.set_properties()

            self.set_properties_without_sub()

            self.check_empty_folders()

            self.rename_fixed_movies()

            Print.print_full_line()

    @staticmethod
    def count_audios(media, number_of_audios):
        counter = 0
        for _ in media.audio_tracks:
            counter += 1
        if counter == number_of_audios:
            return bool(1)

    @staticmethod
    def count_subs(media, number_of_subs):
        counter = 0
        for _ in media.text_tracks:
            counter += 1
        if counter == number_of_subs:
            return bool(1)

    @staticmethod
    def find_eng_audio_id(media_info: MediaInfo, selected_per_audio):
        found_id = None

        if selected_per_audio:
            selected_per_id = int(selected_per_audio[0])

            for index, value in enumerate(media_info.audio_tracks):
                id = int(strip_text(
                    int(media_info.audio_tracks[index].track_id) - 1))
                lang = media_info.audio_tracks[index].language

                if id != selected_per_id:
                    if lang and lang != "fa":
                        found_id = id

            if not found_id:
                for index, value in enumerate(media_info.audio_tracks):
                    id = int(strip_text(
                        int(media_info.audio_tracks[index].track_id) - 1))
                    lang = media_info.audio_tracks[index].language

                    if id != selected_per_id:
                        if not lang:
                            found_id = id

        return found_id

    def set_properties(self):
        if os.path.exists(self.remux_folder):
            for name in os.listdir(self.remux_folder):
                if not os.path.isdir(self.remux_folder + name):
                    if name.lower().endswith(".mkv"):
                        Print.print_full_line()
                        Print.print_white(name)

                        filename_without_extension = File.get_file_name(name)
                        file_path = self.remux_folder + name

                        if filename_without_extension.find(self.suffix_word_final) != -1:
                            title = filename_without_extension.replace(
                                self.suffix_word_final, "")
                        else:
                            title = filename_without_extension

                        set_title_cmd = 'mkvpropedit -v ''"' + \
                            file_path + '"'' --set title=''"' + title + '"'
                        subprocess.call(set_title_cmd, shell=True)

                        set_property_cmd = 'mkvpropedit -v ' '"' + file_path + '" ' \
                                                                               '--edit track:1 --set name="" ' \
                                                                               '--edit track:2 --set name=Persian --set language=per --set flag-forced=1 --set flag-default=1 ' \
                                                                               '--edit track:3 --set name=English --set language=und --set flag-forced=0 --set flag-default=0 ' \
                                                                               '--edit track:4 --set language=per --set name="Eng Parts" --set flag-forced=0 --set flag-default=0'
                        subprocess.call(set_property_cmd, shell=True)

                        move_or_rename_files(
                            file_path, self.final_folder, name)

    def set_properties_without_sub(self):
        if os.path.exists(self.remux_no_sub_folder):
            for name in os.listdir(self.remux_no_sub_folder):
                if not os.path.isdir(self.remux_no_sub_folder + name):
                    if name.lower().endswith(".mkv"):
                        Print.print_full_line()
                        Print.print_white(name)

                        filename_without_extension = File.get_file_name(name)
                        file_path = self.remux_no_sub_folder + name

                        if filename_without_extension.find(self.suffix_word_final) != -1:
                            title = filename_without_extension.replace(
                                self.suffix_word_final, "")
                        else:
                            title = filename_without_extension

                        set_title_cmd = 'mkvpropedit -v ''"' + \
                            file_path + '"'' --set title=''"' + title + '"'
                        subprocess.call(set_title_cmd, shell=True)

                        set_property_cmd = 'mkvpropedit -v ' '"' + file_path + '" ' \
                                                                               '--edit track:1 --set name="" ' \
                                                                               '--edit track:2 --set name=Persian --set language=per --set flag-forced=1 --set flag-default=1 ' \
                                                                               '--edit track:3  --set name=English --set language=und --set flag-forced=0 --set flag-default=0'
                        subprocess.call(set_property_cmd, shell=True)

                        move_or_rename_files(
                            file_path, self.final_folder, name)

    def sort_media(self):
        Print.print_full_line()
        Print.print_white(self.name)

        compare_array = []
        perfect_array = [0, 1, 2, 3]

        for i in self.TEMP_ARRAY:
            compare_array.append(self.TEMP_ARRAY[i])

        if compare_array == perfect_array:
            move_or_rename_files(self.full_path, self.remux_folder, self.name)

        elif compare_array == [0, 1, 2, None]:
            move_or_rename_files(
                self.full_path, self.remux_no_sub_folder, self.name)

        elif self.TEMP_ARRAY["Subtitle"] is None:
            cmd = 'mkvmerge -o "' + self.remux_no_sub_folder + self.name + '" "' + self.full_path + \
                  '"' + " --track-order 0:" + str(self.TEMP_ARRAY["Video"]) + ",0:" + \
                  str(self.TEMP_ARRAY["Per-Audio"]) + \
                ",0:" + str(self.TEMP_ARRAY["Eng-Audio"])

            subprocess.call(cmd, shell=True)

        else:
            # cmd = 'mkvmerge -o "' + self.remux_folder + self.name + '" "' + \
            #       self.full_path + '"' + " --track-order 0:" + str(self.TEMP_ARRAY["Video"]) + \
            #       ",0:" + str(self.TEMP_ARRAY["Per-Audio"]) + ",0:" + str(self.TEMP_ARRAY["Eng-Audio"]) + \
            #       ",0:" + str(self.TEMP_ARRAY["Subtitle"])

            cmd = 'mkvmerge --output "' + self.remux_folder + self.name + '"' + \
                  " --audio-tracks " + str(self.TEMP_ARRAY["Per-Audio"]) + \
                  "," + str(self.TEMP_ARRAY["Eng-Audio"]) + " --subtitle-tracks " + \
                  str(self.TEMP_ARRAY["Subtitle"]) + ' "' + self.full_path + '"' + \
                  " --track-order 0:" + str(self.TEMP_ARRAY["Video"]) + \
                  ",0:" + str(self.TEMP_ARRAY["Per-Audio"]) + ",0:" + str(self.TEMP_ARRAY["Eng-Audio"]) + \
                  ",0:" + str(self.TEMP_ARRAY["Subtitle"])

            subprocess.call(cmd, shell=True)

        if os.path.exists(self.remux_folder):
            if os.path.exists(self.remux_folder + self.name):
                if os.path.exists(self.full_path):
                    move_or_rename_files(
                        self.full_path, self.sorted_out_folder, self.name)
        if os.path.exists(self.remux_no_sub_folder):
            if os.path.exists(self.remux_no_sub_folder + self.name):
                if os.path.exists(self.full_path):
                    move_or_rename_files(
                        self.full_path, self.sorted_out_folder, self.name)

    def check_empty_folders(self):
        delete_empty_folder(
            self.remux_folder, self.remux_no_sub_folder, self.multiple_audios_folder)

    def rename_fixed_movies(self):
        if os.path.exists(self.final_folder):
            for name in os.listdir(self.final_folder):
                if not os.path.isdir(self.final_folder + name):
                    if name.lower().endswith(".mkv"):
                        if not name.find(self.suffix_word_final) != -1:
                            new_name = File.get_file_name(
                                name) + self.suffix_word_final + ".mkv"
                            move_or_rename_files(self.final_folder + name, self.final_folder,
                                                 new_name)


    def fix_films(self):
        if self.full_path.lower().endswith(".mkv"):
            media_info = MediaInfo.parse(self.full_path)

            if self.selected_audio and self.selected_sub:
                found_eng_audio_id = self.find_eng_audio_id(
                    media_info, self.selected_audio)

                found_per_audio_id = strip_text(self.selected_audio[0])

                found_sub_id = strip_text(self.selected_sub[0])

                if found_eng_audio_id or found_eng_audio_id == 0 and (found_per_audio_id or found_per_audio_id == 0):
                    self.TEMP_ARRAY["Video"] = media_info.video_tracks[0].track_id - 1
                    # self.TEMP_ARRAY["Per-Audio"] = media_info.audio_tracks[per_track_id].track_id - 1
                    self.TEMP_ARRAY["Per-Audio"] = int(found_per_audio_id)
                    self.TEMP_ARRAY["Eng-Audio"] = int(found_eng_audio_id)
                    # self.TEMP_ARRAY["Subtitle"] = media_info.text_tracks[sub_track_id].track_id - 1
                    self.TEMP_ARRAY["Subtitle"] = int(found_sub_id)

                    self.sort_media()

            else:
                if self.count_audios(media_info, 2):
                    self.TEMP_ARRAY["Video"] = media_info.video_tracks[0].track_id - 1

                    if media_info.audio_tracks[0].language == "fa":
                        self.TEMP_ARRAY["Per-Audio"] = media_info.audio_tracks[0].track_id - 1
                        self.TEMP_ARRAY["Eng-Audio"] = media_info.audio_tracks[1].track_id - 1
                    elif media_info.audio_tracks[1].language == "fa":
                        self.TEMP_ARRAY["Per-Audio"] = media_info.audio_tracks[1].track_id - 1
                        self.TEMP_ARRAY["Eng-Audio"] = media_info.audio_tracks[0].track_id - 1

                    if self.count_subs(media_info, 1):
                        self.TEMP_ARRAY["Subtitle"] = media_info.text_tracks[0].track_id - 1

                    self.sort_media()
                else:
                    move_or_rename_files(
                        self.full_path, self.multiple_audios_folder, self.name)

        self.TEMP_ARRAY = self.TEMP_ARRAY.fromkeys(self.TEMP_ARRAY)
