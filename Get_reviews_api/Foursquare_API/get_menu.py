import json, requests

while True:
    input_code = input('input venue\'s code (c= break) : ')
    if input_code == 'c':
        break

    url1 = 'https://api.foursquare.com/v2/venues/'
    url2 = str(input_code)
    url3 = '/menu'
    url = url1 + url2+ url3

    params = dict(
        client_id = 'FN5PS1FYKITOSMYDRGMK3UGQVAVZD5GNTCPGBDTFDHJLMC42',
        client_secret = 'PXPLYT5M23203GXN4ABRCZEKC5ETYJX3EU3SQZKDF20FNSXC',
        v = '20180323'
    )

    resp = requests.get(url=url, params = params)
    data = json.loads(resp.text)

    print('---------------------------------------------------------')
    try:
        for i in range(int(data['response']['menu']['menus']['count'])):
            for j in range(int(data['response']['menu']['menus']['items'][i]['entries']['items'][0]['entries']['count'])):
                print(data['response']['menu']['menus']['items'][i]['entries']['items'][0]['entries']['items'][j]['name'])
            print('------------------------------------------------')
    except KeyError:
        print('No menu')
        continue