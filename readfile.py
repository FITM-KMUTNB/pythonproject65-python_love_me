dic = {}
dicbod = {}
hilow = [0,1,2,3,4,5,6,7,8,9,10,
        11,12,13,14,15,16,17,18,
        19,20,21,22,23,24,25,26,
        27,28,29,30,31,32,33,34,
        35,36,37,38,39,40,41,42,
        43,44,45,46,47,48,49,50]
username = 'Test'
userscore = '11'
def write():
    read()
    filew = open('diction.txt','w')
    for name,score in dic.items():
        filew.write(name)
        filew.write(' ')
        filew.write(score+'\n')
    filew.close()
def read():
    filer = open('diction.txt','r')
    line = filer.readline().rstrip('\n')
    while line != '':
        name,score = line.split()
        dic[name] = score
        line = filer.readline().rstrip('\n')
    filer.close()
def updic():
    dic[username] = userscore
def save():
    read()
    updic()
    write()
def scoreboard():
    read()
    nhilow = len(hilow)
    nhilow = nhilow - 1
    while nhilow >= 0: 
        for name, score in dic.items():
            score = int(score)
            if score == hilow[nhilow]:
                print(name,(hilow[nhilow]))
                dicbod[name] = score
        nhilow -= 1