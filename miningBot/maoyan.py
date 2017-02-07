# -*- coding: utf-8 -*-
import json
import time

from miner.baseClasses.miningBot import MiningBot
from miner.baseClasses.movie import Movie
from miner.baseClasses.user import User
from miner.baseClasses.comment import Comment

from miner.toolBox.apiHandler import maoyanApi


class MaoyanMovieMiningBot(MiningBot):
    """docstring for MaoyanMiningBot"""

    def __init__(self):
        super(MaoyanMovieMiningBot, self).__init__(name='maoyan', baseUrl='m.maoyan.com')

    def movieMiningTaskGenerator(self, movieID):
        movie = Movie(id=movieID, platformName=self.name)
        self.movies.append(movie)

    def mineSpecMovieCommentInfo(self, movieID, step=15, start=0, num=60):
        total = 1
        nextStep = 0
        comments = []

        while nextStep < num:
            response = maoyanApi.getMovieCommentData(id=movieID, offset=nextStep)

            if response.status_code is 200:

                time.sleep(3)
                infoJson = response.text

                total, commentInfos = self.HandleMovieCommentJson(infoJson)

                for comment in commentInfos:
                    comments.append(comment)

                nextStep = nextStep + step
            else:
                print('< statusCode:%s >' % (response.status_code))
                return response.status_code

        print(len(comments))

        return comments

    def mineAllMovieCommentInfo(self, movieID, step=15, start=0):
        total = 1
        nextStep = 0
        comments = []

        while nextStep < total:
            response = maoyanApi.getMovieCommentData(id=movieID, offset=nextStep)

            if response.status_code is 200:

                time.sleep(3)
                infoJson = response.text

                total, commentInfos = self.HandleMovieCommentJson(infoJson)

                for comment in commentInfos:
                    comments.append(comment)

                nextStep = nextStep + step
            else:
                print('< statusCode:%s >' % (response.status_code))
                return response.status_code

        return comments

    def HandleMovieCommentJson(self, jsonObj):
        commentInfos = []

        transition = json.loads(jsonObj)

        total = transition['total']

        for cmt in transition['cmts']:
            # print(cmt)

            commentID = cmt['id']
            platformName = self.name

            userID = cmt['userId']

            if 'gender' in cmt:
                gender = cmt['gender']
            else:
                gender = ''

            userUrl = ''

            content = cmt['content']
            creatTime = cmt['startTime']

            rating = cmt['score'] * 2

            favourCount = cmt['approve']
            replyCount = cmt['reply']

            comment = Comment(id=commentID, platformName=platformName, userID=userID, rating=rating, content=content, creatTime=creatTime, favourCount=favourCount, replyCount=replyCount)

            commentInfos.append(comment)

            comment.outputInfo()
            # print('\n')

        return total, commentInfos

    def saveMovieCommentInfos(self, commentInfos):
        if self.dataBase:
            for commentInfo in commentInfos:
                # print(commentInfo.content)
                self.dataBase.insertCommentInfo(commentInfo)
        else:
            print('DB not connect')
            return False


if __name__ == '__main__':
    # Here is test case.

    bot = MaoyanMovieMiningBot()

    bot.startDBConnection()

    commentInfos = bot.mineSpecMovieCommentInfo(movieID='248904')

    bot.saveMovieCommentInfos(commentInfos=commentInfos)

    bot.closeDBConnection()
