#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Created on 2014-11-24

@author: fxm5547
"""

from deploy import Git
from ssh import Ssh
from file import Scp
import sys


if __name__ == '__main__':
    option_tips = ('1 发布项目\n'
                   '2 执行命令\n'
                   '3 同步文件（夹）\n'
                   'q 退出\n')

    while True:
        option = raw_input(option_tips)
        if option.isdigit() and int(option) in range(1, 4):
            if option == '1':
                while True:
                    deploy_option_tips = ('1 clone整体发布项目\n'
                                          '2 pull更新项目\n'
                                          'q 退出\n')
                    deploy_option = raw_input(deploy_option_tips)
                    if deploy_option == '1':
                        git = Git()
                        git.clone()
                        break
                    elif deploy_option == '2':
                        git = Git()
                        git.pull()
                        break
                    elif deploy_option.lower() == 'q':
                        break
                    else:
                        continue
            elif option == '2':
                ssh = Ssh()
                ssh.ssh()
            elif option == '3':
                scp = Scp()
                scp.scp()
        elif option.lower() == 'q':
            sys.exit(0)
        else:
            continue


