from love_rimi.this_un import check


lang_f_dir = check.where()
# lang_f_dir = check.LANG_F_DIR  # 不建议
print("Module<this_un>语言包存放路径:", lang_f_dir)

lang_f_list = check.lang_list()
print("已有的语言包:\n", lang_f_list)

