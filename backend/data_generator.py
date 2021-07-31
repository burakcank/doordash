from faker import Faker

# determine faker seed
Faker.seed(0)


class Restaurant:
    def __init__(self, name, latlng, address, phone_number):
        self.name = name
        self.lat = float(latlng[0])
        self.lng = float(latlng[1])
        self.address = address
        self.phone_number = phone_number


class Meal:
    def __init__(self):
        pass


class DataGenerator:
    """
    Generate random data.
    """

    def __init__(self):
        self.fake = Faker()

    def generate_restaurant(self, data_count):
        result = list()
        for _ in range(data_count):
            rest = Restaurant(
                name=self.fake.company(),
                latlng=self.fake.latlng(),
                address=self.fake.address(),
                phone_number=self.fake.phone_number(),
            )
            result.append(rest.__dict__)

        return result
