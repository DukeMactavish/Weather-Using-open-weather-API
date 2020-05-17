import requests
import json
import csv
import datetime
import time




class Weather:
    # https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={YOUR API KEY}
    url='https://api.openweathermap.org/data/2.5/onecall?'
    key='aa1971877144126023f3c195462ecb6a'
    file='Report'

    def __init__(self, lat, lon, exclude):
        self.lat = lat
        self.lon = lon
        self.exclude=exclude
        self.appid=self.key
        #self.point = lat + ',' + lon
        self.payload = {'lat':lat,'lon':lon,'exclude':exclude,'appid':self.appid,'units':'metric'}
        self.filename = str(Weather.file) + '.csv'
    def get_report(self):
        data = json.loads(requests.get(Weather.url,params=self.payload).text)
        x = datetime.datetime(2018, 6, 1)
        a=x.strftime("%H")
        #print(json.dumps(data, indent=2, sort_keys=True))
        req_data=[]
        req_data.append(data['current']['clouds'])
        req_data.append(data['current']['dew_point'])
        req_data.append(data['current']['feels_like'])
        req_data.append(data['current']['humidity'])
        req_data.append(data['current']['pressure'])
        req_data.append(data['current']['sunrise'])
        req_data.append(data['current']['sunset'])
        req_data.append(data['current']['temp'])
        req_data.append(data['current']['uvi'])
        req_data.append(data['current']['wind_speed'])
        req_data.append(data['current']['weather'][0]['main'])
        req_data.append(a)

        with open(self.filename, 'a', newline='')as f:
            csvwriter = csv.writer(f, )
            csvwriter.writerow(req_data)
        print("Running")
if __name__ == '__main__':
    while True:
        lon = '88.36972'
        lat = '22.569719'
        exclude='hourly,daily'
        ob=Weather(lat,lon,exclude)
        ob.get_report()
        time.sleep(1800)
