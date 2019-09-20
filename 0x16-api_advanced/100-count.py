#!/usr/bin/python3
import re
import requests
""" Modify prototype for handle pagination """


def count_words(subreddit, word_list, hot_list=[], after='null', flag=0):
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
            count_words(subreddit, word_list, hot_list, res_json['after'])
        else:
            """ flag for prevent the print result """
            flag = 1
    else:
        pass
    """ print only when the recursion finished """
    if flag == 1:
        key_dict = {}
        """ find word in the list of titles fill with the recursion """
        for word in word_list:
            num = 0
            rx = r'\b%s\b'% word
            for title in hot_list:
                num = num + len(re.findall(rx, title.lower()))
            key_dict[word] = num
        tup_list = sorted(key_dict.items(), key=lambda x: x[1], reverse=True)
        for tupl in tup_list:
            if tupl[1] != 0:
                print("{}: {}".format(tupl[0], tupl[1]))
