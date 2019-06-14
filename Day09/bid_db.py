# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 13:44:49 2019

@author: Aakriti
"""

client = pymongo.MongoClient("mongodb://akkicluster:<password>@clusterakki-shard-00-00-4duws.mongodb.net:27017,clusterakki-shard-00-01-4duws.mongodb.net:27017,clusterakki-shard-00-02-4duws.mongodb.net:27017/test?ssl=true&replicaSet=clusterakki-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test
mongodb://akkicluster:<password>@clusterakki-shard-00-00-4duws.mongodb.net:27017,clusterakki-shard-00-01-4duws.mongodb.net:27017,clusterakki-shard-00-02-4duws.mongodb.net:27017/test?ssl=true&replicaSet=clusterakki-shard-0&authSource=admin&retryWrites=true&w=majority