import pandas as pd
import re

# df = pd.read_csv('dictionaries/chemnitz/de-en.txt', sep='::', delimiter=None, header='infer', names=None, index_col=None, engine='python')
# print(df)

min_word_len = 4

# writing to file
f = open('dictionaries/chemnitz/de-en.txt', 'r')
lines = f.readlines()


def split_string_by_multiple_separators(text):
    strings = re.split('[;,|]{1}', text)
    return strings


def remove_text_between_parentheses(s):
    s = re.sub(r'\([^)]*\)', '', s)
    s = re.sub(r'\[[^)]*\]', '', s)
    s = re.sub(r'\{[^)]*\}', '', s)
    s = re.sub(r'\<[^)]*\>', '', s)
    return s


def remove_side_spaces(s):
    s = s.lstrip()
    s = s.rstrip()
    return s


def remove_unwanted_characters(s):
    s = s.replace('…', '')
    return s


df_cols = ['word', 'full_def', 'short_def', 'example_sentence', 'hint_level']
df = pd.DataFrame(columns=df_cols)

count = 0
for line in lines:
    line = line.strip()
    line = remove_unwanted_characters(line)

    level1 = line.split('::')
    left_side = level1[0]
    right_side = level1[1]

    # Split the right side
    rights = split_string_by_multiple_separators(remove_text_between_parentheses(right_side))
    for i, r in enumerate(rights):
        rights[i] = remove_side_spaces(r)

    # Split the left side, the guiding one
    lefts = split_string_by_multiple_separators(remove_text_between_parentheses(left_side))
    for l in lefts:
        l = remove_side_spaces(l)
        # Ignore words that are too short
        if len(l) < min_word_len:
            continue
        df = df.append({'word': l,
                        'full_def': remove_side_spaces(right_side),
                        'short_def': rights[0],
                        'hint_level': 5},
                       ignore_index=True)

    count += 1
    if count%1000 == 0:
        print(count)

df.drop_duplicates('word', keep='first', inplace=True)

df.to_csv('out.csv',
          index=True,
          index_label='id')
