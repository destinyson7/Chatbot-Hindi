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

print(stopwords)


def lemmatize(line):
    cur_root = ""
    arr_words = re.split("\.[0-9]\\\\t", line)

    for i in range(1, len(arr_words)):
        words = re.split('\\\\t', arr_words[i])
        temp = arr_words[i].split('\'')
        cur_root = cur_root + (temp[1].split(',')[0] + ' ')

    return cur_root


# while True:
#     query = input()

#     if query == "Bye":
#         break

#     headers = {'Content-Type': 'application/json'}

#     data = '{"text":"' + query.strip() + '"}'
#     response = requests.post('http://10.2.6.249:8010/shallow_parse_hin', headers=headers, data=data.encode('utf-8'))

#     lemmatized_query = lemmatize(response.text)
