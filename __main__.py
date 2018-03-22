from node import Node
import json
import os


nodes = {} #global node dict. contains all nodes loaded in game.

def loadNodeDefs():
    # this will
    # A: read all nodes found in all files in the locs folder,
    # B: take all nodes and put their values into a dictionary,
    # C: create correct connections in every node found in dictionary
    # D: connect nodes to each other globally

    # A
    datas = []  # array of data from files
    jsloads = []  # array of json loaded files
    folder = "./locs/"  # node definition folder
    for fileName in os.listdir(folder):  # for every file name found in the locations folder
        load = open(folder + fileName, "r")
        datas.append(load)  # opens data as read

    # B
    for data in datas:  # for every data found in the opened array
        load = json.load(data)
        jsloads.append(load)
    # C
    for jsload in jsloads:
        for zoneKey in jsload:  # loops through all zoneKeys found
            for nodeKey in jsload[zoneKey]:  # loops through all nodeKeys found
                rawname = zoneKey + "." + nodeKey
                newNode = Node(jsload[zoneKey][nodeKey],zoneKey,rawname)  # passes nodeKey values and rawname to node object
                nodes[newNode.rawname] = newNode  # puts node object in global dict
    #D
    for globalNodeKey in nodes:  # forms all relative node connection
        for directionKey in nodes[globalNodeKey].connected:
            node = nodes[globalNodeKey]  # this iterations node
            targetRaw = node.connected[directionKey]
            if "." not in targetRaw:#target raw is in same world
                targetRaw = node.zonename + "." + targetRaw #updates in world target raw to hit correct global dictionary def

            node.connected[directionKey] = nodes[targetRaw]  # takes direction key W N S etc and sets it's value to the rawname value
def loadNodePlayerdata():
    # this will
    # A: read all nodes found in all files in the saves folder,
    # B: take all nodes and put their values into a dictionary,
    # C: create correct connections in every node found in dictionary
    # D: connect nodes to each other globally

    # A
    datas = []  # array of data from files
    jsloads = []  # array of json loaded files
    folder = "./saves/"  # node definition folder
    for fileName in os.listdir(folder):  # for every file name found in the locations folder
        load = open(folder + fileName, "r")
        datas.append(load)  # opens data as read

    # B
    for data in datas:  # for every data found in the opened array
        load = json.load(data)
        jsloads.append(load)
    # C
    for jsload in jsloads:#loops all loads
        for rawname in jsload["loc"]:
            node = nodes[rawname]
            for propertyKey in jsload["loc"][rawname]:
                node.properties[propertyKey] = jsload["loc"][rawname][propertyKey]





def printAll():
    for globalNodeKey in nodes:
        print globalNodeKey + " is connected to:"
        node = nodes[globalNodeKey]
        for directionKey in node.connected:
            print "     " +directionKey + " " + node.connected[directionKey].rawname
        print "     " + globalNodeKey + " properties:"
        for propertyKey in node.properties:
            # print propertyKey
            print "          " + propertyKey + " " + str(node.properties[propertyKey])

print "load def--------------------------------------------------------------------"
loadNodeDefs()
printAll()
print "load save--------------------------------------------------------------------"
loadNodePlayerdata()
printAll()
