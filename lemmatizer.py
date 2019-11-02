import sys
count = 0
w = 0

sentences = []
roots = []
pos_tags = []
cur_sentence = ""
cur_root = ""
cur_pos = ""
with open(sys.argv[1], 'r') as f:
    for line in f:

        if line[0] == "<" and line[1] == "/" and line[2] == "S":
            sentences.append(cur_sentence)
            roots.append(cur_root)
            pos_tags.append(cur_pos)

            print(cur_sentence)
            print(cur_root)
            print(cur_pos)
            print()

            cur_sentence = ""
            cur_root = ""
            cur_pos = ""

        elif line[0] == ")":
            continue

        else:

            line1 = line.split(' ')

            if line1[0] == "<Sentence":
                count = count + 1
                print("<Sentence_id=%d>" % (count))

            elif line1[1] == "((":
                continue

            else:
                if len(line1[2].split('<')) == 1:
                    cur_sentence = cur_sentence + line1[1] + " "
                    cur_root = cur_root + line1[4].split(',')[0].split('\'')[1] + " "
                    cur_pos = cur_pos + line1[2] + " "

                else:
                    cur_sentence = cur_sentence + line1[1] + " "
                    cur_root = cur_root + line1[3].split(',')[0].split('\'')[1] + " "
                    cur_pos = cur_pos + line1[2].split('<')[0] + " "

                # print(line1[1] + "\t" + line1[4].split(',')[0].split('\'')[1] + "\t" + line1[2])

# print(sentences)
# print(roots)
# print(pos_tags)
