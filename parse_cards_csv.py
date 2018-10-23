import argparse
import os
import re

parser = argparse.ArgumentParser(description='Extract CRcard from SC .csv files')
parser.add_argument('files', help='.csv file(s)', nargs='+')

args = parser.parse_args()

for file in args.files:
    if file.endswith('.csv'):
        if os.path.exists(file):
            with open(file, 'rb') as f:
                lines = f.read().split('\n')
                for line in lines:
                    trimmedLine = line.replace('"', '') 
                    words = trimmedLine.split(',')
                    name = words[0]
                    rarity = words[5]
                    cost = words[6]
                    readableName = re.sub(r"([^A-Z])([A-Z])", r"\1 \2", name)
                    print("CRCardItem(CR_" + name + ", \"" + readableName + "\", " + cost + ", CR_" + rarity + ", 0)")

        else:
            print('[*] File don\'t exist :/')

    else:

        print('[*] Only .csv are supported !')
