import re

pattern = r"[\'\"]{3}(.*?)['\"]{3}"

f = open('D:\\Projects\\DSA\\Data\\Graphs\\Dijkskra Alg\\naive.py').read()

matches = re.search(pattern, f, re.MULTILINE | re.DOTALL)
if matches:
    print(matches.group(1))
