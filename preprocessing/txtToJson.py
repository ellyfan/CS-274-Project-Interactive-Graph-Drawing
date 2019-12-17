import os

data = open("facebook_combined.txt", "r")
jsonFile = open('facebook.json', 'w')

nodesList = []
links = []

for line in data:
    nodes = line.split() # split each line by space
    if (int(nodes[0]) not in nodesList):
        nodesList.append(int(nodes[0]))
    if (int(nodes[1]) not in nodesList):
        nodesList.append(int(nodes[1]))
    links.append({"source": nodes[0], "target": nodes[1]})
nodesList = sorted(nodesList)

jsonFile.write('{\n"nodes": [\n')

# nodes
for node in nodesList[:-1]:
    jsonFile.write('    {"name":' + str(node) + '},\n')
jsonFile.write('    {"name":' + str(nodesList[-1]) + '}\n')
jsonFile.write('],\n"links":[\n')

# links
for link in links[:-1]:
    jsonFile.write('    {"source":' + link["source"] + ',"target":' + link["target"]+ '},\n')
jsonFile.write('    {"source":' + links[-1]["source"] + ',"target":' + links[-1]["target"]+ '}\n')
jsonFile.write(']}\n')

data.close()
jsonFile.close()