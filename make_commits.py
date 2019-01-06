import subprocess
for i in range(1000):
    w = open("numbers.txt","w")
    w.writelines(str(i))
    w.close()
    #race condition for commits cannot do git operations 10% of time
    try:
        print(subprocess.Popen(["git","add","numbers.txt"], stdout=subprocess.PIPE).stdout)
    except subprocess.CalledProcessError as e:
        print(e.output)
        sleep(1)
        i= i-1
        continue
    print(subprocess.Popen(["git","commit","-m", str(i) + " commit"], stdout=subprocess.PIPE).stdout)  
print(subprocess.Popen(["git","status"], stdout=subprocess.PIPE).stdout)
