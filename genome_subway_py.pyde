"""
'Subway' genomic visualization.

Based on: https://github.com/wolfib/sequenceTubeMap
"""

### IMPORTS

import json

import testdata
import consts


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
    frame.setResizable (True);
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
    subway = GenomeGraph (subway_json=testdata.DATASET_1)
            

      
class GenomeGraph (object):
    """
    Use to contain the data for subway and useful accessors.
    
    """

    def __init__ (self, subway_json=None, vg_json=None):
        """
        
        Can be inited empty, from simplified (internal) json or variant graph
        json.
        """
        ## Preconditions:
        assert not (subway_json and vg_json), \
           "cannot initialise with both subway and vg json"
        
        # setting
        merge_nodes = False
        node_width = 'LINEAR' # XXX: move?
            
        # init nodes and tracks, read data if supplied
        if vg_json:
            subway_json = self.vg2subway_json (jg_json)
        if subway_json:
            self.nodes = subway_json['nodes']
            self.tracks = subway_json['tracks']
        else:
            self.nodes = []
            self.tracks = []
            
        # build a mapping from node name to index
        print (self.nodes)
        self.node_map = {n['name']:i for i, n in enumerate (self.nodes)}
        
        # each node needs to know which nodes could be the next and previous
        for n in self.nodes:
            n['next'] = []
            n['prev'] = []
        for t in self.tracks:
            mod_seq = uninvert (track['sequence'])
            for x in range (len (mod_seq) - 1):
                curr_node_name = mod_seq[i]
                next_node_name = mod_seq[i+1]
                curr_node = self.nodes[self.node_map[curr_node_name]]
                if next_node_name not in curr_node['next']:
                    curr_node['next'].push (next_node_name)
                prev_node = self.nodes[self.node_map[prev_node_name]]
                if curr_node_name not in next_node['prev']:
                    next_node['prev'].push (curr_node_name)                    

    def vg2subway_json (self, vg_json):
        """
        Take a vg graph represented as JSON and map it to the internal format.
        
        Args:
            vg_json: data from a vg file as de-serialised JSON
            
        Returns:
            Even more JSON.
            
        """
        # TODO: extract name and any other useful info?
        # NOTE: useful place to detail internal json format
        
        data = {}
        
        # the nodes are stored as a list
        # each node has:
        # - a name/id
        # - a string that is the "chunk" that makes up that node
        # - a cached length (not needed?)
        nodes = []
        for n in vg_json['node']:
            nodes.append ({
               'name': n['id'],
               'seq_len': len (n['sequence']),
               'seq': n['sequence'],
            })
        data['nodes'] = nodes
    
        # the tracks are also stored as a list
        # each track has:
        # - an id
        # - a sequence that is a list of the chunks in the track
        # - each chunk may be prefixed with a '-' sign to signify reversal 
        tracks = []
        for i, p in enumerate (vg_json['path']):
            sequence = []
            is_completely_reverse = True
            if p['position'].get ('is_reverse', False):
                sequence.append ('-' + p['position']['node_id'])
            else:
                sequence.append (p['position']['node_id'])
                is_completely_reverse = False
            if is_completely_reverse:
                sequence.reverse()
                sequence = [s[1:] for s in sequence]
            tracks.append (sequence)
        data['tracks'] = tracks
    
        return data

  
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