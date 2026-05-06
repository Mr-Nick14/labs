with open('2.1.6/20.csv', 'r') as file:
    lines = file.readlines()

with open('2.1.6/20.csv', 'w') as file:
    for line in lines:
        line = line.rstrip().replace(' ', ',')
        line = line.rstrip().replace('	', ',')
        line = line.rstrip().replace('	', ',')
        file.write(line + '\n')