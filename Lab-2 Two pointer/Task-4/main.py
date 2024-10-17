file1=open("D:\Alg\Lab-2 Two pointer\Task-4\input.txt","r")
file2=open("D:\Alg\Lab-2 Two pointer\Task-4\output.txt","w")
length=file1.readline().strip("\n").split(" ")
lst=[]
for y in range (int(length[0])):
    arr=file1.readline().strip("\n").split(" ")
    lst.append(arr)

for t in range (int(length[0])):
    flag1=False
    main1=lst[t]
    index=t+1
    if t==((int(length[0]))-1):
        break
    for u in range (t+1,int(length[0])):
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

count=0
for x in range (int(length[1])):
    finalLst=[]
    for i in range (int(length[0])):
        flag=True
        main=lst[i]
        fixedMain=lst[i]
        index=i
        for z in range (int(length[0])):
            if main == lst[z] or  main == None or lst[z]==None:
                continue
            if (len(finalLst))!=0 and int(finalLst[len(finalLst)-1][1])>int(main[0]):
                flag=False
                break
            temp=lst[z]
            if (int(main[0])==int(temp[0]) or int(main[0])<int(temp[0])) and (int(temp[0])<int(main[1])):
                sizeMain=int(main[1])-int(main[0])
                sizetemp=int(temp[1])-int(temp[0])
                if sizeMain>sizetemp:
                    main=temp
                    index=z
        if flag and main!=None:
            count+=1
            finalLst.append(main)
            lst[index]=None

file2.writelines(str(count))
file1.close()
file2.close()