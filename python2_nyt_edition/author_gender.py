import requests 
import json 
from pprint import pprint 
import sys 
from datetime import date
import random
import time


years_to_check = [1960,1980,2000, 2016]

# ENTER YOUR API KEYS
api_key = ["[API KEY HERE]", "[API KEY HERE]", "[API KEY HERE]", "[API KEY HERE]"]

base_url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?"

    
def random_day(target_year):
    start_date = date.today().replace(day=1, month=1, year=target_year).toordinal()
    end_date = date.today().replace(day=31, month=12, year=target_year).toordinal()
    random_day = date.fromordinal(random.randint(start_date, end_date))
    return random_day

def get_num_pages(formatted_day):
    time.sleep(1)
    url = base_url + "begin_date=" + formatted_day + "&end_date=" + formatted_day + "&page=" +str(0) + "&fq=article&api-key=" + random.choice(api_key)
    resp = requests.get(url)
    data = json.loads(resp.text)
    try:
        hits = data["response"]["meta"]["hits"]
    except:
        print "API KEY DECLINED, VPN?"
        return 0
    return int(hits)/10

# download files here: http://files.leoneckert.com/female_names.txt
# and here: http://files.leoneckert.com/male_names.txt   
f_names = set()
for line in open("female_names.txt", "r"):
    line = line.strip().lower()
    f_names.add(line)
m_names = set()
for line in open("male_names.txt", "r"):
    line = line.strip().lower()
    m_names.add(line)

def is_male(name):
    if name in m_names: 
        return True
    else:
        return False

def is_female(name):
    if name in f_names: 
        return True
    else:
        return False


def get_author_gender(formatted_day, page):
    time.sleep(1)
    genders = list()
    url = base_url + "begin_date=" + formatted_day + "&end_date=" + formatted_day + "&page=" +str(page) + "&fq=article&api-key=" + random.choice(api_key)
    resp = requests.get(url)
    data = json.loads(resp.text)
    try:
        for article in data["response"]["docs"]:
            try:
                name = article["byline"]["person"][0]["firstname"].lower()
                if is_male(name) and not is_female(name):
                    genders.append("M")
                elif is_female(name) and not is_male(name):
                    genders.append("F")

            except: TypeError
    except:
        print "API KEY DECLINED, VPN?"
    return genders




print "Gender of New York Times contributers.\n"
for year in years_to_check:
    print year

    sample_size = 20

    genders = list()
    days_checked = set()

    r_day = str(random_day(year))

    while len(genders) < sample_size:
        while r_day in days_checked:
            r_day = str(random_day(year))
        days_checked.add(r_day)
        day = str(r_day)
        # print day,
        formatted_day = day.split("-")
        formatted_day = "".join(formatted_day)

        # how many pages are there?
        numPages = get_num_pages(formatted_day) 
        if numPages == 0: continue
        random_page = random.choice(range(numPages))
        genders += get_author_gender(formatted_day, random_page)


    genders = genders[:sample_size]
    print "".join(sorted(genders)) + "\n"


    
        

