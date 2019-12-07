# 破解ctf比赛中的md5截断认证, 如: substr(md5($str), 0, 6) === "3322cf"
from hashlib import md5  
from string import ascii_letters, digits
from itertools import permutations  

all_string = ascii_letters + digits + '.,:;-_'

def fuzz_md5(value):  
    value = value.lower()     # 转换为小写
    for i in range(10):  
        print('.', end = '')  
        for item in permutations(all_string, i):  
            item = ''.join(item)  
            if md5(item.encode()).hexdigest()[0:len(value)] == value:
                print('\nSuccess: ' + value + ' ==> ' + item)
                return

md5_value = '3322cf'  
fuzz_md5(md5_value)
