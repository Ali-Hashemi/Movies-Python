from Config import *
from Classes.ClassUtility import *
from Base import *

class Rename:

    def __init__(self, original_file, location):

        filename = os.path.splitext(original_file)[0]

        file_ext = os.path.splitext(original_file)[1]

        words = [
            '.720p.HDTV.Farsi.Dubbed(Film2serial.ir)',
            '.720p.Farsi.Dubbed.(Film2serial.ir)',
            '_720p_Farsi_Dubbed_(Film2serial.ir)',
            '.720p.WEB-DL.Farsi.Dubbed(Film2serial.ir)',
            '_720p_WEB-DL_Farsi_Dubbed(Film2serial.ir)',
            '.720p.BluRay.HardSub.DigiMoviez',
            '.720p.ShAaNiG.(Film2serial.ir)',
            '_720p_ShAaNiG_(Film2serial.ir)',
            '.720p.WEB-DL.KIMO.DUBLE_2',
            '.720p.WEB-DL.KIMO.DUBLE',
            '.720p.BluRay.KIMO.DUBLE',
            '.720p.BRRip.KIMO.DUBLE',
            '.720p.WEB-DL.Farsi.Dubbed',
            '[www.film2serial.ir]',
            '.720p.Farsi.Dubbed',
            '_720p_Farsi_Dubbed',
            ' 720p Farsi Dubbed',
            ' 720p BluRay Fa Dubbed',
            '.DVDRip.Farsi.Dubbed',
            '_DVDRip_Farsi_Dubbed',
            '.720p.KingMovi.DUBLE',
            '_720p_KingMovi_DUBLE',
            '.720p.KIMO.DUBLE',
            '_720p_KIMO_DUBLE',
            '.720p.Farsi.Dub',
            '_720p_Farsi_Dub',
            '_Subtitles01.PER',
            '_Subtitles01.ENG',
            '_Subtitles01',
            '(Per) ',
            '.720p',
            '_720p',
            '.Fixed',
            '.Dubbed',
            '_Dubbed']

        spaces = [
            '.',
            '_'
        ]

        new_name = filename

        x = re.findall("2\d{3}|19\d{2}", new_name)

        if x:
            new_name = slicer(new_name, x[0])
            new_name = new_name.replace("(", "")

            for word in words:
                if find_in_text(new_name, word):
                    new_name = new_name.replace(word, '')

            for i in spaces:
                if find_in_text(new_name, i):
                    new_name = new_name.replace(i, ' ')

            new_name = str(new_name).strip() + " (" + x[0] + ")"

        if os.path.isfile(location + original_file):
            new_file_name_with_extension = new_name + file_ext
        else:
            new_file_name_with_extension = new_name

        # if not os.path.exists(location + new_name):
        #     os.makedirs(location + new_name)

        if new_name:
            # os.rename(str(location + original_file), str(location + new_name + "\\" + new_name + file_ext))
            move_or_rename_files(location + original_file, location + new_name, new_file_name_with_extension)
            srt_file = filename + ".srt"
            if os.path.exists(location + srt_file):
                move_or_rename_files(location + srt_file, location + new_name, new_name + ".srt")
                # os.rename(str(location + srt_file), str(location + new_name + "\\" + new_name + ".srt"))
