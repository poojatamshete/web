def order_bvalue(file):
    orderdict = {}
    for key,value in file.items():
        if value in orderdict:
            orderdict[value].append(key)
        else:
            orderdict[value] = [key]
    return orderdict

file = {
    'a.txt':'pooja',
    'p.txt':'mau',
    'c.txt':'shinu',
    'd.txt':'mau'
}
print(order_bvalue(file))

#output
'''
root@splendornet-HP-EliteBook-840-G3:~/Documents/Machine learning/reddiff_assignment# python3 q1.py 
{'pooja': ['a.txt'], 'mau': ['p.txt', 'd.txt'], 'shinu': ['c.txt']}

'''