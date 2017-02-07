# -*- coding: utf-8 -*-


from miner.toolBox import requestHandler


def getMovieCommentData(id, version='v2', count='20', order_by='hot', start='0'):
    baseUrl = 'https://m.douban.com/rexxar/api'

    apiUrl = '%s/%s/%s/%s/%s' % (baseUrl, version, 'movie', id, 'interests')

    params = {
        'count': str(count),
        'order_by': str(order_by),
        'start': str(start)
    }

    response = requestHandler.get(url=apiUrl, params=params)

    return response
