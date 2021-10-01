from typing import Counter
import urllib.request
import json
from datetime import datetime
import sys

def test_time():
    date_time_str1 = '18/09/19 01:55:19'
    date_time_str2 = '25/09/19 01:55:19'

    date_time_obj1 = datetime.strptime(date_time_str1, '%d/%m/%y %H:%M:%S')
    date_time_obj2 = datetime.strptime(date_time_str2, '%d/%m/%y %H:%M:%S')

    print(date_time_obj1 < date_time_obj2)

    print("The type of the date is now",  type(date_time_obj1))
    print("The date is", date_time_obj1)

# test_time()

def main():

    # To get TOKEN for viewing unpublished data, go to EUI, log in, then view source, then copy token from browser
    # TOKEN = sys.argv[1] if len(sys.argv) > 1 else None 
    TOKEN = 'AgDEMjnKrM2XbBW14KPrVeO6K0yVmy37GPz92QWgG7J9qG6P5ecaCgvKpPDjdMw1Em6wrVqONbrYDQFwgQl7ntGM2k'
    HBM_LINK = 'https://hubmap-link-api.herokuapp.com/hubmap-datasets?format=jsonld'
    if TOKEN:
        HBM_LINK += '&token=' + TOKEN

    # first, let's get the most recent data
    with urllib.request.urlopen(HBM_LINK) as url:
        data = json.loads(url.read().decode())
        # print(data)
        counter = 0
        for item in data['@graph']:
            for sample in item['samples']:
                counter = counter + 1
                date_time_str = sample['rui_location']['creation_date']
                if len(date_time_str) > 12:
                    print(date_time_str)
                    # Need to parse string as datetime object to detemine if in contest range
                    # print(datetime.strptime(date_time_str, '%m/%d/%y %I:%M:%S %p'))
                
        print(counter)


main()
