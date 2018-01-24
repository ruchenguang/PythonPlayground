path = "/Users/shine/Desktop/"

# get the input file
input_file_name = 'baozun_shop20180119.json'
input_file = open(path + input_file_name, "r")

# write result to output_file
output_file_name = 'shopinfo.txt'
output_file = open(path + output_file_name, 'w')

lines = input_file.readlines()
for line in lines:
    attrs = line[1:-2].split(", ")

    shopinfo = [4] # save name ,id, local, url to the array

    for attr in attrs:
        [k, v] = attr.split(": ")
        # print("key: " + k[1:-1] + ", value: " + v[1:-1])
        key = k[1:-1]
        value = v[1:-1]
        if key == "shop_name":
            shop_name = value
        if key == "shop_url":
            shop_url = "https:" + value
        if key == "shop_id":
            shop_id = value
        if key == "shop_local":
            shop_local = value
        if key == "baozun_shop_name":
            baozun_shop_name = value

    print(shop_name, shop_id, shop_local, shop_url, sep="\t")
    output_file.write(shop_name + '\t' + shop_id + '\t' + shop_local + '\t' + shop_url + '\t' + baozun_shop_name + '\n')

output_file.close()
