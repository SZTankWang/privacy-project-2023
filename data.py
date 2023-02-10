import json
import pandas as pd
import csv 

def parse_har_file(har_file):
    
    with open(har_file, encoding='utf8') as f:
        har_txt = json.loads(f.read())

    entries =  har_txt["log"]["entries"]
    d = {"methods": [], "urls": [], "ip address": []}
    for i in range(len(entries)):
        d["methods"].append(entries[i]["request"]["method"])
        url = entries[i]["request"]["url"].split('?')[0].split('/')
        num = 4
        if (len(url[3]) > 30): num = 3
        d["urls"].append('/'.join(url[:num]))
        if 'serverIPAddress' in entries[i]:
            d['ip address'].append(entries[i]['serverIPAddress'])
        else:
            d['ip address'].append(' ')

    df = pd.DataFrame(data=d)
    return df


def query_counts_to_csv(filename, df):
    df.groupby(['methods','urls'])['urls'].size().reset_index(name='count').to_csv(filename, index=False)


# df = parse_har_file('open.spotify.com.har')
# query_counts_to_csv("spotify_records.csv", df)



    
