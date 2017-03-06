"""
Some simple data for tetsing the visualisation.
"""

### CONSTANTS & DEFINES

inputNodes = [
    {'name': "A", width: 1, 'seq': "A"},
    {'name': "B", width: 2, 'seq': "AA"},
    {'name': "C", width: 1, 'seq': "T"},
    {'name': "D", width: 3, 'seq': "GGG"},
    {'name': "E", width: 1, 'seq': "A"},
    {'name': "F", width: 1, 'seq': "G"},
    {'name': "G", width: 3, 'seq': "ATG"},
    {'name': "H", width: 1, 'seq': "T"},
    {'name': "I", width: 1, 'seq': "C"},
    {'name': "J", width: 3, 'seq': "TAA"},
    {'name': "K", width: 1, 'seq': "C"},
    {'name': "L", width: 1, 'seq': "G"},
    {'name': "M", width: 1, 'seq': "C"},
    {'name': "N", width: 1, 'seq': "A"},
    {'name': "O", width: 1, 'seq': "C"},
    {'name': "P", width: 2, 'seq': "AA"},
    {'name': "Q", width: 1, 'seq': "T"},
    {'name': "R", width: 1, 'seq': "C"},
    {'name': "S", width: 2, 'seq': "GA"},
    {'name': "T", width: 3, 'seq': "GTT"},
    {'name': "U", width: 1, 'seq': "A"},
    {'name': "V", width: 1, 'seq': "G"},
    {'name': "W", width: 8, 'seq': "TTGTCTCT"},
    {'name': "X", width: 1, 'seq': "T"},
    {'name': "Y", width: 1, 'seq': "C"},
    {'name': "Z", width: 1, 'seq': "A"},
    {'name': "AA", width: 1, 'seq': "C"},
    {'name': "AB", width: 1, 'seq': "T"},
    {'name': "AC", width: 1, 'seq': "G"},
    {'name': "AD", width: 1, 'seq': "A"},
    {'name': "AE", width: 1, 'seq': "G"},
    {'name': "AF", width: 1, 'seq': "T"},
    {'name': "AG", width: 3, 'seq': "GTG"}
]

inputTracks1 = [
    {id: 0, 'sequence': ["A", "B", "D", "E", "G", "H", "J", "K", "M", "N", "P", "Q", "S", "U", "W", "X", "Z", "AA", "AE", "AG"]},
    {id: 1, 'sequence': ["A", "B", "D", "E", "G", "H", "J", "K", "M", "N", "Q", "S", "U", "AA", "AE", "AG"]},
    {id: 2, 'sequence': ["A", "B", "D", "E", "G", "H", "J", "K", "M", "N", "P", "Q", "S", "V", "W", "X", "Z", "AB", "AE", "AG"]},
    {id: 3, 'sequence': ["B", "C", "D", "E", "G", "H", "J", "L", "M", "N", "P", "R", "S", "U", "W", "Y", "Z", "AC", "AF", "AG"]},
    {id: 4, 'sequence': ["B", "D", "F", "G", "I", "J", "L", "M", "O", "P", "Q", "S", "T", "V", "W", "Y", "Z", "AD", "AF", "AG"]}
]

inputTracks2 = [
    {id: 0, 'sequence': ["A", "B", "D", "E", "G", "H", "J", "K", "M", "N", "P", "Q", "S", "U", "W", "X", "Z", "AA", "AE", "AG"]},
    {id: 1, 'sequence': ["A", "B", "D", "E", "G", "H", "J", "K", "M", "N", "Q", "S", "U", "AA", "AE", "AG"]},
    {id: 2, 'sequence': ["A", "B", "D", "F", "-H", "-G", "-E", "J", "K", "M", "N", "P", "Q", "S", "AB", "V", "W", "X", "-AE", "-AA", "-Z", "AG"]},
    {id: 3, 'sequence': ["B", "C", "D", "E", "G", "H", "J", "L", "-P", "-N", "-M", "R", "S", "U", "W", "Y", "Z", "AC", "AF", "AG"]},
    {id: 4, 'sequence': ["B", "D", "F", "-J", "-I", "-G", "L", "M", "O", "P", "Q", "S", "T", "V", "W", "Y", "Z", "AD", "AF", "AG"]}
]

