#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Created on 2016-12-17
@function: 执行ssh命令
@author: fxm5547
"""

import config.config as conf
import sys
import util

class Ssh:
    """
    通过ssh执行命令
    """

    def __init__(self):
        """构造函数"""
        # 选择的文件／文件夹
        self._command = None

        #生成提示语
        option_tips = '选择操作：\n'
        command_descs = conf.commands.keys()
        command_descs.sort()
        for i, command_desc in enumerate(command_descs, 1):
            option_tips = option_tips + str(i) + ' ' + command_desc + '\n'
        option_tips = option_tips + 'i 手动输入\n'

        #选择文件／文件夹
        while True:
            option = raw_input(option_tips)
            if option.isdigit() and int(option) in range(1, len(command_descs)+1):
                self._command = conf.commands[command_descs[int(option)-1]]
                break
            elif option.lower() == 'i':
                self._command = raw_input('请输入要执行的命令：')
                return
            else:
                continue

    def __del__(self):
        """析构函数"""

    def ssh(self):
        """
        通过pssh执行命令
        :return: None
        """
        if util.pssh(self._command) != 0:
            sys.stderr.write('执行命令出错' + '\n')
            return None
        print '执行命令成功：' + self._command + '\n'
        return None



if __name__ == '__main__':
    ssh = Ssh()
    ssh.ssh()







