"""
어떤 이름 목록에서, 한 글자로 된 이름을 제외한 모든 이름을 대문자화해서
쉼표로 연결한 문자열을 구하는 함수를 작성하라.
"""

def clean_names(names):
    return ','.join(name.upper() for name in names if len(name) > 1)