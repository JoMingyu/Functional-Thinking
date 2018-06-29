"""
텍스트에서 가장 많이 사용된 단어를 찾고, 그 단어와 빈도를 정렬된 목록으로 출력하는 함수를 작성하라.
"""

import re
import collections
import operator

NON_WORDS = frozenset(
    (
        'the', 'and', 'of', 'to', 'a', 'i', 'it', 'in',
        'or', 'is', 'd', 's', 't', 'as', 'so', 'but', 'be', '\n',
        "don't", "let's"
    )
)

def rank_word_frequency(paragraph):
    return dict(
        reversed(
            sorted(
                (collections.Counter(
                    [word for word in re.findall('[A-z]+', paragraph.lower()) if word not in NON_WORDS]
                )).items(), key=operator.itemgetter(1)
            )
        )
    )
