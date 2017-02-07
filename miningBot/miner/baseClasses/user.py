# -*- coding: utf-8 -*-
from miner.baseClasses.mineral import Mineral


class User(Mineral):
    """docstring for User"""

    def __init__(self, id, platformName, gender, url):
        super(User, self).__init__(id, platformName)
        self.gender = gender
        self.url = url


if __name__ == '__main__':
    # Here is test case.
    pass
