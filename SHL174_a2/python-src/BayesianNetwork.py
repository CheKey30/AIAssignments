import numpy as np

def get_p_b_cd(data_add):
    # you need to implement this method.
    p_b_cd = np.zeros((3,3,2),dtype = np.float)
    file = open(data_add)
    line = file.readline().strip()
    line = file.readline().strip()
    # read the data line by line count the number of each situation
    while line:
        id,a,b,c,d,e = line.split("\t")
        line = file.readline().strip()
        p_b_cd[int(b)-1][int(c)-1][int(d)-1]+=1
    cd = np.zeros((3,2),dtype=np.int)

    # calculate the total number of each condition
    for i in range(3):
        for c in range(3):
            for d in range(2):
                cd[c][d] += p_b_cd[i][c][d]
    # calculate the probability under each condition
    for i in range(3):
        for c in range(3):
            for d in range(2):
                p_b_cd[i][c][d] = p_b_cd[i][c][d]/cd[c][d]
    return p_b_cd

# same as the former function
def get_p_a_be(data_add):
    # you need to implement this method.
    p_a_be = np.zeros((2,3,2),dtype = np.float)
    file = open(data_add)
    line = file.readline().strip()
    line = file.readline().strip()
    while line:
        id, a, b, c, d, e = line.split("\t")
        line = file.readline().strip()
        p_a_be[int(a) - 1][int(b) - 1][int(e) - 1] += 1
    be = np.zeros((3,2),dtype=np.int)
    for i in range(2):
        for b in range(3):
            for e in range(2):
                be[b][e] += p_a_be[i][b][e]
    for i in range(2):
        for b in range(3):
            for e in range(2):
                p_a_be[i][b][e] = p_a_be[i][b][e]/be[b][e]
    return p_a_be


# following lines are main function:
data_add = "..\\data\\assign2_BNdata.txt"

# probability distribution of b.
p_b_cd=get_p_b_cd(data_add)
for c in range(3):
    for d in range(2):
        for b in range(3):
            print("P(b=" + str(b+1) + "|c=" + str(c+1) + ",d=" + str(d+1) + ")=" + str(p_b_cd[b][c][d]))


# probability distribution of a.
p_a_be=get_p_a_be(data_add)
for b in range(3):
    for e in range(2):
        for a in range(2):
            print("P(a=" + str(a+1) + "|b=" + str(b+1) + ",e=" + str(e+1) + ")=" + str(p_a_be[a][b][e]))

