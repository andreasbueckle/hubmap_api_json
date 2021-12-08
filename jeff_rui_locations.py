import urllib.request
import json


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
        num_donors = 0
        num_blocks = 0
        jsons = []
        ids = set()
        for donor in data['@graph']:
            if 'provider_name' in donor:
                # print(donor['provider_name'])
                if "Vanderbilt" in donor['provider_name']:
                    num_donors += 1
                    for sample in donor['samples']:
                        rui_location = sample['rui_location']
                        ids.add(rui_location['@id'])
                        organ = sample['rui_location']['placement']['target']
                        if "Kidney" in organ or "kidney" in organ:
                            num_blocks += 1
                            jsons.append(rui_location)
        print(jsons)
                        # print(organ)

    print(f'''
num_donors: {num_donors}
num_blocks: {num_blocks}
len(jsons): {len(jsons)}
    ''')


main()
