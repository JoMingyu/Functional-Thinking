"""
s 중 search_chars 중 어느 문자든 s에서 처음으로 발견되는 위치를 반환하라.
"""

def index_of_any(s, search_chars):
    if not s:
        raise ValueError('String is empty')
    if not search_chars:
        raise ValueError('Chars for search are empty')

    for idx, ch in enumerate(s):
        if ch in search_chars:
            return idx
