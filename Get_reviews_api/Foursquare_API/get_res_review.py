# -*- coding: utf8 -*-
import json, requests
import datetime

near_list = ['Chicago', 'Manchester', 'London', 'Liverpool', 'Oxford']

for i in near_list:
    params = dict(
        client_id='FN5PS1FYKITOSMYDRGMK3UGQVAVZD5GNTCPGBDTFDHJLMC42',
        client_secret='PXPLYT5M23203GXN4ABRCZEKC5ETYJX3EU3SQZKDF20FNSXC',
        v='20180501',
        near = i,
        query='Burger King',
        limit=50000
    )
    
    #EXPLORE = get venue recommendations
    url = 'https://api.foursquare.com/v2/venues/explore'
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)

    res_id = []
    res_name = []

    for i in range(len(data['response']['groups'][0]['items'])):
        res_id.append(data['response']['groups'][0]['items'][i]['venue']['id']) #res id로 접근.
        res_name.append(data['response']['groups'][0]['items'][i]['venue']['name'])

    count = 0
    url1 = 'https://api.foursquare.com/v2/venues/'
    url3 = '/tips'
    for i in range(len(res_name)):
        print('**************************************************************')
        print(res_name[i])
        print('**************************************************************')
        url2 = str(res_id[i])
        url = url1+url2+url3
        params2 = dict(
          venue_id = url2,
          client_id='FN5PS1FYKITOSMYDRGMK3UGQVAVZD5GNTCPGBDTFDHJLMC42',
          client_secret='PXPLYT5M23203GXN4ABRCZEKC5ETYJX3EU3SQZKDF20FNSXC',
          sort = 'recent', #popular , recent 가능
          limit= 1000,
          offset=1,
          v='20180505'
        )

        resp = requests.get(url = url, params=params2)
        data = json.loads(resp.text)
        print('----------------------------------------')
        print(res_name[i], '식당의 리뷰 수집')
        print('----------------------------------------')
        print('리뷰 수 : ',data['response']['tips']['count'])
        for j in range(len(data['response']['tips']['items'])):
          print(j+1, " ",data['response']['tips']['items'][j]['text'])

          #train_text = train_text + str(data['response']['tips']['items'][j]['text'])
          #train_text = train_text + " :flag: "
          #count += 1

          when = data['response']['tips']['items'][j]['createdAt']
          when = datetime.datetime.fromtimestamp(when)
          print('   의 리뷰 작성일 :  ',when)

# SAVE REVIEW
"""
print(train_text)
f = open('./bigmac_review_test.txt','w')
f.write(train_text)
f.close()
"""