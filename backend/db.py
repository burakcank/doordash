from pymongo import MongoClient, TEXT, DESCENDING

from data_generator import DataGenerator


class Database:
    def __init__(self):
        # docker - mongo:27017
        self.client = MongoClient(host="mongo")
        self.db = self.client.doordasher
        self.db.restaurants.create_index([("name", TEXT)])

        self.dg = DataGenerator()

    def insert_random_data(self):
        # generate restaurant data
        restaurants = self.db.restaurants
        restaurants.insert_many(self.dg.generate_restaurant(1000))

    def text_search(self, search_words):
        """
        Text search in database.
        """
        return self.db.restaurants.find(
            {"$text": {"$search": search_words}}, {"score": {"$meta": "textScore"}}
        ).sort([("score", {"$meta": "textScore"})])
