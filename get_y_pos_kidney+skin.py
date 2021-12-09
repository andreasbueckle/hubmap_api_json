import json
import urllib.request


def main():
    # To get TOKEN for viewing unpublished data, go to EUI, log in, then view source, then copy token from browser
    # TOKEN = sys.argv[1] if len(sys.argv) > 1 else None
    TOKEN = 'AgvladOG76Kjw5mY3JEGXlbMeMm8yYNayJP4ledKYqoBV5Ob6NuzCMn0JG0J0WoW9pd90en6ag138zs9oeQYJtw57l'
    HBM_LINK = 'https://hubmap-link-api.herokuapp.com/hubmap-datasets?format=jsonld'
    if TOKEN:
        HBM_LINK += '&token=' + TOKEN

    # first, let's get the most recent data
    with urllib.request.urlopen(HBM_LINK) as url:
        data = json.loads(url.read().decode())

        skin_datasets_male = []
        skin_datasets_female = []

        for item in data['@graph']:
            for sample in item['samples']:
                if 'VHMSkin' in sample['rui_location']['placement']['target']:
                    skin_datasets_male.append(
                        (sample['@id'], sample['rui_location']['placement']['y_translation']))
                elif 'VHFSkin' in sample['rui_location']['placement']['target']:
                    skin_datasets_female.append(
                        (sample['@id'], sample['rui_location']['placement']['y_translation']))

        for item in [skin_datasets_male, skin_datasets_female]:
            print(item)



main()
