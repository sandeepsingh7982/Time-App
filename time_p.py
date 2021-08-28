import os
dir_=input(f'enter your directory')
changedir=os.chdir(dir_)
d={}
for i in os.listdir():
    a=os.path.getmtime(i)
    d.update({i:a})
    
with open('sorted1_.txt','w') as f:
    f.write('Sorted in Ascending Order\n\n')
    update_d1={k: v for k,v in sorted(d.items(),key= lambda z:z[1])}
    for key,value in update_d1.items():
        data=f'File Name={key}\t\tlast modification:{value}'
        print(data)
        f.write(data+'\n')
        
with open('sorted2_.txt','w') as f1:
    f1.write('Sorted in Descending order\n\n')
    update_d2={k: v for k,v in sorted(d.items(),key= lambda z:z[1],reverse=True)}
    for key,value in update_d2.items():
        data=f'File Name={key}\t\tlast modification:{value}'
        print(data)
        f1.write(data+'\n')

