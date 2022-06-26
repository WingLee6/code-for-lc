# -*- coding: utf-8 -*-
# @Time    : 2022/3/10 
# @Author  : li
# @FileName: CallTestCase.py
# @Desc    : 调用测试用例（TestCase.txt)

class CallTestCase(object):
    def __init__(self):
        """

        """

    def strToList(self, str_list):
        '''
        '[1,3]\n'（str类型）转化为[1, 3]（list类型）
        :param str_list:
        :return:
        '''
        for i in range(len(str_list)):
            str_list[i] = eval(str_list[i])  # eval()函数： '[1,3]\n'（str类型）转化为[1, 3]（list类型）
        return str_list

    def strToStr(self, str_list):
        '''
        '"abcabcbb"\n' 提取为 'abcabcbb'
        :param str_list:
        :return:
        '''
        for i in range(len(str_list)):
            str_list[i] = str_list[i][1:-2]
        return str_list

    def readTxt(self, qusetion_id_int=None, parameter_type_str=None):

        with open('/Users/luke_lee/VScodeProject/CodeForLeetCode/PythonLang/Tools/TestCase.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(lines)
            # Step1 根据问题序号（）截取文档
            start_int = lines.index('*****q'+str(qusetion_id_int) + '*****\n')
            end_int = lines.index('*****q'+str(qusetion_id_int+1) + '*****\n') if '*****q'+str(qusetion_id_int+1)+'*****\n' in lines else len(lines)
            lines = lines[start_int+1:end_int]
            if parameter_type_str == 'list':
                lines = self.strToList(lines)
            elif parameter_type_str == 'str':
                lines = self.strToStr(str_list=lines)

        print(lines)



if __name__ == '__main__':
    cell = CallTestCase()
    cell.readTxt(qusetion_id_int=3, parameter_type_str='str')
