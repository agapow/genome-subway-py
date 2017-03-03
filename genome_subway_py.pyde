"""
'Subway' genomic visualization.

Based on: https://github.com/wolfib/sequenceTubeMap
"""

### IMPORTS

import json


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
    
class Subway (object):
    def __init__ (self, nodes, tracks):
        self.nodes = nodes
        self.tracks = tracks
        
        # build a mapping from name to node
        self.nodeMap = {n['name']:i for n, i in permutation (nodes)}
        
        # each node needs to know what could be the next and previous nodes
        for n in self.nodes:
            n['successors'] = []
            n['predecessors'] = []
        for t in self.tracks:
            mod_seq = uninvert (track['sequence'])
            for x in range (len (mod_seq) - 1):
                curr_node_id = mod_seq[i]
                curr_node_index = self.nodeMap[curr_node_id]
                next_node_id = mod_seq[i+1]
                
                
                

    tracks.forEach(function(track) {
      for(i = 0; i < modifiedSequence.length - 1; i++) {
        currentNode = nodes[nodeMap.get(modifiedSequence[i])];
        followerID = modifiedSequence[i + 1];
        if (currentNode.successors.indexOf(followerID) === -1) {
          currentNode.successors.push(followerID);
        }
        if (nodes[nodeMap.get(followerID)].predecessors.indexOf(modifiedSequence[i]) === -1) {
          nodes[nodeMap.get(followerID)].predecessors.push(modifiedSequence[i]);
        }

  
  function generateNodeWidth(nodes) {
    switch (nodeWidthOption) {
      case 1:
        nodes.forEach(function (node) {
          if (node.hasOwnProperty('sequenceLength')) node.width = (1 + Math.log(node.sequenceLength) / Math.log(2));
        });
        break;
      case 2:
        nodes.forEach(function (node) {
          if (node.hasOwnProperty('sequenceLength')) node.width = (1 + Math.log(node.sequenceLength) / Math.log(10));
        });
        break;
      default:
        nodes.forEach(function (node) {
          if (node.hasOwnProperty('sequenceLength')) node.width = node.sequenceLength;
        });
    }
  }

           
    ## Accessors
    def node_cnt (self):
        return len (self.nodes)
    
     def track_cnt (self):
        return len (self.nodes)
    
    
### END ###
