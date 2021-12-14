#!/usr/bin/env python3

'''
Code adapted from https://github.com/xxyzz/WordDumb/tree/master/klld
'''

import re
from lxml import etree
from collections import defaultdict
import csv

RE = r'(?:\([^)]+\)|\[[^]]+\]|‹[^›]+›|<[^>]+>|«[^»]+»|:)'


def parse_es_dict(rawml_path, dic, en_klld):
    for _, element in etree.iterparse(
            rawml_path, tag='hr', html=True,
            remove_blank_text=True, remove_comments=True):

        lemma = element.xpath('following-sibling::div[1]/div[1]/b/text()')
        if len(lemma) == 0:
            element.clear(keep_tail=True)
            continue
        lemma = lemma[0]

        '''
        if lemma not in en_klld:
            element.clear(keep_tail=True)
            continue
        '''

        defs = []
        for s in element.xpath(
                'following-sibling::div[2]//a/following-sibling::span'):
            definition = s.xpath('descendant-or-self::text()')
            examples = s.xpath(
                'following-sibling::*/descendant-or-self::text()')
            definition.extend(examples)
            defs.append(''.join(definition).strip())
        defs = [(x, re.sub(
            RE, '', re.split(r'[;•]', x, 1)[0]).strip()) for x in defs]
        dic[lemma].extend(filter(lambda x: len(x[1]), defs))
        element.clear(keep_tail=True)


if __name__ == "__main__":
    dic = defaultdict(list)
    # parse_es_dict("Duden Deutsches Universalwörterbuch - Duden.rawml", dic, None)
    parse_es_dict("dictionaries/Oxford German - English Dictionary (German Edition).rawml", dic, None)

    with open('wordwise-dict-de-en.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "word", "full_def", "short_def", "example_sentence", "hint_level"])

        i = 0
        for key, value in dic.items():
            if len(value) > 0:
                level1 = value[-1]
                level2 = level1[-1]
                # print(level2)
                writer.writerow([i, key, "", level2, "", 1])
                i = 1 + 1
