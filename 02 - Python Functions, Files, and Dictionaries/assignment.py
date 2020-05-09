
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(x):
    for i in x:
        if i in punctuation_chars:
            x = x.replace(i, '')
    return x


def get_pos(sentence):
    count = 0
    sentence = strip_punctuation(sentence)
    sentence = sentence.split()
    for word in sentence:
        if word in positive_words:
            count += 1
    return count


def get_neg(sentence):
    count = 0
    sentence = strip_punctuation(sentence)
    sentence = sentence.split()
    for word in sentence:
        if word in negative_words:
            count += 1
    return count


with open("project_twitter_data.csv") as fh:
    myfile = fh.readlines()
    csv_data = []
    # Number_of_Retweets = []
    # Number_of_Replies = []
    # Positive_Score = []
    # Negative_Score = []
    # Net_Score = []
    file_handle = myfile[1:]

    # file_handle.extend(myfile[1:])
    for line in file_handle:
        csv_line = {}
        csv_line['Number of Retweets'] = int(line[-2])
        csv_line['Number of Replies'] = int(line[-4])
        csv_line['Positive Score'] = get_pos(line)
        csv_line['Negative Score'] = get_neg(line)
        csv_line['Net Score'] = get_pos(line) - get_neg(line)
        # Positive_Score.append(get_pos(line))
        # Negative_Score.append(get_neg(line))
        # Net_Score.append(get_pos(line) - get_neg(line))
        # print("Number of Replies:", Number_of_Replies[-1])
        # print("Number of Retweets:", Number_of_Retweets[-1])
        # print("Net Score:", Net_Score[-1])
        csv_data.append(csv_line)
print(csv_data)


with open("resulting_data.csv", "w") as fw:
    field_name = ['Number of Retweets', 'Number of Replies', 'Positive Score', 'Negative Score', 'Net Score']

    fw.write(', '.join(field_name))
    fw.write('\n')
    data = []
    for i in csv_data:
        line_data = []
        for j in field_name:
            line_data.append(str(i[j]))
        data.append(', '.join(line_data))
    fw.write(data)

    