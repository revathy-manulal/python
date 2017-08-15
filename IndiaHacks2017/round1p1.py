line1 = raw_input("").split()
line1 = map(int, line1)
stops = line1[0]
seats = line1[1]
#vacant = seats
total = 0
count = 0
for i in range(stops-1):
    line = raw_input("").split()
    line = map(int, line)
    people_in = line[0]
    people_out = line[1]
    total = total - people_out
    if total < 0:
        total = 0
    total += people_in
    if total >= seats:
        count += 1
print count
