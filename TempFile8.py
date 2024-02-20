from Classes.ClassUtility import *


class Main():
    def __init__(self):
        url = "https://m.media-amazon.com/images/M/MV5BYjhiNjBlODctY2ZiOC00YjVlLWFlNzAtNTVhNzM1YjI1NzMxXkEyXkFqcGdeQXVyMjQxNTE1MDA@._V1_.jpg"

        open_in_browser(url)

        Download(url, "D:/Covers", str("Imdb-Cover"), ".jpg")


Main()
