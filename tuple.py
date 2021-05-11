filename=open('mbox.txt')
timer=dict()
for line in filename:
    words=line.rstrip().split()
    if not words:
        continue
    if words[0]!="From":
        continue
    splitted=words[5].split(':')
    timer[splitted[0]]=timer.get(splitted[0],0)+1
    #print(splitted)

sorted_timer=sorted(timer.items())
#print(timer)
for k,v in sorted_timer:
    print(k,v)


text = "X-DSPAM-Confidence:    0.8475";
pos=text.find('.')
print(float(text[pos-1:]))