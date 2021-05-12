class Directory:
    def __init__(self, dir):
        self.current_dir = dir

    def change_dir(self, newDir):
        i = 0
        new_dir = newDir.split('/')
        length = len(new_dir)
        totalPath = self.current_dir.split('/')
        if new_dir[0] == '':
            del totalPath[:]
            totalPath.append('/'+new_dir[1])
            i = i+2
        while(i < length):
            j = len(totalPath)-1
            if new_dir[i] == '..':
                totalPath.pop(j)
            else:
                totalPath.append(new_dir[i])
            i = i+1
        self.current_dir = "/".join(totalPath)

        pass


path = Directory('/a/b/c/d')
path.change_dir('../x')
print(path.current_dir)


'''output'''
'''

root@splendornet-HP-EliteBook-840-G3:~/Documents/Machine learning/reddiff_assignment#root@splendornet-HP-EliteBook-840-G3:~/Documents/Machine learning/reddiff_assignment# p
ython3 q4.py 
/a/b/c/x


'''