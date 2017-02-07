# -*- coding: utf-8 -*-
from miner.toolBox import requestHandler


def getMovieCommentData(id, _v_='yes', offset='0'):
    baseUrl = 'http://m.maoyan.com/mmdb/'

    apiUrl = '%s/%s/%s/%s.%s' % (baseUrl, 'comments', 'movie', id, 'json')

    params = {
        '_v_': 'yes',
        'offset': str(offset)
    }

    response = requestHandler.get(url=apiUrl, params=params)

    return response
