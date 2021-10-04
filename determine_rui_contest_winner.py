from datetime import date
import urllib.request
import json
from dateutil import parser

def main():

    # To get TOKEN for viewing unpublished data, go to EUI, log in, then view source, then copy token from browser
    # TOKEN = sys.argv[1] if len(sys.argv) > 1 else None 
    TOKEN = 'AgYq07xYyyl5vX39Q9V1MjpK0JDG4QdreN75EPzynvr0BXlJdqtWCwNmwdPP5bG8J0VlYzNkpDNQvBSVynMaVHE0e8'
    HBM_LINK = 'https://hubmap-link-api.herokuapp.com/hubmap-datasets?format=jsonld'
    if TOKEN:
        HBM_LINK += '&token=' + TOKEN

    # first, let's get the most recent data
    with urllib.request.urlopen(HBM_LINK) as url:
        data = json.loads(url.read().decode())
        dates = []
        creators = []
        for item in data['@graph']:
            for sample in item['samples']:
          
                # Parse string as datetime object to detemine if in contest range
                as_date_time = parser.parse(sample['rui_location']['creation_date'])      
                if as_date_time > parser.parse('2021-08-30 00:00:00'):
                    creator = sample['label'].split(',')[2].strip()
                # print(type(creator))
                    dates.append(as_date_time)
                    creators.append(creator)
        
        #count submission per team with dictionary
        counts = {}
        for item in creators:
            if item not in counts:
                counts[item] = 1
            else:
                counts[item] += 1
        print(counts)
        # OUTPUT: {'TMC-UCSD': 36, 'General Electric RTI': 11, 'TMC-Florida': 158}

        #now, let's count all the submissions in the contest
        total_submissions = 0
        for item in counts:
            total_submissions += counts[item]
        print("Total #submissions: " + str(total_submissions)) #208

        #finally, let find out on which dates blocks were submitted
        date_counts = {}
        for item in dates:
            as_string = str(item)[0:10]
            if as_string not in date_counts:
                date_counts[as_string] = 1
            else:
               date_counts[as_string] += 1
        print(date_counts)
        # OUTPOT :{'2021-09-27': 7, '2021-09-28': 8, '2021-09-23': 7, '2021-09-10': 25, '2021-10-02': 110, '2021-10-01': 36, '2021-10-03': 15}
       
main()
