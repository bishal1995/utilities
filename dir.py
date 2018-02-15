'''
Created by : Bishal Paul
National institute of Technology Silchar
'''

import os
parent_dir = "/home/daemon32/Desktop/gait/DatasetB"
file_name = 'structure2.txt'
with open(file_name) as f:
	lines = [line.rstrip('\n') for line in open(file_name)]
paths = []
for line in lines:
        paths.append(line.lstrip('.'))
actual_paths = []
for path in paths:
        actual_paths.append(parent_dir + path)

actual_path_details = []
for actual_path in actual_paths:
        count = 0
        files = os.listdir(actual_path.rstrip('\n'))
        for file in files:
                if(file[-3:] == 'png'):
                        count = count + 1
        actual_path_details.append(actual_path.rstrip('\n') + " : " + str(count))

output_file = open('output.txt','w')
for details in actual_path_details:
        output_file.write(details + '\n')
output_file.close()
