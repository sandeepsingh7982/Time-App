import os
dir_=input(f'enter your directory')
changedir=os.chdir(dir_)
d={}
d1={}
for i in os.listdir():
    a=os.path.getsize(i)
    d.update({i:str(a)+'bytes'})
    
with open('sorted_.txt','w') as f:
    f.write('Sorted in Ascending Order\n\n')
    b=sorted(d.values())
    for i in b:
        for j in d.keys():
            if d[j]==i:
                d1[j]=d[j]

    for key,value in d1.items():
        data=f'File Name={key}\t\tFile Size:{value}'
        print(data)
        f.write(data+'\n')
        



