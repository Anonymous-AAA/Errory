#! python3
# errory.py - The quick and dirty python script to evaluate your programming assignments

import zipfile,sys,subprocess,os,re
from shlex import quote

print("Starting Execution")
pgm=zipfile.ZipFile(sys.argv[1])
tst=zipfile.ZipFile(sys.argv[2])
reg=re.compile(r'in')
pgm.extractall()
tst.extractall("./archive")

c=0
ru=0
t=0
subprocess.run("mkdir compile",shell=True)
subprocess.run("mkdir out",shell=True)
r="error_"+sys.argv[1][0:6]
subprocess.run("mkdir "+quote(r),shell=True)
fc=open("./"+r+"/compile_error_"+sys.argv[1][0:6]+".txt",'a')
fr=open("./"+r+"/runtime_error_"+sys.argv[1][0:6]+".txt",'a')
ft=open("./"+r+"/testcase_mismatch_"+sys.argv[1][0:6]+".txt",'a')
fc.truncate(0)
fr.truncate(0)
ft.truncate(0)



for files in os.listdir("./"+sys.argv[1][:-4]):
    l=subprocess.run("gcc "+quote(sys.argv[1][:-4])+"/"+files+" -o ./compile/"+files[:-2],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    if l.stderr.decode("utf-8")!="":
        str=l.stderr.decode("utf-8")
        c+=1
        fc.write(files+"\n\n")
        fc.write(str+"\n\n\n")

fc.close()

for files in os.listdir("./compile"):
    subprocess.run("mkdir ./out/q"+files[-1],shell=True)
    for  foldername,subfolders,filenames in os.walk("./archive"):
        for fil in filenames:
            if re.match(reg,fil) and os.path.basename(foldername)=="q"+files[-1]:
                m=subprocess.run("./compile/"+files+"<"+foldername.replace(" ", "\\ ")+"/"+fil+">./out/q"+files[-1]+"/out"+fil[2]+".txt",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                if m.stderr.decode("utf-8")!="":
                        ru+=1
                        subprocess.run("rm ./out/q"+files[-1]+"/out"+fil[2]+".txt",shell=True)
                        fr.write(os.path.basename(foldername)+" TestCase"+fil[-5]+"\n")
                        fr.write(m.stderr.decode("utf-8")+"\n\n")

fr.close()

for  foldername,subfolders,filenames in os.walk("./out"):
    for filename in filenames:
        for  folder,subfold,filenam in os.walk("./archive"):
            for fil in filenam:
                if fil==filename and os.path.basename(folder)==os.path.basename(foldername):
                    k=subprocess.run("diff -Z   "+foldername+"/"+filename+" "+folder.replace(" ", "\\ ")+"/"+fil,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                    if k.stdout.decode("utf-8")!="":
                        t+=1
                        ft.write(os.path.basename(foldername)+" TestCase"+fil[-5]+"\n")
                        ft.write(k.stdout.decode("utf-8")+"\n\n")

ft.close()

try:
     if sys.argv[3]=='d':
        subprocess.run("rm -r archive compile out "+quote(sys.argv[1][:-4]),shell=True)

except IndexError:
    pass


print(f'Checking complete with {c} Compile errors, {ru} Runtime errors and {t} Test case mismatches')
print(f'Check "{r}" folder for detailed report')
print("IMPORTANT:Please delete the generated files if you are running the code again\nHappy Coding :)")

