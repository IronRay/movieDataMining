# -*- coding: utf-8 -*-
import json

from miner.baseClasses.miner import Miner
from miner.baseClasses.movie import Movie
from miner.baseClasses.user import User
from miner.baseClasses.comment import Comment

from miner.toolBox.apiHandler import doubanApi


class Douban(Miner):
    """docstring for douban"""

    def __init__(self):
        super(Douban, self).__init__(name='douban', baseUrl='m.douban.com')

    def getAllMovieCommentData(self, movie):
        pass

    def getMovieCommentData():
        commentJson = doubanApi.getMovieCommentData(id=id)

        comment = json.loads(commentJson.text)

        return comment


if __name__ == '__main__':
    # Here is test case.

    douban = Douban()
    # douban.getMovieCommentApi('25801066')
