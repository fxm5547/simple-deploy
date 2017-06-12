#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Created on 2016-12-17
@function: 工具函数
@author: fxm5547
"""

import config.config as conf
import os
import sys


def pssh(command):
    """
    封装pssh的操作
    :return: None
    """
    pssh_command = "pssh -h {hosts} -t 300 -i '{command}'".format(hosts=conf.ssh_hosts_file, command=command)
    return os.system(pssh_command)

def pscp(path):
    """
    封装pscp的操作
    :return: None
    """
    src = path
    dst_dir = os.path.dirname(src) + '/'
    pscp_command = "pscp -h {hosts} -v -p -r {src} {dst_dir}".format(hosts=conf.scp_hosts_file, src=src, dst_dir=dst_dir)
    while True:
        option = raw_input('确认同步文件／文件夹（y/n）: ' + path)
        if option.lower() == 'y':
            return os.system(pscp_command)
        elif option.lower() == 'n':
            return None
        else:
            continue



if __name__ == '__main__':
    pssh('ls&&pwd')
