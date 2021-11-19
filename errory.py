#! python3
# errory.py - The quick and dirty python script to evaluate your programming assignments

import zipfile,sys,subprocess,os,re,shutil
from shlex import quote

#Options 
TIMEOUT=30 #seconds      #Stops execution of the program if it takes more than TIMEOUT seconds to execute.This is considered as a runtime error as an occurence of non terminating program
DELETE_TEMP_FILES=True   #Option True deletes the temporary files after execution, option False will retain the temporary files
USE_GDB=True             #Use GDB for extra Runtime error info

print(f"Starting Execution \nThe options set are:\nTIMEOUT: {TIMEOUT} seconds\nDELETE_TEMP_FILES: {DELETE_TEMP_FILES}\nUSE_GDB: {USE_GDB}\nGenerating Report....\n")
pgm=zipfile.ZipFile(sys.argv[1])
tst=zipfile.ZipFile(sys.argv[2])
reg=re.compile(r'in')
r="error_"+sys.argv[1][0:6]
shutil.rmtree(f"./{r}/temp",ignore_errors=True)
os.makedirs(f"./{r}/temp")
pgm.extractall(f"./{r}/temp")
tst.extractall(f"./{r}/temp/archive")

c=0
ru=0
t=0
t_O=0

os.makedirs(f"./{r}/temp/compile")
os.makedirs(f"./{r}/temp/out")





fc=open(f"./{r}/compile_error_{sys.argv[1][0:6]}.txt",'a')
fr=open(f"./{r}/runtime_error_{sys.argv[1][0:6]}.txt",'a')
ft=open(f"./{r}/testcase_mismatch_{sys.argv[1][0:6]}.txt",'a')
fc.truncate(0)
fr.truncate(0)
ft.truncate(0)



for files in os.listdir(f"./{r}/temp/{sys.argv[1][:-4]}"):
    l=subprocess.run(f"gcc ./{r}/temp/{quote(sys.argv[1][:-4])}/{files} -o ./{r}/temp/compile/{files[:-2]} -lm -g",shell=True,stderr=subprocess.PIPE)
    if l.stderr.decode("utf-8")!="":
        str=l.stderr.decode("utf-8")
        c+=1
        fc.write(files+"\n\n")
        fc.write(str+"\n\n\n")

fc.close()


for files in os.listdir(f"./{r}/temp/compile"):
    os.makedirs(f"./{r}/temp/out/q{files[-1]}")
    
    for  foldername,subfolders,filenames in os.walk(f"./{r}/temp/archive"):
        for fil in filenames:
            if re.match(reg,fil) and os.path.basename(foldername)=="q"+files[-1]:
                try:
                    rep=foldername.replace(" ", "\\ ")
                    P=os.path.abspath(f"./{r}/temp/compile/{files}")
                    Q=os.path.abspath(f"./{r}/temp/out/q{files[-1]}/out{fil[2]}.txt")
                    m=subprocess.run(f"(cd {rep}  &&  exec {P}<./{fil}>{Q})",shell=True,stderr=subprocess.PIPE,timeout=TIMEOUT)
                except subprocess.TimeoutExpired:
                    ru+=1
                    t_O+=1
                    os.remove(f"./{r}/temp/out/q{files[-1]}/out{fil[2]}.txt")
                    fr.write(os.path.basename(foldername)+" TestCase"+fil[-5]+"\n")
                    fr.write(f"Program might have run into an infinite loop or it needs more than {TIMEOUT} seconds to execute.Try changing the TIMEOUT variable in errory.py or check for non terminating code.\n\n")
                    continue
                if m.stderr.decode("utf-8")!="":
                        ru+=1
                        
                        fr.write(os.path.basename(foldername)+" TestCase"+fil[-5]+"\n")
                        fr.write(m.stderr.decode("utf-8")+"\n")
                        if(USE_GDB==True):
                            m=subprocess.run(f"(cd {rep}  &&  exec gdb -batch -ex 'r < ./{fil}' -ex 'q' {P})",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)# stderr is piped to remove error from console
                            fr.write(m.stdout.decode("utf-8")[:-136]+"\n\n")
                            if m.stderr.decode("utf-8")!="":
                                gdb_err=m.stderr.decode("utf-8")
                                fr.write(f"GDB ERROR:{gdb_err}\n\n\n\n")
                            else:
                                fr.write("\n\n")
                        os.remove(f"./{r}/temp/out/q{files[-1]}/out{fil[2]}.txt")
                        

fr.close()



for  foldername,subfolders,filenames in os.walk(f"./{r}/temp/out"):
   for filename in filenames:
        for  folder,subfold,filenam in os.walk(f"./{r}/temp/archive"):
            for fil in filenam:
                if fil==filename and os.path.basename(folder)==os.path.basename(foldername):
                    rep=folder.replace(" ", "\\ ")
                    k=subprocess.run(f"diff -Z   {foldername}/{filename} {rep}/{fil}",shell=True,stdout=subprocess.PIPE)
                    if k.stdout.decode("utf-8")!="":
                        t+=1
                        ft.write(os.path.basename(foldername)+" TestCase"+fil[-5]+"\n\n")
                        ft.write(k.stdout.decode("utf-8")+"\n\n\n")

ft.close()

if DELETE_TEMP_FILES==True:
    shutil.rmtree(f"./{r}/temp")
        



if os.stat(f"./{r}/compile_error_{sys.argv[1][0:6]}.txt").st_size==0:
    os.remove(f"./{r}/compile_error_{sys.argv[1][0:6]}.txt")

if os.stat(f"./{r}/runtime_error_{sys.argv[1][0:6]}.txt").st_size==0:
    os.remove(f"./{r}/runtime_error_{sys.argv[1][0:6]}.txt")

if os.stat(f"./{r}/testcase_mismatch_{sys.argv[1][0:6]}.txt").st_size==0:
    os.remove(f"./{r}/testcase_mismatch_{sys.argv[1][0:6]}.txt")


if len(os.listdir(f"./{r}"))==0:
    shutil.rmtree(f"./{r}")




print(f'Checking complete with {c} Compile errors, {ru} Runtime errors({t_O} TIMEOUT errors) and {t} Test case mismatches')
if (c+ru+t)!=0:
    print(f'Check "{r}" folder for detailed report')
else:
    print("Great Work!!! No errors for you :D")
print("Happy Coding :)")