inputTracks3 = [
    {id: 0, 'sequence': ["A", "B", "D", "E", "G", "H", "J", "K", "M", "N", "P", "Q", "S", "U", "W", "X", "Z", "AA", "AE", "AG"]},
    {id: 1, 'sequence': ["A", "B", "D", "E", "G", "H", "J", "K", "M", "N", "Q", "S", "U", "AA", "AE", "AG"]},
    {id: 2, 'sequence': ["A", "B", "D", "-H", "G", "-E", "J", "K", "M", "N", "P", "Q", "S", "AB", "V", "W", "X", "-AE", "-AA", "-Z", "AG"]},
    {id: 3, 'sequence': ["B", "C", "D", "E", "G", "H", "J", "L", "-P", "-N", "-M", "R", "S", "U", "W", "Y", "Z", "AC", "AF", "AG"]},
    {id: 4, 'sequence': ["B", "D", "F", "G", "I", "J", "L", "M", "O", "P", "Q", "S", "T", "V", "W", "Y", "Z", "AD", "AF", "AG"]}
]

inputTracks4 = [
    {id: 0, 'sequence': ["A", "B", "D", "E", "G", "H", "J", "K", "M", "N", "P", "Q", "S", "U", "W", "X", "Z", "AA", "AE", "AG"]},
    {id: 1, 'sequence': ["A", "B", "D", "E", "G", "H", "J", "K", "M", "J", "N", "Q", "S", "U", "AA", "AE", "AG"]},
    {id: 2, 'sequence': ["A", "B", "D", "E", "G", "H", "J", "K", "M", "N", "P", "Q", "S", "V", "W", "X", "Z", "AB", "AE", "AG"]},
    {id: 3, 'sequence': ["B", "C", "D", "E", "D", "E", "G", "H", "J", "L", "M", "N", "P", "R", "S", "U", "W", "Y", "Z", "AC", "AF", "AG"]},
    {id: 4, 'sequence': ["B", "D", "F", "G", "I", "J", "L", "M", "O", "P", "Q", "S", "T", "V", "W", "Y", "Z", "AD", "AF", "AG"]}
]

inputTracks5 = [
    {id: 0, 'sequence': ["A", "B", "D", "E", "G", "H", "J", "K", "M", "N", "P", "Q", "S", "U", "W", "X", "Z", "AA", "AE", "AG"]},
    {id: 1, 'sequence': ["A", "B", "D", "E", "G", "H", "J", "Q", "K", "M", "N", "S", "U", "AA", "AE", "AG"]},
    {id: 2, 'sequence': ["A", "B", "D", "E", "G", "H", "J", "K", "M", "N", "P", "Q", "S", "V", "W", "X", "Z", "AB", "AE", "AG"]},
    {id: 3, 'sequence': ["B", "C", "D", "H", "E", "G", "J", "L", "M", "N", "P", "R", "S", "U", "W", "Y", "Z", "AC", "AF", "AG"]},
    {id: 4, 'sequence': ["B", "D", "F", "G", "I", "J", "L", "M", "O", "P", "Q", "S", "T", "V", "W", "Y", "Z", "AD", "AF", "AG"]}
  ]

DATASET_1 = {
'nodes': inputNodes,
'tracks': inputTracks1,
}

DATASET_2 = {
'nodes': inputNodes,
'tracks': inputTracks2,
}

DATASET_3 = {
'nodes': inputNodes,
'tracks': inputTracks3,
}

DATASET_4 = {
'nodes': inputNodes,
'tracks': inputTracks4,
}

DATASET_5 = {
'nodes': inputNodes,
'tracks': inputTracks5,
}


### END ###
