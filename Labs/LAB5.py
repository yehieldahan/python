dict_names={"yehiel":25000,"avi":50000,"itay":75000,"ortal":100000,"eli":125000}
print(dict_names)
summay=dict_names["yehiel"]+dict_names["eli"]
print("The summary is: " + str(summay))
dict_names.update({"yoel":summay})
print(dict_names)
print("Number of entries: " + str(len(dict_names)))
print("yehiel" in dict_names)
