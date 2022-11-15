#find the largest number in a list bana 

digits = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
bazenga = digits[0]

for digit in digits:
    if digit > bazenga:
        bazenga = digit

print(bazenga)