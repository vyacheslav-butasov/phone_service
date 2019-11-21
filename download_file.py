import os
import requests
from bs4 import BeautifulSoup
from load_csv import load


files = os.listdir('files')
file = files[0]
local_file_date = file[-14:-4]
print('local_file_date', local_file_date)

url_website = 'https://rossvyaz.ru/deyatelnost/resurs-numeracii/vypiska-iz-reestra-sistemy-i-plana-numeracii'
selector_date1 = 'body > div.page.page--grey > div > div.container-fluid.wrapper > p:nth-of-type(2) > strong:nth-of-type(1)'
selector_date2 = 'body > div.page.page--grey > div > div.container-fluid.wrapper > p:nth-of-type(2) > strong:nth-of-type(2)'
r = requests.get(url_website)
data = r.text
soup = BeautifulSoup(data)
server_file_date1 = soup.select(selector_date1)[0].text # string '2'
server_file_date2 = soup.select(selector_date2)[0].text
server_file_date = server_file_date1 + server_file_date2

print(local_file_date, server_file_date)
if local_file_date != server_file_date:
    for file in files:
        os.remove('files/' + file)
    print('in IF')
    url_base = 'https://rossvyaz.ru/data/'
    files_on_server = ['ABC-3xx.csv', 'ABC-4xx.csv', 'ABC-8xx.csv' , 'DEF-9xx.csv']

    for file in files_on_server:
        r = requests.get(url_base + file)
        path = 'files/' + file

        with open(path, 'wb') as f:
            f.write(r.content)

        new_name = file[:-4] + '-' + server_file_date + '.csv'
        print(new_name)
        os.rename('files/'+file, 'files/' + new_name)
        print(r.status_code)
        print(r.headers['content-type'])
        print(r.encoding)
        
    downloaded_files = os.listdir('files')
    load(downloaded_files)
        
