from .crypto import decrypt, read_line, check_sign
from . import LANG_F_DIR


assert LANG_F_DIR.exists()  # 不存在语言文件根目录

def this(lang_fn: str) -> None:
    lang_f = LANG_F_DIR / lang_fn
    if lang_f.suffix != '.lang':
        lang_f = lang_f.with_suffix('.lang')

    assert lang_f.exists()  # 不存在该语言文件
    assert check_sign(lang_f)  # 签名错误

    line_1to2 = read_line(lang_f, 2)
    s = line_1to2.replace(read_line(lang_f, 1), '')
    k = int(read_line(lang_f, 3).replace(line_1to2, ''))
    print(decrypt(s, k))

