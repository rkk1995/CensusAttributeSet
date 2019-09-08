
import math
import os
import random
import re
import sys

def attributesSet(numberOfAttributes, supportThreshold):
    import csv
    import pandas as pd
    import itertools
    import math

    names = ['age','sex','education','country','race','status','workclass','occupation','hours-per-week','income','capital-gain','capital-loss']
    combinations = []
    final = []
    for comb in itertools.combinations(names,numberOfAttributes):
        combinations.append(list(comb))
    url = "https://s3.amazonaws.com/istreet-questions-us-east-1/443605/census.csv"
    c = pd.read_csv(url)
    c.columns= names
    total = len(c.index)
    required = math.ceil(supportThreshold*total)

    for i in combinations:
        g = c.groupby(i).size().sort_values(ascending=False)
        g
        groups = g[g>required].index
        satisfied = list(groups)
        for j in satisfied:
            final.append(','.join(j))

    return final

if __name__ == '__main__':

    numberOfAttributes = int(3)
    supportThreshold = float(.7)
    result = attributesSet(numberOfAttributes, supportThreshold)

    print(result)
