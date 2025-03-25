import pandas as pd
import csv 
from ast import literal_eval
import os
import numpy as np

def get_concentration_matrix():
    dfbin = pd.read_csv('../../vcf/Matrix2.csv')
    mixnames = dfbin.columns[1:].values
    molecules = dfbin['Unnamed: 0'].values
    matrix = dfbin.values[0:,1:].astype('float').T
    conc_dict = {}
    bad_odors = []
    with open('../../vcf/concentrations.csv') as conc_f:
        reader = csv.reader(conc_f)
        next(reader, None)
        for row in reader:
            key = row[0]
            inner_dict_keys = literal_eval(row[2])
            inner_dict_values = literal_eval(row[1])
            try:
                conc_dict[key] = dict(zip(inner_dict_keys, inner_dict_values))
            except:
                bad_odors.append(key)

    mix_dict = {}
    x = iter(matrix)
    for name in mixnames:
        mix_dict[name] = next(x)

    # Check if the binary matrix and concentration dictionary are consistent
    # Load a concentration dict
    bad_odors = list(pd.read_csv('../../vcf/bad_odors.csv')['Odor Name'])
    for mix,bin in mix_dict.items():
        if mix in bad_odors:
            continue
        mix_conc_dict = conc_dict[mix]
        if (sum(bin) != len(mix_conc_dict)):
            print(f"{mix} failed with:  {sum(bin)} BINARY ELTS, {len(mix_conc_dict)} CONCENTRATION ELTS")
            mix_molecules = []
            for i in range(1, len(bin)):
                if bin[i] == 1:
                    molecule = molecules[i]
                    mix_molecules.append(molecule)
                    if molecule not in mix_conc_dict:
                        print(f"MISSING: {molecule}")
            for key in mix_conc_dict.keys():
                if key not in mix_molecules:
                    print(f"EXTRA: {key}")

    # find amount of missing concentration data, populate concentration matrix
    concentration_matrix = []
    total_missing = 0 
    total_molecules = 0
    for i in range(len(matrix)): # for each mix
        mix = matrix[i] # binary vector for mix
        mixname = mixnames[i]
        if mixname in bad_odors:
            conc_odor = [(np.nan, np.nan, np.nan) for _ in range(mix.size)]
            concentration_matrix.append(conc_odor)
            continue
        mix_conc_dict = conc_dict[mixname] # mixname : concentration for this mix
        conc_odor = [] # [(value, low, high)] for each possible molecule in mix
        for j in range(mix.size): # for each molecule
            if mix[j] == 1: # if the molecule is in the mix
                total_molecules += 1
                molecule = molecules[j] # molecule name
                concentration = mix_conc_dict[molecule]
                if isinstance(concentration, int): # concentration is -1 (missing value)
                    conc_odor.append((np.nan, np.nan, np.nan))
                    total_missing += 1
                else: # otherwise string with value (xor low/high)
                    concentration = concentration.split('-')
                    if len(concentration) == 1: # single value
                        if '<' in concentration[0]:
                            conc_odor.append((np.nan, 0., float(concentration[0].split('<')[1]))) # btwn 0 and value after <
                        elif concentration[0] == 'trace': # trace = 0. [can change this]
                            conc_odor.append((0., np.nan, np.nan))
                        elif concentration[0].lower() == 'present': # we already knew this, so missing value
                            conc_odor.append((np.nan, np.nan, np.nan))
                            total_missing += 1
                        else:
                            conc_odor.append((float(concentration[0]), np.nan, np.nan)) # otherwise it's a float value
                    elif len(concentration) == 2: # range concentration given
                        start = concentration[0].find('<') + 1 # this < is nonsensical for lower bound (ignore it)
                        low = 0. if concentration[0][start:] == 'trace' else float(concentration[0][start:]) # if "trace" is lower, set to 0.
                        high_start = concentration[1].find('<') + 1 # this < is nonsensical for upper bound (ignore it)
                        conc_odor.append((np.nan, low, float(concentration[1][high_start:])))
                    else:
                        conc_odor.append((np.nan, np.nan, np.nan)) # unparseable concentration values
                        total_missing += 1
            else: # molecule not in mix
                conc_odor.append((0., 0., 0.))
        concentration_matrix.append(conc_odor)
    
    return np.array(concentration_matrix)
