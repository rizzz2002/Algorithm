file1=open("D:\Alg\Lab-1 Algorithm Analysis\Task-3\input3.txt","r")
file2=open("D:\Alg\Lab-1 Algorithm Analysis\Task-3\output3.txt","w")
length=file1.readline()
IDarr=file1.readline().strip("\n").split(" ")
MarksArr=file1.readline().strip("\n").split(" ")

for i in range (int(length)):
    for j in range (i,int(length)):
        if int(MarksArr[i])<int(MarksArr[j]):
            MarksArr[i],MarksArr[j]=MarksArr[j],MarksArr[i]
            IDarr[i],IDarr[j]=IDarr[j],IDarr[i]
        if int(MarksArr[i])==int(MarksArr[j]):
            if int(IDarr[i])>int(IDarr[j]):
                IDarr[i],IDarr[j]=IDarr[j],IDarr[i]

for z in range (int(length)):
    demoStr="ID: "+IDarr[z]+" Marks: "+MarksArr[z]
    file2.writelines(demoStr)
    file2.writelines("\n")

file1.close()
file2.close()