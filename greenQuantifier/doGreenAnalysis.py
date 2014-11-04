#!/usr/bin/env python
from argparse import ArgumentParser
from greenanalyser import greenAnalyser

def process():
    parser = ArgumentParser(description = "Generate Green Map and Plot")
    parser.add_argument('--region1', '-r1')
    parser.add_argument('--region2','-r2')
    arguments= parser.parse_args()
    if arguments.region1 and arguments.region2:
        greenAnalyser(arguments.region1,arguments.region2)
    else:
        print 'You need to provide two locations for us to get along.'

if __name__ == "__main__":
    process()