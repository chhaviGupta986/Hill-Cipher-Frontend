import string
import numpy as np
import math

keyword=input("Enter encryption key:")
text=input("Enter text to be encrypted:")

special="!@#$%^&*()_+-=~`<>?,./:\";'[]{}\|"
valid=string.ascii_uppercase+string.digits+special
total_chars=len(valid)

def convert_keyword_to_word_matrix(keyword,text):
    keyword=keyword.upper()
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
def convert_text_to_word_matrix(text):
    text=text.upper()
    text_arr=[ch for ch in text]
    text_arr=np.array(text_arr)
    return text_arr

convert_to_mod_valid=np.vectorize(lambda x:x%total_chars)
convert_to_numeric=np.vectorize(lambda x:valid.index(x))
convert_to_chars=np.vectorize(lambda x:valid[x])

# key_arr_numeric=convert_to_numeric(key_arr)
# text_arr_numeric=convert_to_numeric(te)
def convert_to_numeric_key_array(key_arr):
    key_arr_numeric=convert_to_numeric(key_arr)
    return key_arr_numeric
def convert_to_numeric_text_arr(text_arr):
    text_arr_numeric=convert_to_numeric(text_arr)
    #transposing to make it a column matrix
    text_arr_numeric=text_arr_numeric.T
    return text_arr_numeric

def check_determinant_of_encryption_key(key_arr_numeric):
    # The determinant of the encryption key matrix should be relatively prime 
    # to the length of valid character set. i.e. total_chars variable
    det=np.linalg.det(key_arr_numeric)
    if det<0:
        det=det%total_chars
    #check gcd
    if math.gcd(det,total_chars)!=1:
        print("Determinant Invalid. Please try a different key")
        return False
    else:
        print("Valid Determinant. Can proceed with this key")
        return True
def multiply(key_arr_numeric, text_arr_numeric):
    result=np.dot(key_arr_numeric,text_arr_numeric)
    print(f'result before mod={result}')
    result=convert_to_mod_valid(result)
    print(f'result after mod={result}')
    return result
def encrypt():
    pass


