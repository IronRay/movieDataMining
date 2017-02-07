# -*- coding: utf-8 -*-
from miner.baseClasses.miner import Miner
from miner.baseClasses.movie import Movie
from miner.baseClasses.user import User
from miner.baseClasses.comment import Comment

from miner.toolBox.apiHandler import taopiaopiaoApi


class Taopiaopiao(Miner):
    """docstring for douban"""

    def __init__(self):
        super(Taopiaopiao, self).__init__(name='taopiaopiao', baseUrl='https://h5.m.taobao.com/app/movie/pages/index/index.html')

    def getAllMovieData():
        pass

    def getMovieData(self, movieID):
        movie = Movie(platform=self.name, id=movieID)
        movie.getMovieInfo()

    def getMovieCommentApi(self, movie):
        pass


if __name__ == '__main__':
    # Here is test case.

    taopiaopiao = Taopiaopiao()
    taopiaopiao.getMovieData(movieID='178341')
