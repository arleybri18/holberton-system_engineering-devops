#!/usr/bin/python3
import requests
""" Modify prototype for handle pagination """


def recurse(subreddit, hot_list=[], after='null'):
    """ recursively call api """
    headers = {'User-Agent': 'Yony'}
    params = {'after': after}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(
        url,
        headers=headers,
        allow_redirects=False,
        params=params)
    if res.status_code == requests.codes.ok:
        res_json = res.json()['data']
        for subr in res_json['children']:
            hot_list.append(subr['data']['title'])
        if res_json['after'] is not None:
            """ call recursion if next page exist """
            recurse(subreddit, hot_list, res_json['after'])
    else:
        return None
    return hot_list
