import urllib.request
import json

def main():
    # first, let's get the most recent data
    with urllib.request.urlopen("https://hubmap-link-api.herokuapp.com/hubmap-datasets?format=jsonld") as url:
        data = json.loads(url.read().decode())

# then, we create an empty array to capture the ccf_annotations AKA anatomical structures our samples are colliding with
# we iterate through the JSON file we received from the API and extract 
# ccf_annotations for the kidney. Finally, we print the result to the console
    all_ccf_annotations = []
    for i in range(0, len(data['@graph'])):
        graph_item = data['@graph'][i]
        for j in range(0, len(graph_item['samples'])):
            sample = graph_item['samples'][j]
            if 'Kidney' in sample['rui_location']['placement']['target']:
                ccf_annotations = sample['rui_location']['ccf_annotations']
                all_ccf_annotations.append(ccf_annotations)
    print(all_ccf_annotations)
    print()

# next, we create a dict to count unique ccf_annotations
# then, we flatten the 2D array we created above into a 1D array
    counters = {}
    flattened = []
    for i in range(0, len(all_ccf_annotations)):
        for j in range(0, len(all_ccf_annotations[i])):
            flattened.append(all_ccf_annotations[i][j])
# finally, we count the ccf_annotations and print the result to the console
    for item in flattened:
        if item not in counters:
            counters[item] = 0
        if item in counters:
            counters[item] = counters[item] + 1
    print(flattened)
    print()
    print(counters)

main()

