#!/usr/bin/python
#-*- coding: utf-8 -*-

"""
Created on 2016-12-17
@function: 配置文件
@author: fxm5547
"""
import os


#需要发布代码或执行命令的服务器
ssh_hosts_file = os.path.dirname(__file__) + '/ssh_hosts.txt'

#需要同步文件（夹）的服务器
scp_hosts_file = os.path.dirname(__file__) + '/scp_hosts.txt'

#代码文件根路径
www_root = '/alidata/www/'

#代码文件备份路径
www_bak_path = www_root + 'bak/'

#部署项目
projects = {
    'baobaobooks': 'git@git.coding.net:hbweb/baobaobooks.git',
    'baobaobooks-admin': 'git@git.coding.net:hbweb/baobaobooks-admin.git',
    'shop-mobile-front': 'git@git.coding.net:hbweb/shop-mobile-front.git',
    'u-pc-front': 'git@git.coding.net:hbweb/u-pc-front.git',
    'www-front': 'git@git.coding.net:hbweb/www-front.git',
    'account-front-mobile': 'git@git.coding.net:hbweb/account-front-mobile.git',
    'account-front-pc': 'git@git.coding.net:hbweb/account-front-pc.git',
    'daixiao-front': 'git@git.coding.net:hbweb/daixiao-front.git',
}

#命令
commands = {
    'nginx reload': 'service nginx reload',
    'nginx restart': 'service nginx restart',
    'php-fpm reload': 'service php-fpm reload',
    'php-fpm restart': 'service php-fpm restart',
    'daixiao-node restart': 'cd /alidata/www/daixiao && git pull && npm run build && pm2 restart daixiao',
    'haibao-mobile-front restart': 'cd /alidata/www/haibao-mobile-front && git pull && npm run deploy && pm2 restart haibao-mobile-front',
}

#同步文件／文件夹
paths = {
    'nginx vhosts dir': '/alidata/server/nginx/conf/vhosts',
    'www root dir': '/alidata/www',
}