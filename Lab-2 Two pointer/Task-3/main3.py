file1=open("D:\Alg\Lab-2 Two pointer\Task-3\input3.txt","r")
file2=open("D:\Alg\Lab-2 Two pointer\Task-3\output3.txt","w")
length=file1.readline().strip("\n")
lst=[]
for y in range (int(length)):
    arr=file1.readline().strip("\n").split(" ")
    lst.append(arr)

for t in range (int(length)):
    flag1=False
    main1=lst[t]
    index=t+1
    if t==((int(length))-1):
        break
    for u in range (t+1,int(length)):
        if int(main1[0])==int(lst[u][0]):
            if (int(main1[1])-int(main1[0]))>(int(lst[u][1])-int(lst[u][0])):
                main1=lst[u]
                index=u
                flag1=True
        if int(main1[0])>int(lst[u][0]):
            main1=lst[u]
            index=u
            flag1=True
    if flag1:
        lst[t],lst[index]=lst[index],lst[t]


finalLst=[]
count=0
for i in range (int(length)):
    flag=True
    main=lst[i]
    fixedMain=lst[i]
    for z in range (int(length)):
        if main == lst[z] or  main in finalLst:
            continue
        if (len(finalLst))!=0 and int(finalLst[len(finalLst)-1][1])>int(main[0]):
            flag=False
            break
        temp=lst[z]
        if (int(fixedMain[0])==int(temp[0]) or int(fixedMain[0])<int(temp[0])) and (int(temp[0])<int(fixedMain[1])):
            sizeMain=int(main[1])-int(main[0])
            sizetemp=int(temp[1])-int(temp[0])
            if sizeMain>sizetemp:
                main=temp
    if flag and main not in finalLst:
        count+=1
        finalLst.append(main)

file2.writelines(str(count))
file2.writelines("\n")
for q in range (len(finalLst)):
    file2.writelines(finalLst[q][0])
    file2.writelines(" ")
    file2.writelines(finalLst[q][1])
    if q!=(len(finalLst)-1):
        file2.writelines("\n")
file1.close()
file2.close()