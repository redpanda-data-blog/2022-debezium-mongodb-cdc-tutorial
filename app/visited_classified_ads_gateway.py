#!/usr/bin/env python3

import time
import json
import random
import pymongo
import string


def random_classified_id():
    return random.randint(1000, 5000)

def random_user_id():
    return random.randint(1, 10000)

def random_url():
    return f"www.pandonline-classified-ads.com/{get_random_string()}"

def get_random_string():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))

def get_data():
    data = {}

    data["classifiedId"] = random_classified_id()
    data["userId"] = random_user_id()
    data["url"] = random_url()

    return data

def main():
    myclient = pymongo.MongoClient("mongodb://mongo-1:27017/")
    mydb = myclient["testdb"]
    mycol = mydb["classifieds"]

    for _ in range(20000):
        data = get_data()
        mycol.insert_one(data)
        print(f"Classified data is saved: {data}")
        time.sleep(5)


if __name__ == "__main__":
    main()