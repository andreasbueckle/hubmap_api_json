from datetime import date
import urllib.request
import json
from dateutil import parser
import sys


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
        dates = []
        creators = []
        organs = []
        people = []

        for item in data['@graph']:
            for sample in item['samples']:
          
                # Parse string as datetime object to detemine if in contest range
                as_date_time = parser.parse(sample['rui_location']['creation_date'])      
                if as_date_time > parser.parse('2021-08-30 00:00:00') and as_date_time < parser.parse('2021-10-04 00:00:00'):
                    creator = sample['label'].split(',')[2].strip()
                    dates.append(as_date_time)
                    creators.append(creator)
                    organs.append(sample['rui_location']['placement']['target'])
                    people.append(sample['rui_location']['creator'].strip())
        # print(people)



        winners = []
        for p in people:
            if p.lower() not in winners:
                winners.append(p.lower())
        print(winners)

        #count submission per team
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
        # print("Total #submissions: " + str(total_submissions)) #208

        #Find out on which dates blocks were submitted
        date_counts = {}
        for item in dates:
            as_string = str(item)[0:10]
            if as_string not in date_counts:
                date_counts[as_string] = 1
            else:
               date_counts[as_string] += 1
        # print(date_counts)
        # OUTPOT :{'2021-09-27': 7, '2021-09-28': 8, '2021-09-23': 7, '2021-09-10': 25, '2021-10-02': 110, '2021-10-01': 36, '2021-10-03': 15}
    
    # find out submissions by organ
    organ_counts = {}
    for item in organs:
                if item not in organ_counts:
                    organ_counts[item] = 1
                else:
                    organ_counts[item] += 1
    print(organ_counts)
        # {'http://purl.org/ccf/latest/ccf.owl#VHMLung': 14, 'http://purl.org/ccf/latest/ccf.owl#VHFLung': 8, 'http://purl.org/ccf/latest/ccf.owl#VHMSkin': 7, 'http://purl.org/ccf/latest/ccf.owl#VHFSkin': 5, 'http://purl.org/ccf/latest/ccf.owl#VHFThymus': 11, 'http://purl.org/ccf/latest/ccf.owl#VHFSpleen': 8, 'http://purl.org/ccf/latest/ccf.owl#VHFRightLymphNode': 13,
    #     'http://purl.org/ccf/latest/ccf.owl#VHMRightLymphNode': 49, 'http://purl.org/ccf/latest/ccf.owl#VHMSpleen': 40, 'http://purl.org/ccf/latest/ccf.owl#VHMThymus': 38, 'http://purl.org/ccf/latest/ccf.owl#VHMLeftKidney': 4, 'http://purl.org/ccf/latest/ccf.owl#VHFLeftKidney': 5, 'http://purl.org/ccf/latest/ccf.owl#VHFRightKidney': 4, 'http://purl.org/ccf/latest/ccf.owl#VHMRightKidney': 2}

    #determine unique organ/creator combos (for trophies)
    organ_by_creator = []
    for i in range(0, len(organs)):
        organ_by_creator.append((organs[i], creators[i]))
    # print(organ_by_creator)

    unique = []
    for combo in organ_by_creator:
        if combo not in unique:
            unique.append(combo)
    # print(unique)
    # [('http://purl.org/ccf/latest/ccf.owl#VHMLung', 'TMC-UCSD'), ('http://purl.org/ccf/latest/ccf.owl#VHFLung', 'TMC-UCSD'), ('http://purl.org/ccf/latest/ccf.owl#VHMSkin', 'General Electric RTI'), ('http://purl.org/ccf/latest/ccf.owl#VHFSkin', 'General Electric RTI'), ('http://purl.org/ccf/latest/ccf.owl#VHFThymus', 'TMC-Florida'), ('http://purl.org/ccf/latest/ccf.owl#VHFSpleen', 'TMC-Florida'), ('http://purl.org/ccf/latest/ccf.owl#VHFRightLymphNode', 'TMC-Florida'),
    #  ('http://purl.org/ccf/latest/ccf.owl#VHMRightLymphNode', 'TMC-Florida'), ('http://purl.org/ccf/latest/ccf.owl#VHMSpleen', 'TMC-Florida'), ('http://purl.org/ccf/latest/ccf.owl#VHMThymus', 'TMC-Florida'), ('http://purl.org/ccf/latest/ccf.owl#VHMLeftKidney', 'TMC-UCSD'), ('http://purl.org/ccf/latest/ccf.owl#VHFLeftKidney', 'TMC-UCSD'), ('http://purl.org/ccf/latest/ccf.owl#VHFRightKidney', 'TMC-UCSD'), ('http://purl.org/ccf/latest/ccf.owl#VHMRightKidney', 'TMC-UCSD')]
main()
