# Email Collector

import re

str = '''

'''

pattern = re.compile(r"[A-za-z]{3,20}@[a-z]{2,12}.[a-z]{2,4}")
emails = pattern.finditer(str)
email_list = []

for email in emails:
    i = 0
    j = 1
    index0 = email.span()[i]
    index1 = email.span()[j]
    email_index = str[index0:index1]
    email_list.append(email_index)

file = open("emails.txt", "w")
n = 1

for emails in email_list:
    file.write(f"email_{n} - {emails}\n")
    n += 1

file.close()
