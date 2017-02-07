# -*- coding: utf-8 -*-
import json

from miner.baseClasses.mineral import Mineral


class MovieInfo(object):
    """docstring for MovieInfo"""

    def __init__(self, idInfo, basicInfo, artistesInfo):
        self.idInfo = idInfo
        self.basicInfo = basicInfo
        self.artistesInfo = artistesInfo


class IdInfo(object):
    """docstring for idInfo"""

    def __init__(self, showID, doubanID, maoyanID, taopiaopiaoID):
        self.showID = showID
        self.doubanID = doubanID
        self.maoyanID = maoyanID
        self.taopiaopiaoID = taopiaopiaoID


class BasicInfo(object):
    """docstring for basicInfo"""

    def __init__(self, showName, showNameEn, showType, openTime, year, country, openCountry, description, easterEggsInfo, clasification):
        self.showName = showName
        self.showNameEn = showNameEn
        self.showType = showType
        self.openTime = openTime
        self.year = year
        self.country = country
        self.openCountry = openCountry
        self.description = description
        self.easterEggsInfo = easterEggsInfo
        self.clasification = clasification


class Clasification(object):
    """docstring for clasification"""

    def __init__(self, name, title):
        self.name = name
        self.title = title


class EasterEggsInfo(object):
    """docstring for easterEggsInfo"""

    def __init__(self, easterEggsCount, easterEggsDescription):
        self.easterEggsCount = easterEggsCount
        self.easterEggsDescription = easterEggsDescription


class ArtistesInfo(object):
    """docstring for artistesInfo"""

    def __init__(self, actors, directors):
        self.actors = actors
        self.directors = directors


class Artiste():
    """docstring for artiste"""

    def __init__(self, artisteName, artisteNameEn, profession, artisteID):
        self.artisteName = artisteName
        self.artisteNameEn = artisteNameEn
        self.profession = profession
        self.artisteID = artisteID


class Actor(Artiste):
    """docstring for actor"""

    def __init__(self, artisteName, artisteNameEn, profession, artisteID, roleName):
        super(Actor, self).__init__(artisteName, artisteNameEn, profession, artisteID)
        self.roleName = roleName


class Director(Artiste):
    """docstring for director"""

    def __init__(self, artisteName, artisteNameEn, profession, artisteID):
        super(Director, self).__init__(artisteName, artisteNameEn, profession, artisteID)


