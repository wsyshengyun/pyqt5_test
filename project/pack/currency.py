# -*- coding: utf-8 -*-
'''
@File    :   currency.py
@Time    :   2022/03/20 20:51:36

'''

# 通用 

def split_ip(ip:str):

    secs =  ip.split('.')
    return secs[-2], secs[-1]

    
def get_ip_tails(ip_list:list):

    return [split_ip(ip)[1] for ip in ip_list ] if ip_list else []


if __name__ == '__main__':
    a = [1,2,3]
    b = ['a', 'b', 'c', 'd']
    c = [('a', 1), ('b', 2), ('c', 3)]
    d = [(i,j) for i in range(5) for j in range(4)]
    z = zip(b, a)
    for m, n in zip(a, c):
        print(m,  *n)
    print(list(z))
    print(d)
    print(len(d))
    print(list(range(1, 20)))
    print(list(range(0, 20)))
    print(list(range(20)))
    a = range(2, 20)
    a = [str(i) for i in a]
    d = d 
    for id, ia in zip(d, a):
        print(*id, ia )
    print(len(list(zip(a, d))))

    print(split_ip('192.169.123.3'))
    print(get_ip_tails(['192.168.1.3', '192.156.2.9']))