# -*- coding: utf-8 -*-
import pymysql


class DataBase(object):
    """docstring for DataBase"""

    def __init__(self, dbConfig):
        self.dbConfig = dbConfig
        self.connection = self.connect(dbConfig=self.dbConfig)

    def connect(self, dbConfig):
        host = dbConfig['host']
        user = dbConfig['user']
        password = dbConfig['password']
        db = dbConfig['db']

        connection = pymysql.connect(host=host,
                                     user=user,
                                     password=password,
                                     db=db,
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

        host = ''
        user = ''
        password = ''
        db = ''

        connection.autocommit(True)

        return connection

    def insertMovieInfo(self, movie):
        pass

    def insertUserInfo(self, user):
        pass

    def insertCommentInfo(self, comment):
        with self.connection.cursor() as cursor:
            sql = 'INSERT INTO `MOVIE_COMMENTS_TEST_1` (`commentID`,`platformName`,`userID`, `rating`, `content`, `creatTime`, `favourCount`,`replyCount`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'

            valueTuple = (comment.id, comment.platformName, comment.userID, comment.rating, comment.content, comment.creatTime, comment.favourCount, comment.replyCount)

            cursor.execute(sql, valueTuple)


if __name__ == '__main__':

    # userInfo = 'testInfo'
    pass
