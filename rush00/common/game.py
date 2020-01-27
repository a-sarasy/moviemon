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

class Selector():
    slot_place = 0

    @classmethod
    def minus(cls):
        cls.slot_place -= 1

    @classmethod
    def plus(cls):
        cls.slot_place += 1

    @classmethod
    def reset(cls):
        cls.slot_place = 0        

class data_game():
    data = {}
    list_movie_nc = []
    capturable = ''

    def load_game(self, save_file):
        gd_file = open(settings.SAVE_FILES + '/' + save_file, 'rb')
        self.data = pickle.load(gd_file)
        gd_file.close()

    def save_game(self, slot):
        c = re.compile("^slot([{}])_([0-9]*)_([0-9]*)\.mmg$".format(list(['A','B','C'])[slot]))
        for s in os.listdir(settings.SAVE_FILES):
            match = c.match(s)
            if match and int(match.group(2)) < int(match.group(3)) and int(match.group(3)) == len(settings.MOVIES):
                os.remove("{}/{}".format(settings.SAVE_FILES,match.group()))
        pathfile = "{}/slot{}_{}_{}.mmg".format(settings.SAVE_FILES,list(['A','B','C'])[slot],len(self.data['moviedex']),len(self.data['list_moviemon']))
        gd_file = open(pathfile, 'wb')
        pickle.dump(self.data,gd_file)
        gd_file.close()

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
            if not movie['imdbID'] in self.data['moviedex']:
                movie_nc.append(movie['imdbID'])
        return(movie_nc)
    
    def get_random_movie(self):
        list_moviemon_nc = self.get_list_movi_nc()
        return list_moviemon_nc[random.randint(0,len(list_moviemon_nc) - 1)]
    
    def get_strength(self):
        return(len(self.data['moviedex']))
    
    def get_movie(self, moviemon_id):
        for movie in self.data["list_moviemon"]:
            if movie['imdbID'] ==  moviemon_id:
                detail_movie = {
                    "name" : movie['Title'],
                    "poster" : movie['Poster'],
                    "real" : movie["Director"],
                    "year" : movie["Year"],
                    "rating" : movie['imdbRating'],
                    "synopsis" : movie["Plot"],
                    "actors" : movie["Actors"],
                }
                return detail_movie
        return None
    
    def checkpos(self):
        if self.data['position'][0] < 0 or self.data['position'][0] >= settings.GRID_SIZE:
            self.load_state()
        elif self.data['position'][1] < 0 or self.data['position'][1] >= settings.GRID_SIZE:
            self.load_state()
        else:
            return 1
        return 0
    
    @classmethod
    def define_capturable(cls, movie_id):
        cls.capturable = movie_id

    def transform_events(self, movieball_event, moviemon_id):
        events = ['','', '#']
        if movieball_event == "True":
            events[0] = 'You just found a ball!'
            self.data['nbr_movieball'] += 1
        if moviemon_id != "":
            movie_name = self.get_movie(moviemon_id)['name']
            events[1] = "You encountered " + movie_name + ", Press A to capture it!"
            events[2] = 'http://127.0.0.1:8000/battle/' + moviemon_id + '/'
            self.define_capturable(moviemon_id)
        return events

    def try_random_events(self):
        events = ['', '#']
        if random.randint(1, 100) <= settings.FIND_BALL_PROBA_PERCENT:
            events[0] = True
        if random.randint(1, 100) <= settings.FIND_MOVIEMON_PROBA_PERCENT:
            #select random uncaptured movie
            movie_id = self.get_random_movie()
            events[1] = movie_id
        return events


if __name__ == "__main__":
    d = data_game()
    d.load(0,0,5,["film1", "film2"])
    