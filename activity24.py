
cellphone_brands = ["xiaomi", "Iphone", "oppo", "vivo", "huawei", "poco", "samsung"]
                        #0         #1       #2      #3      #4      #5         #6

#DICTIONARY 
#KEY, VALUE
cellphones_d = {"angas":"xiaomi", "lowbat":"Iphone", "Upo":"Oppo", "Vovo":"Vivo", "No Google Chrome":"Huawei", "Pororo":"Poco", "OG":"Samsung"}

print(cellphone_brands[0])

print(cellphones_d["OG"])

#Traversing a dictionary
for x, y in cellphones_d.items():
    print("Key is", x, "--- value is -->", y)