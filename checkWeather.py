import requests
import pprint
import json

extract_info = []
line_break = '\n'
weather = ''
city = ''
temperature = ''
last_time = ''
pass_message = ''

def getweather():
    try:
        response = requests.get("http://api.wunderground.com/api/f144a4b91c08bc4a/forecast/conditions/alerts/q/autoip.json")
        #response = requests.get("http://autocomplete.wunderground.com/aq?query=" + city)
        weather_data = response.json()

        with open('result.json', 'w') as data:
            json.dump(weather_data, data, indent=4, sort_keys=True)
        # print('File creation successful!')
            #for i in grabdata['forecast']:
                #extract_info   
    except:
        print('File creation failed.')

def returninfo():
    try:
        with open('result.json') as info:
            listDict = json.load(info)
            city = listDict['current_observation']['display_location']['city']
                #your_city.append(l)
                #city = ''.join(your_city)
            content1 = ('The weather for ' + city + ': ')
            temperature = listDict['current_observation']['temperature_string']
                #get_temp.append(j)
                #temperature = ''.join(get_temp)
            content2 =('The temperature is ' + temperature + ".")
            weather = listDict['current_observation']['weather']
                #forecast_weather.append(k)
                #weather = ''.join(forecast_weather)
            content3 = (' The weather is ' + weather + ". ")
            last_time = listDict['current_observation']['observation_time']
                #get_time.append(i)
                #last_time = ''.join(get_time)
            content4 =(last_time)

            return str(content1 + content2 + content3 + content4)
            
    except:
        print('Information not found.')

getweather()
returninfo()
