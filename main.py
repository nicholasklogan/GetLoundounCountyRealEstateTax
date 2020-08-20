import requests

import re

def get_realestate_tax():
    for line in requests.post(
        'https://www.loudounportal.com/taxes/default.aspx',
        {
            '__EVENTTARGET': 'ctl00$cphMainContent$SkeletonCtrl_3$btnSearch',
            'ctl00$cphMainContent$SkeletonCtrl_3$drpSearchParam': 'Parcel ID Number',
            'ctl00$cphMainContent$SkeletonCtrl_3$txtSearchParam': # ENTER PARCEL ID HERE
        }
    ).text.split('\r\n'):
        if 'AccountSumTotalDue' in line:
            return re.match('.*?AccountSumTotalDue">(?P<due>.*?)</span></h4>\s*', line).groupdict()['due']

