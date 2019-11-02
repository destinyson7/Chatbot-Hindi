import sys

first_sentence = "यह योजना का एक बड़ी खामी यह है कि महंगाई दर से यह सब्सिडी को जोड़ा नहीं जा है"
second_sentence = "दिल्ली शहरी इलाका है"

array_first = first_sentence.split(" ")
array_second = second_sentence.split(" ")

# We will also remove all the stop words from both the sets later

set_first = {word for word in array_first}
set_second = {word for word in array_second}

union = set_first.union(set_second)

# print(union)

sum_first = 0
sum_second = 0

numerator = 0

for word in union:

    a = 0
    b = 0

    if word in set_first:
        a = 1

    else:
        a = 0

    if word in set_second:
        b = 1

    else:
        b = 0

    sum_first = sum_first + a
    sum_second = sum_second + b

    numerator = numerator + a * b

cos = numerator / float((sum_first * sum_second)**0.5)

print(cos)
