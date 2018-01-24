path = '/Users/shine/Desktop/'

# get the input file
input_file_name = 'baozun_shop_name.txt'
input_file = open(path + input_file_name, "r")

# write result to output_file
output_file_name = 'shoplist.txt'
output_file = open(path + output_file_name, 'w')

lines = input_file.readlines()
for line in lines:
    if line.__len__() > 1:
        result = ''
        if \
            '(k)' in line or \
            '（K）' in line or \
            '（k）' in line or \
            '(K)' in line:
            result = 'Not Found'
        elif '(同' in line:
            result = 'repetitive'
        elif '(改名为' in line:
            result = line[line.find('(')+4:-2]
        else:
            result = line[0:-1]

        print(result)
        output_file.write(result + '\n')

output_file.close()