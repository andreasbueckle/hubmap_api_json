import urllib.request
import json
from dateutil import parser

def main():

    # To get TOKEN for viewing unpublished data, go to EUI, log in, then view source, then copy token from browser
    # TOKEN = sys.argv[1] if len(sys.argv) > 1 else None
    TOKEN = ''
    HBM_LINK = 'https://hubmap-link-api.herokuapp.com/hubmap-datasets?format=jsonld'
    if TOKEN:
        HBM_LINK += '&token=' + TOKEN

    # first, let's get the most recent data
    with urllib.request.urlopen(HBM_LINK) as url:
        data = json.loads(url.read().decode())

        counter = 0
        for item in data['@graph']:

            for sample in item['samples']:
                # Parse string as datetime object to detemine if in contest range
                as_date_time = parser.parse(
                    sample['rui_location']['creation_date'])
                if as_date_time > parser.parse('2021-05-01 00:00:00'):
                    counter = counter + 1

        print(f'''
Number of tissue blocks registered since May 1, 2021: {counter}
''')

# Number of tissue blocks registered since May 1, 2021: 271


main()
