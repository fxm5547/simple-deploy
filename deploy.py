#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Created on 2016-12-17
@function: 通过git完成代码部署
@author: fxm5547
"""

import config.config as conf
import sys
import util

class Git:
    """
    通过git发布或更新项目的类
    """

    def __init__(self):
        """构造函数"""
        # 选择的项目
        self._project = None
        # 选择的项目的零时名称
        self._project_tempname = None
        # 选择的项目的git地址
        self._project_giturl = None
        # 选择的项目的备份路径
        self._project_bakpath = None

        #生成提示语
        option_tips = '选择项目：\n'
        pro_names = conf.projects.keys()
        pro_names.sort()
        for i, pro_name in enumerate(pro_names, 1):
            option_tips = option_tips + str(i) + ' ' + pro_name + '\n'

        #选择项目
        while True:
            option = raw_input(option_tips)
            if option.isdigit() and int(option) in range(1, len(pro_names)+1):
               self._project = pro_names[int(option)-1]
               self._project_tempname = self._project + '_prod'
               self._project_giturl = conf.projects[self._project]
               self._project_bakpath = conf.www_bak_path + self._project
               break
            else:
                continue

    def __del__(self):
        """析构函数"""

    def clone(self):
        """
        通过git clone整体部署项目
        :return: None
        """
        #clone项目
        print 'clone代码...'
        command_template = 'git config --global user.email "martin@baobaobooks.com" 2>&1 && git config --global user.name "fxm5547" 2>&1 && cd {wwwroot}  && ( rm -rf {project_temp} 2>&1; git clone --recursive  {giturl} {project_temp} 2>&1 ) && cd {project_temp} && git checkout release 2>&1 && git submodule foreach git checkout release 2>&1 && chown -R www:www {wwwroot}{project_temp}'
        command = command_template.format(wwwroot=conf.www_root, giturl=self._project_giturl,
                                          project_temp=self._project_tempname, project=self._project)
        if util.pssh(command) == 0:
            #替换项目
            print '\n替换代码...'
            mv_command_template = 'mkdir -p {www_bak_path} 2>&1 ; rm -rf {project_bakpath} 2>&1 ; mkdir -p {wwwroot}{project} 2>&1 ; mv {wwwroot}{project} {www_bak_path} 2>&1 ; mv {wwwroot}{project_temp} {wwwroot}{project} 2>&1 '
            mv_command = mv_command_template.format(www_bak_path=conf.www_bak_path,
                                                    project_bakpath=self._project_bakpath, wwwroot=conf.www_root,
                                                    project=self._project, project_temp=self._project_tempname)
            if util.pssh(mv_command) != 0:
                sys.stderr.write('替换项目出错' + '\n')
                return None
        else:
            sys.stderr.write('clone代码出错' + '\n')
            return None
        print 'clone发布项目成功：' + self._project + '\n'
        return None

    def pull(self):
        """
        通过git pull更新项目
        :return: None
        """
        command_template = 'git config --global user.email "martin@baobaobooks.com" 2>&1 && git config --global user.name "fxm5547" 2>&1 && cd {wwwroot}{project}  && git fetch --all 2>&1 && git reset --hard origin/release 2>&1 && git checkout release 2>&1 && git submodule foreach git fetch --all 2>&1 && git submodule foreach git reset --hard origin/release 2>&1 && git submodule foreach git checkout release 2>&1 && chown -R www:www {wwwroot}{project}'
        command = command_template.format(wwwroot=conf.www_root, project=self._project)
        if util.pssh(command) != 0:
            sys.stderr.write('pull代码出错' + '\n')
            return None
        print 'pull更新项目成功：' + self._project + '\n'
        return None



if __name__ == '__main__':
    git = Git()
    git.clone()
    git.pull()






