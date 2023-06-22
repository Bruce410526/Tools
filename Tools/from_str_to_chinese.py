# 该文档可以从从字符串中提取中文

import re

def get_chinese(strs):

    a_list = re.findall(r'[\u4e00-\u9fa5]',strs)
    chinese = ''.join(a_list)
    print(chinese)
    return chinese

strs = input("请输入任意字符，回车结束：")
get_chinese(strs)
