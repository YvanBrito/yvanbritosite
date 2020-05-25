import json
import time
import urllib.request
import pandas as pd

jsonToReturn = {}
counter = 0

def globalCases():
    # Confirmed cases
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    dataConfirmed = pd.read_csv(url)
    dataConfirmed = dataConfirmed.drop(columns=['Province/State', 'Country/Region', 'Lat', 'Long'])
    dataConfirmed = dataConfirmed.sum(axis=0)

    #Death cases
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
    dataDeaths = pd.read_csv(url)
    dataDeaths = dataDeaths.drop(columns=['Province/State', 'Country/Region', 'Lat', 'Long'])
    dataDeaths = dataDeaths.sum(axis=0)

    #Recovered cases
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
    dataRecovered = pd.read_csv(url)
    dataRecovered = dataRecovered.drop(columns=['Province/State', 'Country/Region', 'Lat', 'Long'])
    dataRecovered = dataRecovered.sum(axis=0)

    #-------------------------
    d = {'date': dataConfirmed.index.tolist(), 'confirmed': dataConfirmed.values.tolist(), 'deaths': dataDeaths.values.tolist(), 'recovered': dataRecovered.values.tolist()}
    data = pd.DataFrame(data=d)

    resp = json.loads(data.to_json(orient='records'))
    jsonToReturn['globalCases'] = resp

def brasilCases():
    # Confirmed cases
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    dataConfirmed = pd.read_csv(url)
    dataConfirmed = dataConfirmed.loc[dataConfirmed["Country/Region"] == "Brazil"]
    dataConfirmed = dataConfirmed.drop(columns=['Province/State', 'Country/Region', 'Lat', 'Long'])
    dataConfirmed = dataConfirmed.sum(axis=0)
    
    #Death cases
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
    dataDeaths = pd.read_csv(url)
    dataDeaths = dataDeaths.loc[dataDeaths["Country/Region"] == "Brazil"]
    dataDeaths = dataDeaths.drop(columns=['Province/State', 'Country/Region', 'Lat', 'Long'])
    dataDeaths = dataDeaths.sum(axis=0)

    #Recovered cases
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv"
    dataRecovered = pd.read_csv(url)
    dataRecovered = dataRecovered.loc[dataRecovered["Country/Region"] == "Brazil"]
    dataRecovered = dataRecovered.drop(columns=['Province/State', 'Country/Region', 'Lat', 'Long'])
    dataRecovered = dataRecovered.sum(axis=0)

    #-------------------------
    d = {'date': dataConfirmed.index.tolist(), 'confirmed': dataConfirmed.values.tolist(), 'deaths': dataDeaths.values.tolist(), 'recovered': dataRecovered.values.tolist()}
    data = pd.DataFrame(data=d)

    resp = json.loads(data.to_json(orient='records'))
    jsonToReturn['brasilCases'] = resp

def toptenconfirmed():
    # Confirmed cases
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    dataConfirmed = pd.read_csv(url)
    dataConfirmed = dataConfirmed.drop(columns=['Province/State','Lat', 'Long'])
    col = dataConfirmed['Country/Region']
    col = col.to_numpy()
    col = list(dict.fromkeys(col))

    data = []
    for c in col:
        d = dataConfirmed.loc[dataConfirmed["Country/Region"] == c]
        d = d.drop(columns=['Country/Region']).sum(axis=0)
        if (c == 'Diamond Princess'):
            continue
        if (c == 'Czechia'):
            c = 'Czech'
        if (c == 'Korea, South'):
            c = 'Korea (Republic of)'
        if (c == 'Taiwan*'):
            c = 'Taiwan'
        if (c == 'US'):
            c = 'USA'
        
        try:
            response = urllib.request.urlopen('https://restcountries.eu/rest/v2/name/' + c.replace(" ", "%20"))
        except:
            response = urllib.request.urlopen('https://restcountries.eu/rest/v2/name/' + c.split(" ", 1)[0])
        countryInfo = json.loads(response.read())
        d = d.values.tolist()
        country = {'Region': countryInfo[0]['region'], 'Country': c, 'value': d[len(d)-1]}
        data.append(country)
    
    data = sorted(data, key=lambda k: k['value'], reverse=True)[:10]
    data = pd.DataFrame(data=data)

    resp = json.loads(data.to_json(orient='records'))
    jsonToReturn['topTenConfirmed'] = resp

def worldregions():
    # Confirmed cases
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
    dataConfirmed = pd.read_csv(url)
    dataConfirmed = dataConfirmed.drop(columns=['Province/State','Lat', 'Long'])
    col = dataConfirmed['Country/Region']
    col = col.to_numpy()
    col = list(dict.fromkeys(col))

    data = {}
    for c in col:
        d = dataConfirmed.loc[dataConfirmed["Country/Region"] == c]
        d = d.drop(columns=['Country/Region']).sum(axis=0)
        if c == 'Diamond Princess':
            continue
        if c == 'Czechia':
            c = 'Czech'
        if c == 'Korea, South':
            c = 'Korea (Republic of)'
        if c == 'Taiwan*':
            c = 'Taiwan'
        if c == 'US':
            c = 'United States of America'
        
        try:
            response = urllib.request.urlopen('https://restcountries.eu/rest/v2/name/' + c.replace(" ", "%20"))
        except:
            response = urllib.request.urlopen('https://restcountries.eu/rest/v2/name/' + c.split(" ", 1)[0])
        countryInfo = json.loads(response.read())
        d = d.values.tolist()
        if data.get(countryInfo[0]['region']):
            data[countryInfo[0]['region']] = data[countryInfo[0]['region']] + d[len(d)-1]
        else:
            data[countryInfo[0]['region']] = d[len(d)-1]
    
    data = {k: v for k, v in sorted(data.items(), key=lambda item: item[1], reverse=True)}

    resp = []
    for key in data:
        resp.append({'Region': key, 'value': data[key]})
    
    data = pd.DataFrame(data=resp)

    resp = json.loads(data.to_json(orient='records'))
    jsonToReturn['worldregions'] = resp


def reloadData():

    globalCases()
    brasilCases()
    toptenconfirmed()
    worldregions()

    response = json.loads(urllib.request.urlopen('https://api.github.com/repos/CSSEGISandData/COVID-19/commits').read())
    jsonToReturn['updateTime'] = response[0]['commit']['author']['date']
    jsonToReturn['updateTime'] = jsonToReturn['updateTime'].replace('T', ' ').replace('Z', '.0')

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(jsonToReturn, f, ensure_ascii=False, indent=4)

while True:
    with open('data.json') as json_file:
        dateBefore = json.loads(json_file.read())['updateTime']

    response = json.loads(urllib.request.urlopen('https://api.github.com/repos/CSSEGISandData/COVID-19/commits').read())
    dateNow = response[0]['commit']['author']['date']
    dateNow = dateNow.replace('T', ' ').replace('Z', '.0')

    if dateBefore != dateNow:
        reloadData()
