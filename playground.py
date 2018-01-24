path = "/Users/shine/Desktop/"

# get the input file
input_file_name = '属性分布.json'
input_file = open(path + input_file_name, "r")

lines = input_file.readlines()
for line in lines:
    if 'id' in line:
        kws = line.split(',')
        i = 0
        for i in range(0, kws.__len__()-1):
            kw = kws[i]
            if 'id' not in kw and "name" not in kw and "\n" not in kw:
                content = kw.split(':')
                content[1] = content[1].replace("\"", "")
                kw = ":".join(content)
                # print(":".join(content))
            kws[i] = kw
            # print(kw)

        print(",".join(kws))

                    # print(attr.split(':')[1].replace("\"", ""))