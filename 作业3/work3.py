from collections import Iterable, Iterator
import requests


class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0  # 通过index来确定具体迭代哪个城市的气温信息

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.get_weather(city)

    def get_weather(self, city):
        url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city
        r = requests.get(url)
        data = r.json()['data']['forecast'][0]
        return city, data['high'], data['low']


class WeatherIterable(Iterable):
    def __init(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


def show(W):
    for x in W:
        print(x)


if __name__=='__main__':

    W = WeatherIterator(['北京','上海','广州','长春'] * 3)
    show(W)