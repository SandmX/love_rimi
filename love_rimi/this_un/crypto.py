import hashlib
from pathlib import Path


"""------ 对内容加密解密 ------"""

def encrypt(s: str, k: int) -> str:
    ac = [ord(c) + k for c in s]
    return ",".join(map(str, ac))


def decrypt(s: str, k: int) -> str:
    ac = [int(c) - k for c in s.split(",")]
    return "".join(chr(_) for _ in ac)


# def XOR(s: str, k: int) -> str:
#     r = ''
#     for c in s:
#         c_en = chr(ord(c) ^ k)
#         r += c_en
#     return r

"""------ 对签名生成和校验 ------"""

def read_line(f: Path, l: int) -> str:
    d = ''
    with f.open('r', encoding='utf-8') as f:
        for i in range(l):
            d += f.readline()

    return d

def gen_sign(lang_c: str) -> str:
    h = hashlib.sha256()
    h.update(lang_c.encode('utf-8'))

    return h.hexdigest()

def gen_sign_from_file(lang_f: Path) -> str:
    h = hashlib.sha256()
    h.update(read_line(lang_f, 4).encode('utf-8'))

    return h.hexdigest()

def check_sign(lang_f: Path) -> bool:
    total = lang_f.read_text(encoding='utf-8')
    content = read_line(lang_f, 4).strip()
    sign_check = total.replace(content, '').strip()
    sign_correct = gen_sign(content)
    return sign_correct == sign_check


