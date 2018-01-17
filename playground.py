path = "/Users/shine/Desktop/baozun_shop.json.json"
shop_file = open(path, "r")

lines = shop_file.readlines()

for line in lines:
    attrs = line[1:-2].split(", ")

    shop_name = ""
    shop_url = ""
    shop_id = ""
    shop_local = ""
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

    print(shop_name, shop_id, shop_local, shop_url, sep="\t")

# print(lines.__len__())
# while line = shop_file.readline():
#     print(shop_file.readline())
