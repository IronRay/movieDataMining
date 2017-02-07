# -*- coding: utf-8 -*-
from miner.baseClasses.miningBot import MiningBot
from miner.baseClasses.movie import Movie
from miner.baseClasses.user import User
from miner.baseClasses.comment import Comment

from miner.toolBox.apiHandler import taopiaopiaoApi


class Taopiaopiao(MiningBot):
    """docstring for douban"""

    def __init__(self):
        super(Taopiaopiao, self).__init__(name='taopiaopiao', baseUrl='https://h5.m.taobao.com/app/movie/pages/index/index.html')

    def movieInfoMiner(self, movieID):
        if self.name is 'taopiaopiao':
            movie = Movie(platformName=self.name, id=movieID)

            movieData = taopiaopiaoApi.getMovieData(id=movieID)

            movieInfo = movie.handleMovieData(movieData)
        else:
            print('Wrong Platform: %s' % (self.name))

        return movieInfo


if __name__ == '__main__':
    # Here is test case.

    taopiaopiao = Taopiaopiao()
    taopiaopiao.movieInfoMiner(movieID='178341')
