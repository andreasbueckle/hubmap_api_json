from ast import Index
import urllib.request
import json
dimensions = [{

    'x': [],
    'y': [],
    'z': []
},
    {

    'x': [],
        'y': [],
        'z': []
}
]


def select_by_organ(d):
    for i in d['@graph']:
        # counter = counter + 1
        donor = i
        # print(donor['samples'])
        for sample in donor['samples']:
            placement = sample['rui_location']['placement']
            if 'LeftKidney' in placement['target']:
                # print(placement['target'])
                print('got one')
                dimensions[0]['x'].append(
                    sample['rui_location']['x_dimension'])
                dimensions[0]['y'].append(
                    sample['rui_location']['y_dimension'])
                dimensions[0]['z'].append(
                    sample['rui_location']['z_dimension'])
            elif 'RightKidney' in placement['target']:
                # print(placement['target'])
                dimensions[1]['x'].append(
                    sample['rui_location']['x_dimension'])
                dimensions[1]['y'].append(
                    sample['rui_location']['y_dimension'])
                dimensions[1]['z'].append(
                    sample['rui_location']['z_dimension'])


def compute_average(dim, dim_name):
    # for organ in dim:
    print(dim[dim_name])
    counter = 0
    total = 0
    for num in dim[dim_name]:
        total = total + num
        counter = counter + 1
    print('result for ' + dim_name + ': ' + str(total/counter))


with urllib.request.urlopen("https://hubmap-link-api.herokuapp.com/hubmap-datasets?format=jsonld") as url:
    data = json.loads(url.read().decode())
    select_by_organ(data)
    # print(dimensions[0]['x'])

    dimension_letters = ('x','y','z')

    for element in dimensions:
        for item in dimension_letters:
            compute_average(element, item)
print(len(dimensions[0]['x']))
print(len(dimensions[1]['x']))
    # compute_average(dimensions[0], 'x')
