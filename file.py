#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Created on 2016-12-17
@function: 同步文件／文件夹
@author: fxm5547
"""

import config.config as conf
import sys
import util

class Scp:
    """
    通过scp同步文件（夹）
    """

    def __init__(self):
        """构造函数"""
        # 选择的文件／文件夹
        self._path = None

        #生成提示语
        option_tips = '选择文件（夹）：\n'
        path_descs = conf.paths.keys()
        path_descs.sort()
        for i, path_desc in enumerate(path_descs, 1):
            option_tips = option_tips + str(i) + ' ' + path_desc + '\n'
        option_tips = option_tips + 'i 手动输入\n'

        #选择文件／文件夹
        while True:
            option = raw_input(option_tips)
            if option.isdigit() and int(option) in range(1, len(path_descs)+1):
                self._path = conf.paths[path_descs[int(option)-1]]
                break
            elif option.lower() == 'i':
                self._path = raw_input('请输入要同步的文件（夹）：')
                return
            else:
                continue

    def __del__(self):
        """析构函数"""

    def scp(self):
        """
        通过pscp同步文件（夹）
        :return: None
        """
        if util.pscp(self._path) != 0:
            sys.stderr.write('同步文件（夹）出错' + '\n')
            return None
        print '同步文件（夹）成功：' + self._path + '\n'
        return None



if __name__ == '__main__':
    scp = Scp()
    scp.scp()







