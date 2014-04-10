# -*- coding: utf-8 -*-

import redis


class DB:

    connection = 0

    def __init__(self):
        self.connection = redis.StrictRedis(host='localhost', port=6379, db=7)

    def save(self, array, key):
        self.connection.delete(key)
        self.connection.set(key, array)
        return array

    def get(self, key):
        array = []
        s = self.connection.get(key)
        s = s[slice(1, -1)]
        for i in s.split(", "):
            array.append(int(i))
        return array
