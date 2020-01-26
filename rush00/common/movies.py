from django.conf import settings
import requests

class Movies_info:
    film_list = []

    @classmethod
    def get_info_list(cls):
        titles_movies = settings.MOVIES
        for title in titles_movies:
            # try except
            response_json = requests.get(
                'http://www.omdbapi.com/?apikey=63ce3381&t="' + title + '"'
            )
            # code check , if !200 -> raise 404
            res = response_json.json()
            cls.film_list.append(res)

    def get_list(self):
        if len(self.film_list) == 0:
            self.get_info_list()
        return self.film_list
