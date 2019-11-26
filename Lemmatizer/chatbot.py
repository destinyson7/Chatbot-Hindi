import requests
import re

sentences = []
roots = []
pos_tags = []
stopwords = []

with open('data_sentences.txt', 'r') as f:
    for line in f:
        sentences.append(line.split("\n")[0])

with open('data_roots.txt', 'r') as f:
    for line in f:
        roots.append(line.split("\n")[0])

with open('data_pos_tags.txt', 'r') as f:
    for line in f:
        pos_tags.append(line.split("\n")[0])

with open('stop_words.txt', 'r') as f:
    for line in f:
        stopwords.append(line.split("\n")[0])


def lemmatize(line):
    cur_root = ""
    arr_words = re.split("\.[0-9]\\\\t", line)

    for i in range(1, len(arr_words)):
        words = re.split('\\\\t', arr_words[i])
        # print(arr_words[i])
        temp = arr_words[i].split('\'')
        print(temp)
        cur_root = cur_root + (temp[1].split(',')[0] + ' ')

    return cur_root


def cosine_similarity(first_sentence):
    array_first = first_sentence.split(" ")

    max_cos = -1
    max_i = -1

    for i in range(0, len(sentences)):
        array_second = sentences[i].split(" ")

        # We will also remove all the stop words from both the sets later

        set_first = {word for word in array_first if not word in stopwords}
        set_second = {word for word in array_second if not word in stopwords}

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

        if cos > max_cos:
            max_i = i
            max_cos = cos

    return max_i


while True:
    query = input()

    if query == "Bye":
        break

    headers = {'Content-Type': 'application/json'}

    data = '{"text":"' + query.strip() + '"}'
    response = requests.post('http://10.2.6.249:8010/shallow_parse_hin', headers=headers, data=data.encode('utf-8'))
    print(response.text)
    lemmatized_query = lemmatize(response.text)

    print(cosine_similarity(lemmatized_query))

    try:
        response = sentences[cosine_similarity(lemmatized_query)] + sentences[cosine_similarity(lemmatized_query) + 1]

    except:
        response = sentences[cosine_similarity(lemmatized_query)]

    print(response)
