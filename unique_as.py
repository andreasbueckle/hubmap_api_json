for_vu = [

   [
        "http://purl.obolibrary.org/obo/UBERON_0002015",
        "http://purl.obolibrary.org/obo/UBERON_0000362",
        "http://purl.obolibrary.org/obo/UBERON_0004200",
        "http://purl.obolibrary.org/obo/UBERON_0001225",
        "http://purl.obolibrary.org/obo/UBERON_0001284",
        "http://purl.obolibrary.org/obo/UBERON_0002189"
    ],

   [
        "http://purl.obolibrary.org/obo/UBERON_0002015",
        "http://purl.obolibrary.org/obo/UBERON_0000362",
        "http://purl.obolibrary.org/obo/UBERON_0004200",
        "http://purl.obolibrary.org/obo/UBERON_0001225",
        "http://purl.obolibrary.org/obo/UBERON_0001284",
        "http://purl.obolibrary.org/obo/UBERON_0002189",
        "http://purl.obolibrary.org/obo/UBERON_0001222"
    ],

 [
        "http://purl.obolibrary.org/obo/UBERON_0002015",
        "http://purl.obolibrary.org/obo/UBERON_0000362",
        "http://purl.obolibrary.org/obo/UBERON_0004200",
        "http://purl.obolibrary.org/obo/UBERON_0001225",
        "http://purl.obolibrary.org/obo/UBERON_0001284",
        "http://purl.obolibrary.org/obo/UBERON_0002189",
        "http://purl.obolibrary.org/obo/UBERON_0001222"
    ],

 [
        "http://purl.obolibrary.org/obo/UBERON_0002015",
        "http://purl.obolibrary.org/obo/UBERON_0000362",
        "http://purl.obolibrary.org/obo/UBERON_0004200",
        "http://purl.obolibrary.org/obo/UBERON_0001225",
        "http://purl.obolibrary.org/obo/UBERON_0001284",
        "http://purl.obolibrary.org/obo/UBERON_0002189",
        "http://purl.obolibrary.org/obo/UBERON_0001222"
    ],

 [
        "http://purl.obolibrary.org/obo/UBERON_0002015",
        "http://purl.obolibrary.org/obo/UBERON_0000362",
        "http://purl.obolibrary.org/obo/UBERON_0004200",
        "http://purl.obolibrary.org/obo/UBERON_0001225",
        "http://purl.obolibrary.org/obo/UBERON_0001284",
        "http://purl.obolibrary.org/obo/UBERON_0002189",
        "http://purl.obolibrary.org/obo/UBERON_0001222"
    ],

  [
        "http://purl.obolibrary.org/obo/UBERON_0002015",
        "http://purl.obolibrary.org/obo/UBERON_0000362",
        "http://purl.obolibrary.org/obo/UBERON_0004200",
        "http://purl.obolibrary.org/obo/UBERON_0001225",
        "http://purl.obolibrary.org/obo/UBERON_0001284",
        "http://purl.obolibrary.org/obo/UBERON_0002189",
        "http://purl.obolibrary.org/obo/UBERON_0001222"
    ],

[
        "http://purl.obolibrary.org/obo/UBERON_0002015",
        "http://purl.obolibrary.org/obo/UBERON_0000362",
        "http://purl.obolibrary.org/obo/UBERON_0004200",
        "http://purl.obolibrary.org/obo/UBERON_0001225",
        "http://purl.obolibrary.org/obo/UBERON_0001284",
        "http://purl.obolibrary.org/obo/UBERON_0002189",
        "http://purl.obolibrary.org/obo/UBERON_0001222",
        "http://purl.obolibrary.org/obo/UBERON_0001228",
        "http://purl.obolibrary.org/obo/UBERON_0006517",
        "http://purl.obolibrary.org/obo/UBERON_0001227"
    ],

]

counters = {}
flattened = []
for i in range(0, len(for_vu)):
    for j in range(0, len(for_vu[i])):
        flattened.append(for_vu[i][j])
# finally, we count the ccf_annotations and print the result to the console
for item in flattened:
    if item not in counters:
        counters[item] = 0
    if item in counters:
        counters[item] = counters[item] + 1
print(flattened)
print(len(flattened))
print()
print(counters)

# print(for_vu)
# print(len(for_vu))
