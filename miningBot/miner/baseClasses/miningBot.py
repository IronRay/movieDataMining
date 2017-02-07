# -*- coding: utf-8 -*-
from miner.config.dbConfig import dbConfig
from miner.toolBox.dbHandler.dataBase import DataBase


class MiningBot(object):
    """docstring for Site"""

    def __init__(self, name, baseUrl):
        self.name = name
        self.baseUrl = baseUrl
        self.movies = []
        self.dataBase = ''

    def startDBConnection(self):
        self.dataBase = DataBase(dbConfig=dbConfig)

        return True

    def closeDBConnection(self):
        if self.dataBase:
            self.dataBase.connection.close()
        else:
            print('DB not connect')
            return False

        return True
