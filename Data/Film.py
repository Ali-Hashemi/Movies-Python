import json
import os.path
from types import SimpleNamespace
from Classes.ClassUtility import *


class Film:
    def __init__(self, per_title=None, eng_title=None, release=None, score=None, director=None,
                 actors=None, per_genre=None, eng_genre=None, per_info=None, eng_info=None,
                 country=None, url_imdb=None, url_30nama=None,parent_guide=None, dubbed=0):
        if actors is None:
            actors = []

        if per_genre is None:
            per_genre = []

        if eng_genre is None:
            eng_genre = []

        self._per_title = per_title
        self._eng_title = eng_title
        self._release = release
        self._score = score
        self._director = director
        self._actors = actors
        self._per_genre = per_genre
        self._eng_genre = eng_genre
        self._per_info = per_info
        self._eng_info = eng_info
        self._country = country
        self._url_imdb = url_imdb
        self._url_30nama = url_30nama
        self._parent_guide = parent_guide
        self._dubbed = dubbed

    @property
    def per_title(self):
        return self._per_title

    @per_title.setter
    def per_title(self, value):
        self._per_title = value

    @property
    def eng_title(self):
        return self._eng_title

    @eng_title.setter
    def eng_title(self, value):
        self._eng_title = value

    @property
    def release(self):
        return self._release

    @release.setter
    def release(self, value):
        self._release = value

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value

    @property
    def director(self):
        return self._director

    @director.setter
    def director(self, value):
        self._director = value

    @property
    def actors(self):
        return self._actors

    @actors.setter
    def actors(self, value):
        self._actors = value

    @property
    def per_genre(self):
        return self._per_genre

    @per_genre.setter
    def per_genre(self, value):
        self._per_genre = value

    @property
    def eng_genre(self):
        return self._eng_genre

    @eng_genre.setter
    def eng_genre(self, value):
        self._eng_genre = value

    @property
    def per_info(self):
        return self._per_info

    @per_info.setter
    def per_info(self, value):
        self._per_info = value

    @property
    def eng_info(self):
        return self._eng_info

    @eng_info.setter
    def eng_info(self, value):
        self._eng_info = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @property
    def url_imdb(self):
        return self._url_imdb

    @url_imdb.setter
    def url_imdb(self, value):
        self._url_imdb = value

    @property
    def url_30nama(self):
        return self._url_30nama

    @url_30nama.setter
    def url_30nama(self, value):
        self._url_30nama = value

    @property
    def parent_guide(self):
        return self._parent_guide

    @parent_guide.setter
    def parent_guide(self, value):
        self._parent_guide = value

    @property
    def dubbed(self):
        return self._dubbed

    @dubbed.setter
    def dubbed(self, value):
        self._dubbed = value

    @staticmethod
    def translate_per_genre(genre):
        for index, value in enumerate(genre):
            if value == "اجتماعی":
                genre[index] = "درام"
            elif value == "طنز":
                genre[index] = "کمدی"
            elif value == "رومانتیک":
                genre[index] = "عاشقانه"
            elif value == "ملودرام":
                genre[index] = "درام"

        remove_array_duplicates(genre)

        return genre

    @staticmethod
    def title_translate():
        dictionary = {
            "Per Title": "per_title",
            "Eng Title": "eng_title",
            "Release": "release",
            "Score": "score",
            "Director": "director",
            "Actors": "actors",
            "Per Genre": "per_genre",
            "Eng Genre": "eng_genre",
            "Per Info": "per_info",
            "Eng Info": "eng_info",
            "Country": "country",
            "Link Imdb": "url_imdb",
            "Link 30nama": "url_30nama",
            "Parent Guide": "parent_guide",
            "Dubbed": "dubbed"
        }
        return dictionary

    def object_to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

    def get_all(self):
        dictionary = {
            "per_title": self.per_title,
            "eng_title": self.eng_title,
            "release": self.release,
            "score": self.score,
            "director": self.director,
            "actors": self.actors,
            "per_genre": self.per_genre,
            "eng_genre": self.eng_genre,
            "per_info": self.per_info,
            "eng_info": self.eng_info,
            "country": self.country,
            "url_imdb": self.url_imdb,
            "url_30nama": self.url_30nama,
            "parent_guide": self.parent_guide,
            "dubbed": self.dubbed,

        }

        return dictionary

    @staticmethod
    def json_file_to_class(json_file_location):
        film = None

        if os.path.exists(json_file_location):
            with open(json_file_location) as f:
                data = json.load(f, object_hook=lambda d: SimpleNamespace(**d))

            film = Film()
            film.per_title = data._per_title
            film.eng_title = data._eng_title
            film.release = data._release
            film.score = data._score
            film.director = data._director
            film.actors = data._actors
            film.per_genre = data._per_genre
            film.eng_genre = data._eng_genre
            film.per_info = data._per_info
            film.eng_info = data._eng_info
            film.country = data._country
            film.url_imdb = data._url_imdb
            film.url_30nama = data._url_30nama
            film.dubbed = data._dubbed

            if hasattr(data, '_parent_guide'):
                film.parent_guide = data._parent_guide

        else:
            Print.print_red("File did not found !!!")

        return film

    def is_empty(self) -> bool:
        is_empty = False

        dictionary = self.__dict__
        for i in dictionary:
            if i == "_dubbed":
                pass
            else:
                if not dictionary[i]:
                    is_empty = True
                    break
        return is_empty

    @staticmethod
    def get_empty_values(film):
        empty_values = {}

        dictionary = film.__dict__
        for i in dictionary:
            if not i == "_dubbed":
                if not dictionary[i]:
                    empty_values[i] = dictionary[i]

        return empty_values
