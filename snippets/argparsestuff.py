import argparse
import sys

parser = argparse.ArgumentParser(description='some test app')
parser.add_argument('-f', '--file', dest='fname', help='file?')
parser.add_argument('-f2', dest='fname2', help='file2?', action='store_true')
parser.add_argument('-l', dest='log', type=argparse.FileType('w'), default=sys.stdout)
parser.add_argument('-s', dest='what', required=True)
args = parser.parse_args()
args.log.write('dddd')
print(args)
