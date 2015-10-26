import sys
def dataProcess(fn):
    data=open(fn,'r')
    test=open('test.data','w')
    train=open('train.data','w')
    traint=open('trainTarget.data','w')
    testt=open('testTarget.data','w')
    for line in data:
        line=line.split(',')
        if line[0].strip()=='row.names':
            for i in range(1,257):
                if i!= 256:
                    train.write(line[i].strip()+',')
                    test.write(line[i].strip()+',')
                else:
                    train.write(line[i].strip()+'\n')
                    test.write(line[i].strip()+'\n')
        if line[-1].strip().split('.')[0]=='train':
            print 1
            num=0
            for i in line:
                if num!=258 and num!= 0 :
                    if num<256:
                        train.write(line[num].strip()+',')
                    elif num==256:
                        train.write(line[num].strip()+'\n')
                    else:
                        traint.write(line[num].strip()+'\n')
                num=num+1
        if line[-1].strip().split('.')[0]=='test':
            print 1
            num=0
            for i in line:
                if num!=258 and num!= 0 :
                    if num<256:
                        test.write(line[num].strip()+',')
                    elif num==256:
                        test.write(line[num].strip()+'\n')
                    else:
                        testt.write(line[num].strip()+'\n')
                num=num+1
if __name__=='__main__':
    fn=sys.argv[1]
    dataProcess(fn)




    
