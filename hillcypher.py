import string
import numpy as np
import math

# keyword=input("Enter encryption key:")
# text=input("Enter text to be encrypted:")
keyword="GYBNQKURP"
text="Act"

special="!@#$%^&*()_+-=~`<>?,./:\";'[]{}\|"
# valid=string.ascii_uppercase+string.digits+special
valid=string.ascii_uppercase
total_chars=len(valid)
def batch_size(keyword):
    keylen=len(keyword)
    n=int(math.sqrt(keylen))
    if(n*n)!=keylen:
        n+=1
    print(n)
    return n

def convert_keyword_to_word_matrix(keyword):
    keyword=keyword.upper()
    # n=len(text)
    keylen=len(keyword)
    # n=math.sqrt(keylen)//1
    n=batch_size(keyword)
    sqr=n*n
    # rem=keylen%n
    # if(rem!=0):
    #     add=keyword[-1]*(n-rem)
    #     keyword_copy=keyword+add
    # else:
    #     keyword_copy=keyword
    add=keyword[-1]*(sqr-keylen)
    print(f'sqr={sqr} keylen={keylen}')
    print("add=",add)
    keyword_copy=(keyword+add)
    print(keyword_copy)
    key_arr=[ch for ch in keyword_copy]
    print(f'keyword_copy= {keyword_copy}')
    key_arr=np.array(key_arr)
    key_arr=key_arr.reshape(-1,n)
    print(key_arr)
    return key_arr
def convert_text_to_word_matrix(keyword,text):
    print("entered convert text to word matix with keyword=",keyword," text=",text)
    print(f"lenth of text",len(text))
    text = text.replace('\x00', '') #removing null characters
    n=batch_size(keyword)
    print("and n=",n)
    # if len(text)<n:
    #     print("Please try again with a shorter keyword!")
    #     exit(0)
    rem=len(text)%n
    print("rem=",rem)
    if(rem!=0):
        pad=(n-rem)
        # text_copy=text+('z'*pad)
        text_copy=text
        for i in range(pad):
            text_copy=text_copy+'0'
        print("pad=",pad)
    else:
        text_copy=text
    # text_copy=text+(text[-1]*pad)
    
    
    print(f"rem={rem},text_copy={text_copy}")
    text_copy=text_copy.upper()
    print(f"lenth of text_copy",len(text_copy))
    print("upper text copy",text_copy)
    # text_arr=[ch for ch in text_copy]
    text_arr=[]
    for ch in text_copy:
        text_arr.append(ch)
    print("text_Arr1")
    print(text_arr)
    text_arr=np.array(text_arr)
    print("text_Arr2")
    print(text_arr)
    text_arr=text_arr.reshape(-1,n)
    print("before returning")
    print(text_arr)
    return text_arr

convert_to_mod_valid=np.vectorize(lambda x:x%total_chars)
convert_to_numeric=np.vectorize(lambda x:valid.index(x))
convert_to_chars=np.vectorize(lambda x:valid[x])
round_off=np.vectorize(lambda x:int(np.rint(x)))
# key_arr_numeric=convert_to_numeric(key_arr)
# text_arr_numeric=convert_to_numeric(te)
def convert_to_numeric_key_array(key_arr):
    print("Entered cinvert_to)numeric")
    print(key_arr)
    key_arr_numeric=convert_to_numeric(key_arr)
    print(key_arr_numeric)
    print("end")
    return key_arr_numeric
def convert_to_numeric_text_arr(text_arr):
    print("Entered cinvert_to)numeric_text_arr")
    print(text_arr)
    text_arr_numeric=convert_to_numeric(text_arr)
    #transposing to make it a column matrix
    text_arr_numeric=text_arr_numeric.T
    print(text_arr_numeric)
    print("eend 2")
    return text_arr_numeric

def check_determinant_of_encryption_key(key_arr_numeric):
    # The determinant of the encryption key matrix should be relatively prime 
    # to the length of valid character set. i.e. total_chars variable
    det=np.linalg.det(key_arr_numeric)
    det=int(det)
    if det<0:
        det=det%total_chars
    #check gcd
    # if math.gcd(det,total_chars)!=1:
    #     print("Determinant Invalid. Please try a different key")
    #     return False
    # else:
    #     print("Valid Determinant. Can proceed with this key")
    #     return True
    return True
def multiply(key_arr_numeric, text_arr_numeric):
    print("entered multiply with")
    print(key_arr_numeric)
    print(text_arr_numeric)
    result=np.dot(key_arr_numeric,text_arr_numeric)
    print(f'result before mod={result}')
    result=convert_to_mod_valid(result)
    # result=convert_to_int_type(result)
    print(f'result after mod={result}')
    print("end multiply")
    return result
def encrypt(keyword,text):
    key_arr=convert_keyword_to_word_matrix(keyword)
    text_arr=convert_text_to_word_matrix(keyword,text)
    key_arr_numeric=convert_to_numeric_key_array(key_arr)
    text_arr_numeric=convert_to_numeric_text_arr(text_arr)

    isvalidkey=check_determinant_of_encryption_key(key_arr_numeric)
    if not isvalidkey:
        exit(0)
    result=multiply(key_arr_numeric, text_arr_numeric)
    # return result
    char_arr=convert_to_chars(result)
    print(char_arr)
    # encrypted=""
    # for i in char_arr:
    #     encrypted
    
    encrypted=char_arr.tostring().decode('utf-8')
    print(encrypted)
    return encrypted
# def convert_to_string(result):
#     char_arr=convert_to_chars(result)
#     print(char_arr)
#     # encrypted=""
#     # for i in char_arr:
#     #     encrypted
    
#     encrypted=char_arr.tostring().decode('utf-8')
#     print(encrypted)
#     return encrypted
def create_decrypt_key(keyword):
    key_arr=convert_keyword_to_word_matrix(keyword)
    key_arr_numeric=convert_to_numeric_key_array(key_arr)
    det=np.linalg.det(key_arr_numeric)
    det=int(det)
    if det==0:
        print("Decryption wont work with this keyword, pls try again with diff key")
        exit(0)
    elif det < 0:
        det = det % total_chars
    det_inv = None #modular multiplicative inverse
    for i in range(total_chars):
        if (det * i) % total_chars == 1:
            det_inv = i
            break
    dec_key=det_inv*det*np.linalg.inv(key_arr_numeric)
    dec_key=convert_to_mod_valid(dec_key) 
    return dec_key
def decrypt(keyword,cipher):
    dec_key=create_decrypt_key(keyword)
    print("dec_key")
    print(dec_key)
    cipher_arr=convert_text_to_word_matrix(keyword,cipher)
    print("cipher_arr")
    print(cipher_arr)
    cipher_arr_numeric=convert_to_numeric_text_arr(cipher_arr)
    print("cipher_arr_numeric")
    print(cipher_arr_numeric)
    result=multiply(dec_key, cipher_arr_numeric)
    result=round_off(result)
    result=convert_to_mod_valid(result)
    print("DECRYPTED FINAL RESULT ARRAY")
    print(result)
    char_arr=convert_to_chars(result)
    
    print("CHAR ARRAY")
    print(char_arr)
    decrypted=""
    for i in char_arr:
        for j in i:
            decrypted+=j
    print(decrypted)
    return decrypted

cipher=encrypt(keyword,text)
print(f"CIPHER={cipher}\n\n\n\n\n")
plaint=decrypt(keyword,cipher)
print(f"DECRYPTED={plaint}")
