import sys
import subprocess

def GetMisses(trname,l1_isize=32,l1_ibsize=4, l1_iassoc=8 ,l1_dsize=32,l1_dbsize=4, l1_dassoc=8, maxtrace='20'):
    command = ['../dineroIV','-informat','s','-trname',
                                      trname,'-maxtrace', maxtrace,'-l1-isize',
                                      str(l1_isize)+'K','-l1-dsize',str(l1_dsize)+'K','-l1-ibsize',str(l1_ibsize)+'K',
                                      '-l1-dbsize',str(l1_dbsize)+'K','-l1-iassoc',str(l1_iassoc),'-l1-dassoc',str(l1_dassoc)]
    #print("COMMAND: "," ".join(command))
    output = subprocess.check_output(command)
    output = output.decode("utf-8").replace("\\n","\n").replace("\t","")
    output = output.split("\n")
    output = [x for x in output if x.find("Misses")>=0]
    output = [x.split() for x in output ]
    result = []
    for i in range(len(output)):
        result.append(output[i][2])
    return result

consumerCPU = {'size':32, 'bsize':8 , 'assoc':4 }
factor=[0.5,1,2]

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

if __name__=="__main__":
    tentativa = 1;
    if len(sys.argv) == 1:
        eprint ("ERROR: Needs program name to test");
        exit()
    eprint("-----------SCRIPT STARTED------------")
    print('"'+sys.argv[1]+'"')
    print('"size", "block size", "assoc", "l1-i miss", "l1-d miss"');
    for sizeFact in factor:
        for blockFactor in factor:
            for assocFactor in factor:
                eprint("----Test",tentativa,"----")
                tentativa+=1
                line = (str(int(consumerCPU['assoc']*assocFactor*consumerCPU['bsize']*blockFactor))+"K ,"+
                      str(int(consumerCPU['bsize']*blockFactor))+"K ,"+
                      str(int(consumerCPU['assoc']*assocFactor))+",")
                result = (GetMisses(sys.argv[1],int(consumerCPU['assoc']*assocFactor*consumerCPU['bsize']*blockFactor),
                                               int(consumerCPU['bsize']*blockFactor),
                                                int(consumerCPU['assoc']*assocFactor),
                                                int(consumerCPU['assoc']*assocFactor*consumerCPU['bsize']*blockFactor),
                                                int(consumerCPU['bsize']*blockFactor),
                                                int(consumerCPU['assoc']*assocFactor), maxtrace='20'))
                print(line+(", ".join(result)))
    eprint("-----------SCRIPT FINSIHED SUCCESSFULlY------------")
