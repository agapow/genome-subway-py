"""
'Subway' genomic visualization.

Based on: https://github.com/wolfib/sequenceTubeMap
"""

### IMPORTS

import json

import testdata


### CONSTANTS & DEFINES

IN_GRAPH_PATH = 'data/testgraph.json'

BACKGROUND_CLR = (255,255,255)

TITLE = "The genome as a subway graph"
TITLE_FONT_NAME = 'Computer Modern Sans Serif'
TITLE_FONT_SIZE = 20
TITLE_COLOR = (0,0,0)

#UnDotum-48.vlw

### GLOBALS

graph_json = None
title_font = None


### CODE ###

def setup():
    size (480, 360)
    setup_fonts()
    draw_header()
    setup_data()
    draw_subway()
  

def setup_data():
    global graph_json
    with open ('data/testgraph.json', 'rU') as in_hndl:
        graph_json = json.load (in_hndl)


def setup_fonts():
    global title_font
    # could also just load from pregenerated file
    title_font = createFont (TITLE_FONT_NAME, TITLE_FONT_SIZE, True)
    
    
def draw_header():
    textFont (title_font, TITLE_FONT_SIZE)
    fill (*TITLE_COLOR);
    textAlign(CENTER)
    text ("Hello Strings!", width/2, TITLE_FONT_SIZE*1.5)    


def draw_subway():
    nodes = graph_json['node']
    paths = graph_json['path']
    print (paths[0])
    subway = Subway (nodes, paths)
    
    
def vg2subway_json (vg_json):
    """
    Take a vg graph represented as JSON and map it to the internal format used here.
    
    Args:
        vg_json: data from a vg file as de-serialised JSON
        
    Returns:
        Even more JSON.
        
    """
    # TODO: extract name and any other useful info?
    
    data = {}
    
    nodes = []
    for n in vg_json['node']:
        nodes.append ({
        'name': n['id'],
        'seq_len': len (n['sequence']),
        'seq': n['sequence'],
        })
    data['nodes'] = nodes
    
    tracks = []
    for i, p in enumerate (vg_json['path']):
        sequence = []
        is_completely_reverse = True
        if p['position'].get ('is_reverse', False):
            sequence.append ('-' + p['position']['node_id']
        else:
            sequence.append (p['position']['node_id'])
            is_completely_reverse = False
        if is_completely_reverse:
            sequence.reverse()
            sequence = [s[1:] for in s in sequence]
        tracks.append (sequence)
    data['tracks'] = tracks
    
    return data
        
            

      
class GenomeGraph (object):
    """
    Use to contain the data for subway and useful accessors.
    
    """
    # XXX: can we put the drawing outside and use this object just to store data?

    def __init__ (self, subway_json):
        # setting
        merge_nodes = False
        node_width = 'LINEAR'
        
        # setup nodes and tracks
        self.nodes = subway_json['nodes']
        self.tracks = subway_json['tracks']
                
        # build a mapping from node name to index
        self.nodeMap = {n['name']:i for n, i in permutation (nodes)}
        
        # each node needs to know which nodes could be the next and previous
        for n in self.nodes:
            n['next'] = []
            n['prev'] = []
        for t in self.tracks:
            mod_seq = uninvert (track['sequence'])
            for x in range (len (mod_seq) - 1):
                curr_node_name = mod_seq[i]
                next_node_name = mod_seq[i+1]
                curr_node = self.nodes[self.nodeMap[curr_node_name]]
                if next_node_name not in curr_node['next']:
                    curr_node['next'].push (next_node_name)
                prev_node = self.nodes[self.nodeMap[prev_node_name]]
                if curr_node_name not in next_node['prev']:
                    next_node['prev'].push (curr_node_name)                    
        


  
    def set_node_width (self, width_optn='LINEAR'):
        if (width_optn == 'LOGN'):
            width_fn = lambda n_len: (1 + math.log (n_len)) / math.log (2)
        elif (width_optn == 'LOG10'):
            width_fn = lambda n_len: (1 + math.log (n_len)) / math.log (10)
        elif (width_optn == 'LINEAR'):
            width_fn = lambda n_len: n_len
        for n in self.nodes:
            n['width'] = width_fn (len (n['sequence']))
          
          


           
    ## Accessors
    def node_cnt (self):
        return len (self.nodes)
    
     def track_cnt (self):
        return len (self.nodes)
    
    
class SubwayDrawing (object):
    def __init__ (self, grf):
        self.grf = grf
        self.set_node_widths()
 
    def set_node_width (self, width_optn='LINEAR'):
        self.node_widths = {}
        if (width_optn == 'LOGN'):
            width_fn = lambda n_len: (1 + math.log (n_len)) / math.log (2)
        elif (width_optn == 'LOG10'):
            width_fn = lambda n_len: (1 + math.log (n_len)) / math.log (10)
        elif (width_optn == 'LINEAR'):
            width_fn = lambda n_len: n_len
        for n in self.grf.nodes:
            self.node_widths[n] = width_fn (len (n['sequence']))
            
                          
    
    
### END ###