from prototype_cache.prototype import Prototype
from copy import deepcopy
import datetime


class Application(Prototype):
    def __init__(self, name, category, rating, reviews, size, installs, last_updated,
                 android_version):
        self.name = name
        self.category = category
        self.rating = rating
        self.reviews = reviews
        self.size = size
        self.installs = installs
        self.last_updated = last_updated
        self.last_search_date = datetime.datetime.now()
        self.android_version = android_version
        self.comments_reviews = []

    def __str__(self):
        output = (f"\n::::::::::::::::::::::::::::::::\nAPP NAME: {str(self.name).upper()}\n"
                  f"Category: {self.category}\n"
                  f"Rating: {self.rating}\n"
                  f"Reviews: {self.reviews}\n"
                  f"Size: {self.size}\n"
                  f"Installs: {self.installs}\n"
                  f"Last update: {self.last_updated}\n"
                  f"Last search date: {self.last_search_date}\n"
                  f"Android version: {self.android_version}\n"
                  f"Comments reviews:\n")
        str_comments = ""
        for comment in self.comments_reviews:
            str_comments += f"{str(comment)}\n\t-------------------------------------\n"
        return output + str_comments + "\n"

    def clone(self):
        return deepcopy(self)
