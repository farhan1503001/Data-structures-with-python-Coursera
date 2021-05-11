from os import name


filename=open('mbox.txt')
vocab_list=dict()
for line in filename:
    words=line.rstrip().split()
    if not words:
        continue
    if words[0]=='From':
        vocab_list[words[1]]=vocab_list.get(words[1],0)+1

print(vocab_list)
name=''
count=0
for key,value in vocab_list.items():
    if value>count:
        name=key
        count=value
print(name,count)
