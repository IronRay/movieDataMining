# -*- coding: utf-8 -*-
import requests

HEADER = {
    'User-Agent': 'Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate',
}

COOKIE = {
    'cookies': {}
}


def get(url, params=None, useHeaders=False, headers='', useCookies=False, cookies=''):
    if useHeaders:
        if headers:
            headers = headers
        else:
            headers = HEADER
    else:
        headers = ''

    if useCookies:
        if cookies:
            cookies = cookies
        else:
            cookies = COOKIE['cookies']
    else:
        cookies = ''

    response = requests.get(url, headers=headers, cookies=cookies, params=params, timeout=30)

    # print('< Get API Data Status_code: %s >' % response.status_code)
    # print('< Text: %s >' % response.text)
    # print('< Url: %s >' % response.url)

    return response
