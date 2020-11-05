import re

string = '''name: Akash Gupta,
            email: akash910203955@gmail.com,
            phone: +91 9102039155, 06145-78654, +91 6754389765
            address: Tilha Rajendra Ashram Thakur saw lane,
            Hobby: Coding and progarmming,
            City: Gaya,
            State : Bihar,
            Counter: India,
            to kasie aaaaaaappp appp apap llloogg
            Companies: Google, Microsoft, Facebook, Apple, Tesla, SpaceX, SolarCity, Paypal, Ebay.'''

# Findall, search, split, sub, finditer

# pattern = re.compile(r"Google")
# pattern = re.compile(r".Google")
# pattern = re.compile(r"^name")
# pattern = re.compile(r"Ebay.$")
# pattern = re.compile(r"a*p*")
# pattern = re.compile(r"ap+")
# pattern = re.compile(r"ap{2,4}")
# pattern = re.compile(r"(ap){2}")
# pattern = re.compile(r"ap{1}|Tesla")

# SPecial sequences
# pattern = re.compile(r"\Aname")
# pattern = re.compile(r"\bAkash")
# pattern = re.compile(r"Akash\b")
pattern = re.compile(r"[+91]{3} [0-9]{10}")
list = []

matches = pattern.finditer(string)
for match in matches:
    # print(match)
    a = match.span()
    # print(a)
    list.append(match)


print(list)

"""
# Small Notes:- 

.   Any character (except newline)
^   Starts with
$   Ends with
*   Zero or more occurrences
+   one or more occurences
{}  Exactly the specified no. of occurrences
()  Capture and Group

# Special sequence:-

\A  begining of string
\b  begining or ending of words, ex:- \bword & word\b
\d  digit ex- \d{10}

"""