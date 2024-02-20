import os
from Classes.ClassUtility import *
from pymediainfo import MediaInfo
import subprocess


class FixSubbed:
    # ------------- Absolutes --------------- #
    SUBBED_FOLDER_NAME = "000-Subbed"
    SUBBED_FOLDER_FINAL = None
    TEMP_ARRAY = {
        "Video": None,
        "Per-Audio": None,
        "Eng-Audio": None
    }

    SUB_SUFFIX_ARRAY_FINAL = ['.srt', '.ass', '.idx', '.sub']

    SUB_PREFIX_FINAL = "(Per) "
    PER_SUB_FOLDER_FINAL = "Full Subs\\"

    root = None

    # ------------- Absolutes --------------- #

    def __init__(self, file):
        self.root = rename_file_paths_by_os(str(file[:file.find(":")]) + ":")

        letters = ["Seagate Backup Plus", "My Book 6TB", "My Book 4TB", "Others"]

        # self.SUBBED_FOLDER_FINAL = rename_file_paths_by_os(self.root + self.SUBBED_FOLDER_FINAL)

        for i in letters:
            if find_in_text(file, i):
                text = rename_file_paths_by_os(str(file[:file.find(str(i))]))
                self.SUBBED_FOLDER_FINAL = rename_file_paths_by_os(
                    rename_file_paths_by_os(text + i) + self.SUBBED_FOLDER_NAME)

        username = str(os.getlogin())

        # self.SUBBED_FOLDER_FINAL = rename_file_paths_by_os(
        #     "C:/Users/" + username + "/Desktop/" + self.SUBBED_FOLDER_FINAL)

        h, t = get_path_and_file(file)

        if os.path.isdir(file):
            self.is_folder(rename_file_paths_by_os(file))

        elif os.path.isfile(file):
            self.is_movie(h, t)

    def is_folder(self, path):
        if os.path.exists(path):
            for name in os.listdir(path):
                if not os.path.isdir(path + name):
                    if str(name).lower().endswith(".mkv"):
                        # if not name.find("Trailer") != -1:
                        if not find_in_text(name, "Trailer"):
                            media_info = MediaInfo.parse(path + name)

                            if self.count_audios(media_info, 2):
                                self.TEMP_ARRAY["Video"] = media_info.video_tracks[0].track_id - 1

                                if media_info.audio_tracks[0].language == "fa":
                                    self.TEMP_ARRAY["Per-Audio"] = media_info.audio_tracks[0].track_id - 1
                                    self.TEMP_ARRAY["Eng-Audio"] = media_info.audio_tracks[1].track_id - 1
                                elif media_info.audio_tracks[1].language == "fa":
                                    self.TEMP_ARRAY["Per-Audio"] = media_info.audio_tracks[1].track_id - 1
                                    self.TEMP_ARRAY["Eng-Audio"] = media_info.audio_tracks[0].track_id - 1

                                self.sort_media(path, name, self.TEMP_ARRAY)
                                self.copy_per_sub_for_folder(path)

                        self.TEMP_ARRAY = self.TEMP_ARRAY.fromkeys(self.TEMP_ARRAY)

    def is_movie(self, path, name):
        if name.lower().endswith(".mkv"):
            if not name.lower().find("trailer") != -1:
                media_info = MediaInfo.parse(path + name)

                if self.count_audios(media_info, 2):
                    self.TEMP_ARRAY["Video"] = media_info.video_tracks[0].track_id - 1

                    if media_info.audio_tracks[0].language == "fa":
                        self.TEMP_ARRAY["Per-Audio"] = media_info.audio_tracks[0].track_id - 1
                        self.TEMP_ARRAY["Eng-Audio"] = media_info.audio_tracks[1].track_id - 1
                    elif media_info.audio_tracks[1].language == "fa":
                        self.TEMP_ARRAY["Per-Audio"] = media_info.audio_tracks[1].track_id - 1
                        self.TEMP_ARRAY["Eng-Audio"] = media_info.audio_tracks[0].track_id - 1

                    self.sort_media(path, name, self.TEMP_ARRAY)
                    self.copy_per_sub_for_movies(path, name)

            self.TEMP_ARRAY = self.TEMP_ARRAY.fromkeys(self.TEMP_ARRAY)

    def sort_media(self, path, media, temp_array):
        if not os.path.exists(self.SUBBED_FOLDER_FINAL + media):
            cmd = 'mkvmerge --audio-tracks ' + str(temp_array["Eng-Audio"]) + \
                  ' --no-subtitles -o "' + self.SUBBED_FOLDER_FINAL + media + '" "' + path + media + '"'

            subprocess.call(cmd, shell=True)

    # TODO ----------------- check if it is a utility method
    def count_audios(self, media, number_of_audios):
        counter = 0
        for _ in media.audio_tracks:
            counter += 1
        if counter == number_of_audios:
            return bool(1)

    # TODO ----------------- check if it is a utility method
    def count_videos(self, path):
        counter = 0

        if os.path.exists(path):
            for name in os.listdir(path):
                if not os.path.isdir(path + name):
                    if name.lower().endswith(".mkv"):
                        counter += 1
        return counter

    def copy_per_sub_for_folder(self, h):
        if os.path.exists(h):
            for name in os.listdir(h):
                if not os.path.isdir(h + name):
                    if name.find(self.SUB_PREFIX_FINAL) != -1:
                        sub_name = name.replace(self.SUB_PREFIX_FINAL, "")

                        if not os.path.exists(self.SUBBED_FOLDER_FINAL + sub_name):
                            copy_files_to_folder(h + name, self.SUBBED_FOLDER_FINAL, sub_name)
                            break

    def copy_per_sub_for_movies(self, h, t):
        filename_without_extension = File.get_file_name(t)

        if os.path.exists(h):
            for name in os.listdir(h):
                if not os.path.isdir(h + name):
                    if name.find(self.SUB_PREFIX_FINAL + filename_without_extension) != -1:
                        ext = os.path.splitext(name)[1]

                        final_name = filename_without_extension + ext

                        if not os.path.exists(self.SUBBED_FOLDER_FINAL + final_name):
                            copy_files_to_folder(
                                h + name, self.SUBBED_FOLDER_FINAL, final_name)

        if os.path.exists(h + self.PER_SUB_FOLDER_FINAL):
            for name in os.listdir(h + self.PER_SUB_FOLDER_FINAL):
                if not os.path.isdir(h + self.PER_SUB_FOLDER_FINAL + name):
                    if name.find(filename_without_extension) != -1:
                        ext = os.path.splitext(name)[1]

                        final_name = filename_without_extension + ext

                        if not os.path.exists(self.SUBBED_FOLDER_FINAL + final_name):
                            copy_files_to_folder(
                                h + self.PER_SUB_FOLDER_FINAL + name, self.SUBBED_FOLDER_FINAL, final_name)
