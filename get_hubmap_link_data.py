import urllib.request
import json

"""
Creating a list of objects to hold dimension data for each organ
"""
dimensions = [
    {
        'name': 'RK',
        'x': [],
        'y': [],
        'z': []
    },
    {
        'name': 'LK',
        'x': [],
        'y': [],
        'z': []
    },
    {
        'name': 'SP',
        'x': [],
        'y': [],
        'z': []
    },
    {
        'name': 'Colon',
        'x': [],
        'y': [],
        'z': []
    }
]

"""
This function takes in the data we retrieve from the API endpoint, filters out values for x, y, z-dimensions, and fills them in the dimensions list
"""
def add_to_list_by_organ(d):
    for i in d['@graph']:
        donor = i
        for sample in donor['samples']:
            placement = sample['rui_location']['placement']
            if 'LeftKidney' in placement['target']:
                append_to_list_of_dimension(sample, 0)
            elif 'RightKidney' in placement['target']:
                append_to_list_of_dimension(sample, 1)
            elif 'Spleen' in placement['target']:
                append_to_list_of_dimension(sample, 2)
            elif 'Colon' in placement['target']:
                append_to_list_of_dimension(sample, 3)


def append_to_list_of_dimension(sample, index):
    for letter in ['x', 'y', 'z']:
        dimensions[index][letter].append(
            sample['rui_location'][letter + '_dimension'])


"""
Computes the average size for each dimension and prints the result to the console
"""
def compute_average(dim, dim_name):
    counter = 0
    total = 0
    for num in dim[dim_name]:
        total = total + num
        counter = counter + 1
    print('average size for ' + dim_name + " in " +
          str(dim['name']) + ': ' + str(total/counter))

"""
Retrieves the JSON data from the API endpoint and prints relevant output to the console
"""
def main():
    with urllib.request.urlopen("https://hubmap-link-api.herokuapp.com/hubmap-datasets?format=jsonld") as url:
        data = json.loads(url.read().decode())
        add_to_list_by_organ(data)

        dimension_letters = ('x', 'y', 'z')
        for element in dimensions:
            for item in dimension_letters:
                compute_average(element, item)

    num_blocks_total = 0
    print()
    for element in dimensions:
        num_blocks_organ = len(element['x'])
        num_blocks_total = num_blocks_total + num_blocks_organ

        print("Number of tissue blocks for " +
              element['name'] + ": " + str(num_blocks_organ))
    print()
    print("Total #blocks: " + str(num_blocks_total))


main()


"""
UNUSED:
This function takes JSON data and returns a list of unique strings from the 'target' field. 
Can be used to identify for how many unique organs tissue blocks have been registered. Should be used if code is run on larger number of tissue blocks.
"""
def unique(d):
    all_targets = []
    result = []
    for i in d['@graph']:
        donor = i
        for sample in donor['samples']:
            if sample['rui_location']['placement']['target'] not in result:
                result.append(sample['rui_location']['placement']['target'])
    return result
