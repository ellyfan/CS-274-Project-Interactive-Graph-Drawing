data = open("metabolic.edgelist.txt", "r")
dotFile = open('metabolic.gv', 'w')

dotFile.write('graph {\n')

for line in data:
    nodes = line.split() # split each line by space
    dotFile.write('    ' + nodes[0] + ' -- ' + nodes[1] + ';\n')

dotFile.write('}')

data.close()
dotFile.close()