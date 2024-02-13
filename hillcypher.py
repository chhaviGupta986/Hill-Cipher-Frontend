import string
import numpy as np


keyword=input("Enter encryption key:")
text=input("Enter text to be encrypted:")

special="!@#$%^&*()_+-=~`<>?,./:\";'[]{}\|"
valid=string.ascii_uppercase+string.digits+special
total_chars=len(valid)

def convert_to_encryption_key(keyword,text):
    n=len(text)
    keylen=len(keyword)
    rem=keylen%n
    if(rem!=0):
        add=keyword[-1]*(n-rem)
        keyword_copy=keyword+add
    else:
        keyword_copy=keyword
    key_arr=[ch for ch in keyword_copy]
    print(f'keyword_copy= {keyword_copy}')
    key_arr=np.array(key_arr)
    key_arr=key_arr.reshape(-1,n)
    print(key_arr)
    return key_arr

convert_to_encryption_key(keyword,text)


