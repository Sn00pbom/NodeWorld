import behavior

class Node(object):


    def __init__(self,nodeDef,zonename,rawname):
        # playerdata fields
        self.properties = {"revealed": False}  # every node must have revealed property, starts at false until changed

        #definition fields
        try:
            self.name = nodeDef["name"]#display name
            self.zonename = zonename
            self.rawname = rawname  # generated from load dic path
            self.behavior = behavior.all[nodeDef["behavior"]]#link to function def in behavior module
            self.connected = nodeDef["connected"]#will be correct, but contain connection rawnames
            try:
                for key in nodeDef["properties"]:
                    self.properties[key] = nodeDef["properties"][key]
            except:
                pass #no properties field found in node definition


        except:
            print "Node definition loading failed... exiting..."
            exit(0)