class Movie(Mineral):
    """docstring for Movie"""

    def __init__(self, id, platformName):
        super(Movie, self).__init__(id, platformName)
        self.commentInfos = []

    def handleCommentInfos(self, commentInfos):
        pass

    def appendCommentInfos(self, commentInfos):
        for commentInfo in commentInfos:
            self.commentInfos.append(commentInfo)

    def handleMovieData(self, movieData):
        def getIDInfo():
            showID = self.id
            doubanID = ''
            maoyanID = ''
            taopiaopiaoID = self.id

            idInfo = IdInfo(showID, doubanID, maoyanID, taopiaopiaoID)

            return idInfo

        def getBasicInfo(transition):
            showName = transition['data']['returnValue']['showName']
            showNameEn = transition['data']['returnValue']['showNameEn']
            showType = transition['data']['returnValue']['type']
            openTime = transition['data']['returnValue']['openTime']
            year = transition['data']['returnValue']['features']['year']
            country = transition['data']['returnValue']['country']
            openCountry = transition['data']['returnValue']['openCountry']
            description = transition['data']['returnValue']['description']

            easterEggsCount = transition['data']['returnValue']['easterEggsCount']
            easterEggsDescription = transition['data']['returnValue']['easterEggsInfo']
            easterEggsInfo = EasterEggsInfo(easterEggsCount, easterEggsDescription)

            clasificationName = transition['data']['returnValue']['showDataList'][4]['name']
            clasificationTitle = transition['data']['returnValue']['showDataList'][4]['title']

            clasification = Clasification(name=clasificationName, title=clasificationTitle)

            basicInfo = BasicInfo(showName, showNameEn, showType, openTime, year, country, openCountry, description, easterEggsInfo, clasification)

            return basicInfo

        def getArtistesInfo(transition):
            def getActors(transition):
                actors = []
                actorsTransition = transition['data']['returnValue']['artistes']['actor']

                for actorTransition in actorsTransition:
                    artisteName = actorTransition['artisteName']
                    artisteNameEn = actorTransition['artisteNameEn']
                    profession = actorTransition['profession']
                    roleName = actorTransition['roleName']
                    artisteID = actorTransition['id']
                    actor = Actor(artisteName, artisteNameEn, profession, roleName, artisteID)

                    actors.append(actor)

                return actors

            def getDirectors(transition):
                directors = []
                directorsTransition = transition['data']['returnValue']['artistes']['directors']

                for directorTransition in directorsTransition:
                    artisteName = directorTransition['artisteName']
                    artisteNameEn = directorTransition['artisteNameEn']
                    profession = directorTransition['profession']
                    artisteID = directorTransition['id']
                    director = Director(artisteName, artisteNameEn, profession, artisteID)

                    directors.append(director)

                return directors

            actors = getActors(transition)
            directors = getDirectors(transition)

            artistesInfo = ArtistesInfo(actors, directors)

            return artistesInfo

        def outputInfo(movieInfo):

            print("<idInfo>")
            print("<showID: %s>" % movieInfo.idInfo.showID)
            print("<doubanID: %s>" % movieInfo.idInfo.doubanID)
            print("<maoyanID: %s>" % movieInfo.idInfo.maoyanID)
            print("<taopiaopiaoID: %s>" % movieInfo.idInfo.taopiaopiaoID)
            print('\n')

            print("<basicInfo>")
            print("<showName: %s>" % (movieInfo.basicInfo.showName))
            print("<showNameEn: %s>" % (movieInfo.basicInfo.showNameEn))
            print("<showType: %s>" % (movieInfo.basicInfo.showType))
            print("<openTime: %s>" % (movieInfo.basicInfo.openTime))
            print("<year: %s>" % (movieInfo.basicInfo.year))
            print("<country: %s>" % (movieInfo.basicInfo.country))
            print("<openCountry: %s>" % (movieInfo.basicInfo.openCountry))
            print("<description: %s>" % (movieInfo.basicInfo.description))
            print("<easterEggsInfo: %s:%s>" % (movieInfo.basicInfo.easterEggsInfo.easterEggsCount, movieInfo.basicInfo.easterEggsInfo.easterEggsDescription))
            print("<clasification: %s:%s>" % (movieInfo.basicInfo.clasification.name, movieInfo.basicInfo.clasification.title))
            print('\n')

            print("<artistesInfo>")
            print("<directors>")
            for director in movieInfo.artistesInfo.directors:
                print("<artisteName: %s>" % (director.artisteName))
                print("<artisteNameEn: %s>" % (director.artisteNameEn))
                print("<profession : %s>" % (director.profession))
                print("<artisteID: %s>" % (director.artisteID))
                print('\n')
            print('\n')

            print("<actors>")
            for actors in movieInfo.artistesInfo.actors:
                print("<artisteName: %s>" % (actors.artisteName))
                print("<artisteNameEn: %s>" % (actors.artisteNameEn))
                print("<roleName: %s>" % (actors.roleName))
                print("<profession : %s>" % (actors.profession))
                print("<artisteID: %s>" % (actors.artisteID))
                print('\n')
            print('\n')

        movieInfoJson = movieData

        transition = json.loads(movieInfoJson)

        idInfo = getIDInfo()
        basicInfo = getBasicInfo(transition)
        artistesInfo = getArtistesInfo(transition)

        movieInfo = MovieInfo(idInfo, basicInfo, artistesInfo)

        outputInfo(movieInfo)

        return movieInfo
