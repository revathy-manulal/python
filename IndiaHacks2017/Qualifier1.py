array_len = int(raw_input(""))
array = raw_input("")
array = array.split()
array = map(int, array)

def main():
    start_index = []
    end_index = []
    one_count = []
    distance = []
    max_count = 0
    for i in range(array_len):
        if array[i] == 1 and (i == 0 or array[i-1] == 0):
            start_index.append(i)
        if (i > 0 and array[i] == 0 and array[i-1] == 1):
            end_index.append(i-1)
        if (i == array_len-1 and array[i] == 1):
            end_index.append(i)
    #print "start_index: ", start_index
    #print "end_index: ", end_index
    for i in range(len(start_index)):
        cluster_count = end_index[i] - start_index[i] + 1
        one_count.append(cluster_count)
        if max_count < cluster_count:
            max_count = cluster_count
        if i == 0:
            distance.append(-1)
        else:
            distance.append(start_index[i] - end_index[i-1] - 1)
    if len(start_index) > 1:
        max_count += 1
    #print "distance: ", distance
    #print "one_count: ", one_count
    #print "max_count: ", max_count
    for i in range(len(distance)):
        if distance [i]== 1:
            count_now = one_count[i] + one_count[i-1]
            if len(start_index) > 2:
                count_now += 1
            if count_now > max_count:
                max_count = count_now
    print max_count

main()
