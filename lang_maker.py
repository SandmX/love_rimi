from love_rimi.this_un import LANG_F_DIR
from love_rimi.this_un.crypto import encrypt, gen_sign

"""
This script generates a language file 
You can find it in pkg/this_un/lang
"""

"""------ 配置区 ------"""

# 国际语言代码 (str)
name = 'ar'
# 版本号 (str) e.g. x.x.x.x
version = '0.0.0.1'
# 加密密钥 (int)
key = 5201314
# 内容
c = """لـريمي، من ساندماير
أجمل من بساطة الكود،
حيوية مثل دقة الخوارزمية.
كما تضيء التعليقات معنى الكود،
ابتسامتك تمنح حياتي اللون.
مثل دالة لها هدف محدد،
نظراتك توجه قلبي.
في الحب، أتطلع إلى المنطق،
وأنتِ هي أجمل القواعد.
الأخطاء لم تعد مخيفة أمامك،
لأن تسامحك مثل الصبر في التصحيح.
مثل الحلقة، الحب لا يتوقف أبدًا،
مرافقتي لك هي سعاي الأبدي.
ريمي، أنت كود روحي،
مُجمَع مع الحب، لا أخطاء أبدًا.
ليكن قصتنا مثل مشروع مفتوح المصدر،
يتشارك الجمال ويبقى دائمًا في الذاكرة.
"""

"""------  END  ------"""

lang_f = (LANG_F_DIR / name).with_suffix('.lang')
if lang_f.exists():
    if input(f'已存在文件:{lang_f}, 是否覆盖? [y/n]\n') != 'y':
        exit(0)

c_enc = encrypt(c, key)
content = name + '\n' + c_enc + '\n' + str(key) + '\n' + version
content = content + '\n' + gen_sign(content)
lang_f.write_text(content)
