# -*- coding: utf-8 -*-

import redis


class DB:
    r = redis.StrictRedis(host='localhost', port=6379, db=7)
    r.set('foo', 'bar')
    print(r.get('foo'))