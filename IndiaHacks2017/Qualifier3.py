team_len, op_count = raw_input("").split()
team_len = int(team_len)
op_count = int(op_count)
skill_set = raw_input("").split()
skill_set = map(int, skill_set)

def operation1(l, r, k):
    skill_level = 0
    for i in range(l-1, r):
        for j in range(k+1):
            if i-j >= 0:
                skill_level += skill_set[i-j]
    return skill_level

def operation2(i, x):
    skill_set[i-1] = x

def main():
    outputs = []
    for i in range(op_count):
        op_line = raw_input("").split()
        op_line = map(int, op_line)
        if op_line[0] == 1:
            outputs.append(operation1(op_line[1], op_line[2], op_line[3]))
        else:
            operation2(op_line[1], op_line[2])
    for i in outputs:
        print i

main()
