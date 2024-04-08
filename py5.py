str = 'X-DSPAM-Confidence: 0.8475'
pos = (str.find(':') + 1)
ends = len(str)
output = str[pos:ends]
print(output.strip())


