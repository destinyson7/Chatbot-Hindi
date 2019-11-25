sentences = []
roots = []
pos_tags = []
with open('data_sentences.txt', 'r') as f:
    for line in f:
        sentences.append(line.split("\n")[0])

with open('data_roots.txt', 'r') as f:
    for line in f:
        roots.append(line.split("\n")[0])

with open('data_pos_tags.txt', 'r') as f:
    for line in f:
        pos_tags.append(line.split("\n")[0])

print(sentences[0])
print(roots[0])
print(pos_tags[0])
