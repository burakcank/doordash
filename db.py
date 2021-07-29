from pymongo import MongoClient


class Database:
    def __init__(self):
        # docker - mongo:27017
        self.client = MongoClient(host="mongo")
        self.db = self.client.doordasher

    def insert_random_data(self):
        restaurant1 = {"name": "Burger King", "location": "maslak"}
        restaurant2 = {"name": "McDonalds", "number": "17", "location": "İstanbul"}

        restaurants = self.db.restaurants
        restaurants.insert_many([restaurant1, restaurant2])
