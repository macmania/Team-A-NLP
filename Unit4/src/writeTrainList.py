import os, glob, errno

def writeTrainList():
    files = glob.glob('../YourSmallAllLabelled/*.txt')
    f= open('YourSmallTrain.txt','w')
    count_pos=0
    count_neg=0
    for name in files:
        ext=name[-8:-4]
        name= os.path.basename(name)
        if ext=='_pos':
            f.write(name+' '+'pos'+'\n')
            count_pos+=1
        elif ext=='_neg':
            f.write(name+' '+'neg'+'\n')
            count_neg+=1
    print('count_pos='+str(count_pos)+' and count_neg='+str(count_neg))
    f.close()            
    
writeTrainList()
