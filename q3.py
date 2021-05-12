import re
import json

def generateDicts(log_fh):
    currentDict = {}
    for line in log_fh:
        if line.startswith(matchDate(line)):
            if currentDict:
                yield currentDict
            currentDict = {"date":line.split("__")[0][:19],"type":line.split("-",5)[4],"text":line.split("-",5)[-1]}
        else:
            currentDict["text"] += line
    yield currentDict

def matchDate(line):
    matchThis = ""
    matched = re.match(r'\d\d\d\d-\d\d-\d\d\ \d\d:\d\d:\d\d',line)
    if matched:
        #matches a date and adds it to matchThis
        matchThis = matched.group()
    else:
        matchThis = "NONE"
    return matchThis

with open("new.logs") as f:
    listNew= list(generateDicts(f))
    print(*listNew,sep = "\n")

with open("myfile.txt", 'w') as f:
    for i in  listNew:
        for key, value in i.items():
            f.write('%s:%s\n' % (key, value))


#output
'''
root@splendornet-HP-EliteBook-840-G3:~/Documents/Machine learning/reddiff_assignment# python3 q3.py 
{'date': '2015-05-22 16:46:46', 'type': ' INFO ', 'text': ' Starting to Wait for Files\n'}
{'date': '2015-05-22 16:46:56', 'type': ' Warnings ', 'text': ' Starting: Attempt 1 Checking for New Files from gs://folder/folder/\n'}
{'date': '2015-05-22 16:47:46', 'type': ' INFO ', 'text': ' Success: Downloading the Files from Cloud Storage: Return Code - 0 and FileCount 1\n'}
{'date': '2015-05-22 16:48:48', 'type': ' ERROR ', 'text': ' Failed: Waiting for files the Files from Cloud Storage: gs://folder/folder/'}

'''