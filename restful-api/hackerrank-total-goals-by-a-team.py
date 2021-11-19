#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#

def getTotalGoals(team, year):
    # Write your code here
    import requests, json
    url1 = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page='
    url2 = f'https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page='
    
    res_1 = requests.get(url1 + '1')
    res_2 = requests.get(url2 + '1')
    
    result_1 = json.loads(res_1.content)
    result_2 = json.loads(res_2.content)
    
    total_page_1 = result_1['total_pages']
    total_page_2 = result_2['total_pages']
    
    total = 0
    for cur in range(1, total_page_1 + 1):
        res = json.loads(requests.get(url1 + str(cur)).content)
        datas = res['data']
        for data in datas:
            if data['team1'].upper() == team.upper():
                total += int(data['team1goals'])
    
    for cur in range(1, total_page_2 + 1):
        res = json.loads(requests.get(url2 + str(cur)).content)
        datas = res['data']
        for data in datas:
            if data['team2'].upper() == team.upper():
                total += int(data['team2goals'])
        
    return total
    

if __name__ == '__main__':