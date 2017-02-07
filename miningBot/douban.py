# -*- coding: utf-8 -*-
import json
import time

from miner.baseClasses.miningBot import MiningBot
from miner.baseClasses.movie import Movie
from miner.baseClasses.user import User
from miner.baseClasses.comment import Comment

from miner.toolBox.apiHandler import doubanApi


class DoubanMovieMiningBot(MiningBot):
    """docstring for doubanMiningBot"""

    def __init__(self):
        super(DoubanMovieMiningBot, self).__init__(name='douban', baseUrl='m.douban.com')

    def movieMiningTaskGenerator(self, movieID):
        movie = Movie(id=movieID, platformName=self.name)
        self.movies.append(movie)

    def mineMovieList(self):
        # get all movieID on douban.com
        movieIDs = ''

        return movieIDs

    def mineAllMovieCommentInfo(self, movieID, step=20, start=0):
        total = 1
        nextStep = 0
        comments = []

        while nextStep < total:
            response = doubanApi.getMovieCommentData(id=movieID, start=nextStep)

            if response.status_code is 200:

                time.sleep(3)
                infoJson = response.text

                total, commentInfos = self.HandleMovieCommentJson(infoJson)

                for comment in commentInfos:
                    comments.append(comment)

                nextStep = nextStep + step
            else:
                return response.status_code

        return comments

    def HandleMovieCommentJson(self, jsonObj):
        commentInfos = []

        transition = json.loads(jsonObj)

        total = transition['total']

        for interest in transition['interests']:
            commentID = interest['id']
            platformName = self.name

            userID = interest['user']['id']
            gender = interest['user']['gender']
            userUrl = interest['user']['url']

            content = interest['comment']
            creatTime = interest['create_time']

            if interest['rating']:
                rating = interest['rating']['value'] * 2
            else:
                rating = ''

            favourCount = interest['vote_count']
            replyCount = ''

            comment = Comment(id=commentID, platformName=platformName, userID=userID, rating=rating, content=content, creatTime=creatTime, favourCount=favourCount, replyCount=replyCount)

            comment.outputInfo()
            # print('\n')

            commentInfos.append(comment)

        return total, commentInfos

    def saveMovieCommentInfos(self, commentInfos):
        if self.dataBase:
            for commentInfo in commentInfos:
                self.dataBase.insertCommentInfo(commentInfo)


if __name__ == '__main__':
    # Here is test case.

    bot = DoubanMovieMiningBot()
