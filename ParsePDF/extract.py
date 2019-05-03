with open('pdf.txt', 'r') as file:
    str = file.read().replace(" ","").replace("\n\n","\n")

parse = str.split("\n")
position = []

for index in range(0, len(parse)):
    if parse[index] == "Time":
        position.append(index-1)
    if len(position) == 2:
        break

text = parse[position[0]:position[1]]
data = dict()

for index in range(0, len(text)):
    if text[index] == "Time":
        data['Time'] = text[index+1]
    elif text[index] == "Northbound(NB)":
        data['NB'] = text[index+1]
    elif text[index] == "Southbound(SB)":
        data['SB'] = text[index+1]
    elif text[index] == "Total":
        data['Total'] = text[index+1]

