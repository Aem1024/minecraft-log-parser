import os
data = "/path/to/logs"
serverip = ""
logs = [f for f in os.listdir(data) if os.path.isfile(os.path.join(data, f))]

logs.sort()

masterlist = []

for i in range(len(logs)):
    isserver = False
    hypixel = False
    bufferlist = []
    log = open(data+str(logs[i]), "r", encoding="utf8")
    print("%3.1f%%" % ((i/float(len(logs)))*100))
    linelist = []
    newline = log.readline()
    while True:
            newline = log.readline()
            if (serverip.upper() in newline.upper()):
                isserver = True
            if ("hypixel".upper() in newline.upper()):
                hypixel = True
            if len(newline) == 0:
                break
            else:
                if (("[CHAT]".upper() in newline.upper())):
                    bufferlist.append("["+str(logs[i]) + "] ")
                    bufferlist.append(newline)
    if (isserver == True and hypixel == False):
        masterlist.extend(bufferlist)
        
    log.close()


outfile = open("output.txt", "w", encoding="utf8")
outfile.writelines(masterlist)
