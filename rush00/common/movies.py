from django.conf import settings
import requests


class Movies_info:
    film_list = []

    def get_info_list(self):
        titles_movies = settings.MOVIES
        for title in titles_movies:
            # try except
            response_json = requests.get(
                'http://www.omdbapi.com/?apikey=3cc63f26&t="' + title + '"'
            )
            # code check , if !200 -> raise 404
            res = response_json.json()
            self.film_list.append(res)
        return self.film_list

    def get_list(self):
        if len(self.film_list) == 0:
            self.film_list = self.get_info_list()
        return self.film_list
