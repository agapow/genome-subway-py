"""
Some simple data for tetsing the visualisation.
"""

### CONSTANTS & DEFINES

## Internal/subway data format
        
# the nodes are stored as a list
# each node has:
# - a name/id
# - a string that is the "chunk" that makes up that node
# - a cached length (not needed?)
#
# the tracks are also stored as a list
# each track has:
# - an id
# - a sequence that is a list of the chunks in the track
# - each chunk may be prefixed with a '-' sign to signify reversal 

inputNodes = [
    {'name': "A", "width": 1, 'seq': "A"},
    {'name': "B", "width": 2, 'seq': "AA"},
    {'name': "C", "width": 1, 'seq': "T"},
    {'name': "D", "width": 3, 'seq': "GGG"},
    {'name': "E", "width": 1, 'seq': "A"},
    {'name': "F", "width": 1, 'seq': "G"},
    {'name': "G", "width": 3, 'seq': "ATG"},
    {'name': "H", "width": 1, 'seq': "T"},
    {'name': "I", "width": 1, 'seq': "C"},
    {'name': "J", "width": 3, 'seq': "TAA"},
    {'name': "K", "width": 1, 'seq': "C"},
    {'name': "L", "width": 1, 'seq': "G"},
    {'name': "M", "width": 1, 'seq': "C"},
    {'name': "N", "width": 1, 'seq': "A"},
    {'name': "O", "width": 1, 'seq': "C"},
    {'name': "P", "width": 2, 'seq': "AA"},
    {'name': "Q", "width": 1, 'seq': "T"},
    {'name': "R", "width": 1, 'seq': "C"},
    {'name': "S", "width": 2, 'seq': "GA"},
    {'name': "T", "width": 3, 'seq': "GTT"},
    {'name': "U", "width": 1, 'seq': "A"},
    {'name': "V", "width": 1, 'seq': "G"},
    {'name': "W", "width": 8, 'seq': "TTGTCTCT"},
    {'name': "X", "width": 1, 'seq': "T"},
    {'name': "Y", "width": 1, 'seq': "C"},
    {'name': "Z", "width": 1, 'seq': "A"},
    {'name': "AA", "width": 1, 'seq': "C"},
    {'name': "AB", "width": 1, 'seq': "T"},
    {'name': "AC", "width": 1, 'seq': "G"},
    {'name': "AD", "width": 1, 'seq': "A"},
    {'name': "AE", "width": 1, 'seq': "G"},
    {'name': "AF", "width": 1, 'seq': "T"},
    {'name': "AG", "width": 3, 'seq': "GTG"}
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


## VG data format
        
# the nodes are stored as a list
# each node has:
# - a name/id
# - a string that is the "chunk" that makes up that node
#
# the tracks are also stored as a list ("path")
# each track has:
# - an name/id
# - a sequence that is a list of the chunks in the track
# - each chunk may be prefixed with a '-' sign to signify reversal 


VG_DATA_1 = {
    "node": [
        {"id": 1, "sequence": "CTTAAAATGAT"},
        {"id": 2, "sequence": "AAGTCCCG"},
        {"id": 3, "sequence": "TTCAAATCTTATTT"}
    ],
    "edge": [
        {"from": 1, "to": 2, "to_end": True},
        {"from": 3, "to": 2, "from_start": True}
    ],
    "path": [
        {
        "name": "ref", 
        "mapping": [
            {
                "rank": 1,
                "edit": [{"from_length": 14, "to_length": 14}],
                "position": {"node_id": 3, "offset": 0, "is_reverse": True}
            },
            {
                "rank": 2,
                "edit": [{"from_length": 8, "to_length": 8}],
                "position": {"node_id": 2, "offset": 0, "is_reverse": False}},
            {
                "rank": 3,
                "edit": [{"from_length": 11, "to_length": 11}],
                "position": {"node_id": 1, "offset": 0, "is_reverse": True}
            }
        ]
        }
    ]
}

VG_DATA_2 = {
    'node': [
    {'id': 6, 'sequence': 'TCAGATTCTCAT'},
    {'id': 8, 'sequence': 'CCCTCCTC'},
    {'id': 10, 'sequence': 'AAGGGCTT'},
    {'id': 11, 'sequence': 'CT'},
    {'id': 30, 'sequence': 'CT'},
    {'id': 12, 'sequence': 'AACTACTC'},
    {'id': 14, 'sequence': 'CACATCAA'},
    {'id': 16, 'sequence': 'AGCTA'},
    {'id': 17, 'sequence': 'C'},
    {'id': 26, 'sequence': 'G'},
    {'id': 28, 'sequence': 'GACTAAGG'},
    {'id': 29, 'sequence': 'ACAAAGGTGCGGGGAG'},
    {'id': 4, 'sequence': 'T'},
    {'id': 18, 'sequence': 'C'},
    {'id': 20, 'sequence': 'C'},
    {'id': 22, 'sequence': 'AGGCCA'},
    {'id': 24, 'sequence': 'TTTTAAGT'},
    {'id': 25, 'sequence': 'TTCCTG'},
    ], 
    'edge': [
    {'from': 6, 'to': 8},
    {'from': 8, 'to': 10},
    {'from': 10, 'to': 11},
    {'from': 10, 'to': 30},
    {'from': 11, 'to': 12},
    {'from': 11, 'to': 26},
    {'from': 12, 'from_start': True, 'to': 17},
    {'from': 12, 'to': 14},
    {'from': 14, 'to': 16},
    {'from': 16, 'to': 17},
    {'from': 17, 'to': 18},
    {'from': 30, 'to': 17, 'to_end': True},
    {'from': 26, 'to': 28},
    {'from': 28, 'to': 29},
    {'from': 25, 'to': 4},
    {'from': 4, 'to': 26},
    {'from': 18, 'to': 20},
    {'from': 18, 'to': 22},
    {'from': 20, 'to': 22},
    {'from': 22, 'to': 24},
    {'from': 24, 'to': 25},
    ],
    'path': [
       {
           'name': 's1',
           'mapping': [
    {'rank': 1, 'position': {'node_id': 6},
     'edit': [{'from_length': 12, 'to_length': 12}]},
    {'rank': 2, 'position': {'node_id': 8}, 'edit': [{'from_length': 8,
     'to_length': 8}]},
    {'rank': 3, 'position': {'node_id': 10},
     'edit': [{'from_length': 8, 'to_length': 8}]},
    {'rank': 4, 'position': {'node_id': 11},
     'edit': [{'from_length': 2, 'to_length': 2}]},
    {'rank': 5, 'position': {'node_id': 12},
     'edit': [{'from_length': 8, 'to_length': 8}]},
    {'rank': 6, 'position': {'node_id': 14},
     'edit': [{'from_length': 8, 'to_length': 8}]},
    {'rank': 7, 'position': {'node_id': 16},
     'edit': [{'from_length': 5, 'to_length': 5}]},
    {'rank': 8, 'position': {'node_id': 17},
     'edit': [{'from_length': 1, 'to_length': 1}]},
    {'rank': 9, 'position': {'node_id': 18},
     'edit': [{'from_length': 1, 'to_length': 1}]},
    {'rank': 10, 'position': {'node_id': 20},
     'edit': [{'from_length': 1, 'to_length': 1}]},
    {'rank': 11, 'position': {'node_id': 22},
     'edit': [{'from_length': 6, 'to_length': 6}]},
    {'rank': 12, 'position': {'node_id': 24},
     'edit': [{'from_length': 8, 'to_length': 8}]},
    {'rank': 13, 'position': {'node_id': 25},
     'edit': [{'from_length': 6, 'to_length': 6}]},
    {'rank': 14, 'position': {'node_id': 4},
     'edit': [{'from_length': 1, 'to_length': 1}]},
    {'rank': 15, 'position': {'node_id': 26},
     'edit': [{'from_length': 1, 'to_length': 1}]},
    {'rank': 16, 'position': {'node_id': 28},
     'edit': [{'from_length': 8, 'to_length': 8}]},
    {'rank': 17, 'position': {'node_id': 29},
     'edit': [{'from_length': 16, 'to_length': 16}]},
    ]},
        {
            'name': 's2', 'mapping': [
    {'rank': 1, 'position': {'node_id': 6},
     'edit': [{'from_length': 12, 'to_length': 12}]},
    {'rank': 2, 'position': {'node_id': 8}, 'edit': [{'from_length': 8,
     'to_length': 8}]},
    {'rank': 3, 'position': {'node_id': 10},
     'edit': [{'from_length': 8, 'to_length': 8}]},
    {'rank': 4, 'position': {'node_id': 11},
     'edit': [{'from_length': 2, 'to_length': 2}]},
    {'rank': 5, 'position': {'node_id': 26},
     'edit': [{'from_length': 1, 'to_length': 1}]},
    {'rank': 6, 'position': {'node_id': 28},
     'edit': [{'from_length': 8, 'to_length': 8}]},
    {'rank': 7, 'position': {'node_id': 29},
     'edit': [{'from_length': 16, 'to_length': 16}]},
    ]}]}



### END ###