from django.conf import settings
from django.shortcuts import Http404
import requests

class Movies_info:
    film_list = []

    @classmethod
    def get_info_list(cls):
        titles_movies = settings.MOVIES
        for title in titles_movies:
            try:
                response_json = requests.get(
                    'http://www.omdbapi.com/?apikey=63ce3381&t="' + title + '"'
                )
            except Exception as e:
                raise Http404()
            if response_json.status_code != 200:
                raise Http404()
            res = response_json.json()
            if (res['Title'] == 'N/A'):
                raise Http404()
            if (res['Poster'] == 'N/A'):
                raise Http404()
            if (res['imdbRating'] == 'N/A'):
                raise Http404()

            cls.film_list.append(res)

    def get_list(self):
        if len(self.film_list) == 0:
            self.get_info_list()
        return self.film_list
