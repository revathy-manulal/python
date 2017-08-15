size = int(raw_input(""))
array = raw_input("")
my_dict = {}
for i in range(len(array)):
    if array[i] in my_dict:
        my_dict[array[i]].append(i)
    else:
        my_dict[array[i]] = [i]
#print my_dict

def get_count(index1, index3, indexes):
    #print "indexes: ", indexes
    count = 0
    count2 = 0
    for i in range(len(indexes)):
        if indexes[i] > index1:
            if indexes[i] < index3:
                count += 1
            else:
                count2 = len(indexes) - i
                break
    #print "count: ", count
    #print "count2: ", count2
    return count * count2

final_count = 0
for letter in my_dict.keys():
    #print "letter: ", letter
    letter_indexes = my_dict[letter]
    if len(letter_indexes) == 1:
        pass
    for i in range(0, len(letter_indexes) - 1):
        for j in range(i+1, len(letter_indexes)):
            index1 = letter_indexes[i]
            index3 = letter_indexes[j]
            if index3 - index1 == 1:
                pass
            #print "index1: ", index1
            #print "index3: ", index3
            for k in range(index1+1, index3):
                if array[k] != letter:
                    #print "letterk: ", array[k]
                    k_indexes = my_dict[array[k]]
                    final_count += get_count(index1, index3, k_indexes)
print final_count
