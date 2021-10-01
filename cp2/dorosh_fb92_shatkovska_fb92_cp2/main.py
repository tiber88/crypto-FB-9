# # This is the 2nd lab on Cryptology yet in progress by Dorosh and Shatkovska FB-92
from collections import Counter
import random
from itertools import chain

keys_list = ['мэ', 'фуж', 'хшлъ', 'етгуз', 'илиъглкяоф', 'йпфъчнвэови', 'щзрхдъыэрглф', 'нблзчсхкмшпня', 'сучвнюоъптяамю', 'ъеьяюжхээфъэыью', 'гакыыхрвбчлючицы', 'рнътдцаоицкшлжьни', 'ьищэксьтчбещйархря', 'увэояихшцхерхкпхнфы', 'яоьдэузэцяеьобмэхруы']

# getting the alphabet
def get_dict():
    a = ord('а')

    # ["_"] +
    alphabet = ["_"] + [chr(i) for i in range(a,a+32)]

    return alphabet


def open_file(txt):
    with open(txt, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    return text


# Cleaning example text to match the criteria before doing the task
def clean_text(txt):
    chars = '.71()-«5d?[“!93286”…—4;»0:],na'

    with open(txt, 'r', encoding='utf-8') as file:
        text = file.read().lower()
    for ch in chars:
        text = text.replace(ch, '')

    text = ''.join([word.strip('\n') for word in text.split('_')])

    with open('example_prepared.txt', 'w', encoding='utf-8') as file:
        file.write(text)


def encode(text, key):
    encrypted = []

    for idx, ch in enumerate(text):
       # print(idx, ch)
        p_idx = alphabet.index(ch)
        k_idx = (idx+1) % len(key)
        print(p_idx, k_idx)
        c_idx = (p_idx + k_idx) % len(alphabet)

        encrypted.append(alphabet[c_idx])
    return encrypted


def decode(text, key):
    decrypted = []
    key_idx = [alphabet.index(k) for k in key]
    for idx, ch in enumerate(text):
        print(idx, ch)
        c_idx = alphabet.index(ch)
        k_idx = key_idx[idx % len(key)]
        p_idx = (c_idx - k_idx + len(alphabet)) % len(alphabet)

        decrypted.append(alphabet[p_idx])
    return decrypted


def count_mono(text):
    res = Counter(text[idx] for idx in range(len(text)))
    res = {x: round(res[x]/len(text), 6) for x in res}
    return dict(res)

alphabet = get_dict()
in_text = "большойфлопченко"
"""
print("Encoded text")
for key in keys_list:
    c_text = encode(in_text, key)
    print(f" {key} : {len(key)} : {''.join(c_text)}")"""

key = "кот"
c_text = encode(in_text, key)
print(''.join(c_text))
p_text = decode(c_text, key)
print(''.join(p_text))

# test and debug

get_dict()
clean_text("example.txt")
#in_text = "большойфлопченко"
in_key = "кот"
#test = encode(in_text, in_key)
#print(test)
#print(decode(test, in_key))
#print(gen_keys(alphabet))
# бпньщрйхнорщеомо
# бпньщрйхнорщеомо

'''a = ord('а')
pr = enumerate([chr(i) for i in range(a,a+32)])
for p, k in pr:
    print(p+1, k)
print(pr)'''