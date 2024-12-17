# -*- coding: utf-8 -*-
"""Regex.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1b48lcVDlDbmnTq8mSx4CkNVKOMh8aYsy
"""

# Importing necessary libraries -

import re

# Downloading dataset -

!gdown 1sSDV5UspYZL3UUOGuiuxppSGcv1wS9ex

data = open("data.txt", "r").read()
print(data[:500]) # display some data

import re # importing regex library

def is_vemail(s):
  email_pattern = "^\w+([\.-]?\w+)*@\w+([|.-]?\w+)*(\.\w{2,3})+$"
  res = re.search(email_pattern, s)
  # scans through string looking for the first location where pattern is found
  if res:
    return True
  else:
    return False

is_vemail("abc@gm.com")

is_vemail("sgargh.com")

# Regular Expression

pattern = "\d{3}-\d{3}-\d{4}"
print(re.match(pattern, data))

pattern = "\d{3}-\d{3}-\d{4}"
print(re.search(pattern, data)) # first occurence

pattern = "\d{3}-\d{3}-\d{4}"
res = re.findall(pattern, data)
print(res)

pattern = "\d{3}-\d{3}-\d{4}"
numbers = re.finditer(pattern, data)

for i, num in enumerate(numbers):
  print(num)
  if i==5:
    break

re.match('ab*', 'a')
re.match('ab*', 'ab')
re.match('ab*', 'abb')

re.match('ab*', 'ba')

print(re.match('ab*', 'ba'))

re.search('aaaa', 'alohaaaa')

re.search('aaa', 'alohaaaa')

re.search('aaa', 'alohaaa')

re.search('aaaa', 'alohaaa')

print(re.search('aaaa', 'alohaaa'))

x='[0-9]+'
re.findall(x, '7 768 apples and 444 mangoes 345')

import re
x = r'\bs\w*t\b' # start with s, end with t
re.findall(x, 'she sells seat short')

!gdown https://drive.google.com/file/d/1tlGQIZjOrrMYYOwbXCiC6qMgksf_zNWz/view?usp=sharing

mydata = open("view?usp=sharing", "r").read()
print(mydata[:500]) # display some data

!gdown 1tlGQIZjOrrMYYOwbXCiC6qMgksf_zNWz

mydata = open("navdeepsandhu.rtf", "r").read()
print(mydata[:500]) # display some data

!gdown 1rZ-DizDSoAmrzGu8GkhJlJsy3geqBUtG

mydata = open("sample1.txt", "r").read()
print(mydata[:500]) # display some data

import re
ans = re.search('amet', mydata)
ans

!gdown 1rZ-DizDSoAmrzGu8GkhJlJsy3geqBUtG

mydata = open("sample1.txt", "r").read()
print(mydata[:500]) # display some data

import re
ans = re.search('Collatio', mydata)
ans

!gdown 1wBnedCujROorrsggZs_mx-F240cushDQ

navdeep = open("Regex.txt", "r").read()
print(navdeep)

import re
pattern = "\d{3}-\d{3}-\d{3}"
print(re.search(pattern, navdeep))