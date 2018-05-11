# -*- coding: utf8 -*-
from pandas import Series, DataFrame
import datetime
import requests
import json

class Api(object):
    def __init__(self, USER_KEY, host="https://developers.zomato.com/api/v2.1",
                 content_type='application/json'):
        self.host = host
        self.user_key = USER_KEY
        self.headers = {
            "User-agent": "curl/7.43.0",
            'Accept': content_type,
            'X-Zomato-API-Key': self.user_key
        }

    def get(self, endpoint, params):
        url = self.host + endpoint + "?"
        for k,v in params.items():
            url = url + "{}={}&".format(k, v)
        url = url.rstrip("&")
        response = requests.get(url, headers=self.headers)
        return response.json()

class Pyzomato(object):
    def __init__(self, USER_KEY):
        self.api = Api(USER_KEY)

    def getCategories(self):
        categories = self.api.get("/categories", {})
        return categories

    def getCityDetails(self, **kwargs):
        params = {}
        available_keys = ["q", "lat", "lon", "city_ids", "count"]
        for key in available_keys:
            if key in kwargs:
                params[key] = kwargs[key]
        cities = self.api.get("/cities", params)
        return cities

    def getCollectionsViaCityId(self, city_id, **kwargs):
        params = {"city_id": city_id}
        optional_params = ["lat", "lon", "count"]

        for key in optional_params:
            if key in kwargs:
                params[key] = kwargs[key]
        collections = self.api.get("/collections", params)
        return collections

    def getCuisines(self, city_id, **kwargs):
        params = {"city_id": city_id}
        optional_params = ["lat", "lon"]

        for key in optional_params:
            if key in kwargs:
                params[key] = kwargs[key]
        cuisines = self.api.get("/cuisines", params)
        return cuisines

    def getEstablishments(self, city_id, **kwargs):
        params = {"city_id": city_id}
        optional_params = ["lat", "lon"]

        for key in optional_params:
            if key in kwargs:
                params[key] = kwargs[key]
        establishments = self.api.get("/establishments", params)
        return establishments

    def getByGeocode(self, lan, lon):
        params = {"lat": lan, "lon": lon}
        response = self.api.get("/geocode", params)
        return response

    def getLocationDetails(self, entity_id, entity_type):
        params = {"entity_id": entity_id, "entity_type": entity_type}
        location_details = self.api.get("/location_details", params)
        return location_details

    def getLocations(self, query, **kwargs):
        params = {"query": query}
        optional_params = ["lat", "lon", "count"]

        for key in optional_params:
            if key in kwargs:
                params[key] = kwargs[key]
        locations = self.api.get("/locations", params)
        return locations

    def getDailyMenu(self, restaurant_id):
        params = {"res_id": restaurant_id}
        daily_menu = self.api.get("/dailymenu", params)
        return daily_menu

    def getRestaurantDetails(self, restaurant_id):
        params = {"res_id": restaurant_id}
        restaurant_details = self.api.get("/restaurant", params)
        return restaurant_details

    def getRestaurantReviews(self, restaurant_id, **kwargs):
        params = {"res_id": restaurant_id}
        optional_params = ["start", "count"]

        for key in optional_params:
            if key in kwargs:
                params[key] = kwargs[key]
        reviews = self.api.get("/reviews", params)
        return reviews

    def search(self, **kwargs):
        params = {}
        available_params = [
            "entity_id", "entity_type", "q", "start",
            "count", "lat", "lon", "radius", "cuisines",
            "establishment_type", "collection_id",
            "category", "sort", "order"]

        for key in available_params:
            if key in kwargs:
                params[key] = kwargs[key]
        results = self.api.get("/search", params)
        return results


# FIND BURGER RES's ID버거 음식 취급하는 레스토랑 id 찾아내기 (20개가 max(?))#
city_code_list = [61,68,323]
p = Pyzomato('3d88e125cd88809e8fa4cf8642858681')
cuisines_code = 168  # burger code

review_text = []
review_score = []

for ij in range(len(city_code_list)):
    kb = p.search(cuisines = cuisines_code, count = 20, entity_type = 'city', entity_id = city_code_list[ij])
    res_id_list = []
    res_name_list = []
    for i in range(20):       ##range범위 뭘로해야하는지 모르겠음(len(kb)는 3까지밖에 안돔)!
        res_id_list.append(kb['restaurants'][i]['restaurant']['R']['res_id'])
        res_name_list.append(kb['restaurants'][i]['restaurant']['name'])

    print('-----------------------------------------------------')
    for i in range(len(res_id_list)):
        print("레스토랑 코드 : ", res_id_list[i])
        print("레스토랑 이름 : ", res_name_list[i])

        xx = p.getRestaurantReviews(res_id_list[i])
        reviewCNT = xx['reviews_count']
        print("리뷰 갯수 : ", reviewCNT)
        if reviewCNT == 0:
            print('리뷰 없음')
            continue
        elif reviewCNT >0 and reviewCNT < 5:
            for j in range(reviewCNT):
                print(xx['user_reviews'][j]['review']['rating'])
                print(xx['user_reviews'][j]['review']['review_text'])
                review_text.append(xx['user_reviews'][j]['review']['review_text'])
                review_score.append(xx['user_reviews'][j]['review']['rating'])
                print(datetime.datetime.fromtimestamp(xx['user_reviews'][j]['review']['timestamp']))
        else:
            for j in range(5):
                print(xx['user_reviews'][j]['review']['rating'])
                print(xx['user_reviews'][j]['review']['review_text'])
                review_text.append(xx['user_reviews'][j]['review']['review_text'])
                review_score.append(xx['user_reviews'][j]['review']['rating'])
                print(datetime.datetime.fromtimestamp(xx['user_reviews'][j]['review']['timestamp']))
        print('-----------------------------------------------------')


print('\n\n')
print(review_score)
print(review_text)

df = DataFrame(columns=("review_score","review_text"))
df['review_score'] = review_score
df['review_text'] = review_text
print(df)
f = open('df', 'w')
f.write('\n'.join(review_text))
f.close()

x3 = p.getLocationDetails('london',13)
print(x3)