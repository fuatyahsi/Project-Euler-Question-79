import os

print(os.getcwd())
os.chdir("/users/Fuat.yahsi/Desktop")
print(os.getcwd())

with open("euler79.txt", "r", encoding="utf = 8") as d:
    keylogs = set(d.read().splitlines())  # contents of given file, 3-digit numbers
keys_set = set()
for i in keylogs:
    for j in i: keys_set.add(j)  # numbers in password -unordered,uniqe-


def after_key(x):
    after_x = set()
    for i in keylogs:
        for j in i:
            if x == j:
                for k in i[i.index(j) + 1::]: after_x.add(k)
    return x, after_x, len(after_x)


explanation = [after_key(i) for i in keys_set]
for i in explanation:
    print(
        "The set of number/numbers that comes after {} is {}. This set has {} number/numbers".format(i[0], i[1], i[2]))
len_after_key_list = [after_key(i)[2] for i in keys_set]
len_after_key_list.sort(reverse=True)
solution = ""
for i in len_after_key_list:
   for j in keys_set:
       if after_key(j)[2] == i:
           solution+=j
print(solution)
