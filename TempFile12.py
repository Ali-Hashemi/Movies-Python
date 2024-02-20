import os
from chardet import detect
from Classes.ClassUtility import *


# get file encoding type
def get_encoding_type(file):
    with open(file, 'rb') as f:
        rawdata = f.read()
    return detect(rawdata)['encoding']


srcfile = "D:\\Per Subs\\Thunderstruck (2012).srt"
trgfile = "D:\\Thunderstruck (2012).srt"

from_codec = get_encoding_type(srcfile)

# add try: except block for reliability
try:
    with open(srcfile, 'r', encoding=from_codec) as f, open(trgfile, 'w', encoding='utf-8') as e:
        text = f.read()  # for small files, for big use chunks
        e.write(text)

    # os.remove(srcfile) # remove old encoding file
    # os.rename(trgfile, srcfile)  # rename new encoding
except UnicodeDecodeError:
    print('Decode Error')
except UnicodeEncodeError:
    print('Encode Error')
