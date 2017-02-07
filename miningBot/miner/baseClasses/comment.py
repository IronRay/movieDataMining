# -*- coding: utf-8 -*-
from miner.baseClasses.mineral import Mineral
from miner.baseClasses.user import User


class Comment(Mineral):
    """docstring for User"""

    def __init__(self, id, platformName, userID, rating, content, creatTime, favourCount, replyCount):
        super(Comment, self).__init__(id, platformName)
        self.userID = userID

        self.rating = rating
        self.content = content
        self.creatTime = creatTime

        self.favourCount = favourCount
        self.replyCount = replyCount

    def commentDataHandler(self):
        pass

    def outputInfo(self):
        print("< id:%s >" % (self.id))
        print("< platformName:%s >" % (self.platformName))
        print("< userID:%s >" % (self.userID))

        print("< rating:%s >" % (self.rating))
        print("< content:%s >" % (self.content))
        print("< creatTimg:%s >" % (self.creatTime))

        print("< favourCount:%s >" % (self.favourCount))
        print("< replyCount:%s >\n" % (self.replyCount))


if __name__ == '__main__':
    # Here is test case.
    pass
