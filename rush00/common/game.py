import pickle
from common import movies
from django.conf import settings
import random
import os
import re

class slot():
    slot_place = 0

    @classmethod
    def minus(cls):
        if not cls.slot_place <= 0:
            cls.slot_place -= 1

    @classmethod
    def plus(cls):
        if not cls.slot_place >= 2:
            cls.slot_place += 1

    @classmethod
    def reset(cls):
        cls.slot_place = 0

        

class data_game():
    data = {}
    list_movie_nc = []
    def save_state(self):
        gd_file = open('gamedata', 'wb')
        pickle.dump(self.data,gd_file)
        gd_file.close()
    def load_state(self):
        gd_file = open('gamedata', 'rb')
        self.data = pickle.load(gd_file)
        gd_file.close()
    def load(self,posx, posy, movieball, moviedex):
        self.data = {
            "position": [posx, posy],
            "nbr_movieball": movieball,
            "moviedex": moviedex,
            "list_moviemon" : movies.Movies_info().get_list(),
            }
        self.list_movie_nc = self.get_list_movi_nc()
        return self
    def dump(self):
        return(self.data)
    def load_default_settings(self):
        self.data = {
            "position": [settings.POS_X, settings.POS_Y],
            "nbr_movieball":settings.NBR_MOVIEBALL,
            "moviedex":[],
            "list_moviemon" : movies.Movies_info().get_list(),
        }
        list_movie_nc = settings.MOVIES
        return self  
    def get_list_movi_nc(self):
        movie_nc = []
        for movie in self.data['list_moviemon']:
            if not movie['Title'] in self.data['moviedex']:
                movie_nc.append(movie['Title'])
        return(movie_nc)
    def get_random_movie(self):
        list_moviemon_nc = self.get_list_movi_nc()
        return list_moviemon_nc[random.randint(0,len(list_moviemon_nc) - 1)]
    def get_strength(self):
        return(len(self.data['moviedex']))
    def get_movie(self, moviemon):
        for movie in self.data["list_moviemon"]:
            if movie['Title'] ==  moviemon:
                detail_movie = {
                    "name" : movie['Title'],
                    "poster" : movie['Poster'],
                    "real" : movie["Director"],
                    "year" : movie["Year"],
                    "rating" : movie['Rated'],
                    "synopsis" : movie["Plot"],
                    "actors" : movie["Actors"],
                }
                return detail_movie
    def checkpos(self):
        if self.data['position'][0] < 0 or self.data['position'][0] >= settings.GRID_SIZE:
            self.load_state()
        elif self.data['position'][1] < 0 or self.data['position'][1] >= settings.GRID_SIZE:
            self.load_state()
        else:
            return 1
        return 0
    def try_random_events(self):
        event = ['', '']
        if random.randint(1, 100) <= settings.FIND_BALL_PROBA_PERCENT:
            event[0] = 'You just found a ball!'
            #add ball
        if random.randint(1, 000) <= settings.FIND_MOVIEMON_PROBA_PERCENT:
            #select random uncaptured movie
            event[1] = "You encountered " + 'MOVIEMON' + "Press ? to capture it!" 


if __name__ == "__main__":
    d = data_game()
    d.load(0,0,5,["film1", "film2"])
    