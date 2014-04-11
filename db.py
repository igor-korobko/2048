# -*- coding: utf-8 -*-

import redis


class DB:

    connection = 0

    def __init__(self):
        self.connection = redis.StrictRedis(host='0.0.0.0', port=6379, db=7)

    def save(self, array, key):
        self.connection.delete(key)
        self.connection.set(key, array)
        self.connection.publish(key, array)
        return array

    def get(self, key):
        array = []
        s = self.connection.get(key)
        s = s[slice(1, -1)]
        for i in s.split(", "):
            array.append(int(i))
        return array

    def publish(self, array, key):
        self.connection.publish(key, array)


class Subscribe:

    r = 0

    def __init__(self, server):
        self.r = redis.Redis(host=server, port=6379, db=7)

    def subscribe(self, key):

        p = self.r.pubsub()
        p.psubscribe(key)

        for m in p.listen():
                if m['pattern'] == key and m['channel'] == key:
                    array = []
                    s = m["data"][slice(1, -1)]
                    for i in s.split(", "):
                        array.append(int(i))
                    return array
