## this file just rasdomized the data in testdata.json and saved it to ex2.5.json

import json
import random
with open('ex2.json') as f:
    data = json.load(f)

#randomly shuffle the data
for n in data:
    random.shuffle(n)

#load the new data into a file names ex2.5.json
with open('ex2.5.json', 'w') as f:
    json.dump(data, f)

##############
# #fnd length of each list in ex2.5.json
# with open('ex2.5.json') as f:
#     data = json.load(f)
# length_of_data = []
# for n in data:
#     length_of_data.append(len(n))

# #find length of each list in testdata.json
# length_of_data_og = []
# with open('testdata.json') as f:
#     data = json.load(f)
# for n in data:
#     length_of_data_og.append(len(n))

# print(length_of_data)
# print(length_of_data_og)

