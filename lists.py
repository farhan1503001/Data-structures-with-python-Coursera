
filename=open('romeo.txt')
collector=list()
for line in filename:
    line.rstrip()#Remove the white spaces on the right side
    words=line.split()
    for word in words:
        if word in collector:
            continue
        collector.append(word)

collector.sort()
print(collector)

file2=open('mbox.txt')
count=0
lister=list()
for row in file2:
    word=row.rstrip().split()
    if not word:
        continue
    if word[0]=='From:':
        continue
    if word[0].lower()=='from':
        lister.append(word[1])
        count=count+1

    #print(word)
print("There were",count,"lines in here")
print(lister)