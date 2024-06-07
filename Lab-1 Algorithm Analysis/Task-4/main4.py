infile = open("D:\Alg\Lab-1 Algorithm Analysis\Task-4\input4.txt", 'r')
outfile = open("D:\Alg\Lab-1 Algorithm Analysis\Task-4\output4.txt", 'w')

n = int(infile.readline().strip())
info = []
name = []
time = []

for i in range(n):
    temp = infile.readline().strip()
    info.append(temp)
    name.append(temp.split()[0])
    time.append(temp.split()[-1])

for i in range(len(name)):
    for j in range(len(name)-i-1):
        if name[j] > name[j+1]:
            name[j], name[j+1] = name[j+1], name[j]
            info[j], info[j+1] = info[j+1], info[j]

        if name[j] == name[j+1]:
            if time[j] > time[j+1]:
                time[j], time[j+1] = time[j+1], time[j]
                info[j], info[j+1] = info[j+1], info[j]

for i in range(n):
    outfile.write(f'{info[i]}\n')

infile.close()
outfile.close()