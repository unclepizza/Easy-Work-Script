#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: gaok 
@contact: 542385331@qq.com 
@site: https://blog.csdn.net/qq_27258799 
@file: files_cleaner.py 
@time: 2018/4/25 11:34 
""" 

import os
import re
import shutil

MOVED_DIR = 'D:\\Users\\gaok\\.gradle\\move'  # 移动后的路径
TARGET_DIR = 'D:\\Users\\gaok\\.gradle\\daemon'  # 待处理的路径
DELETED_FILES_NAME = 'D:\\Users\\gaok\\.gradle\\deleteFiles.txt'  # 被删除文件的名字
DELETE_PATTERN = re.compile('daemon-\w*\.out')  # 待删除文件名的格式
COUNT = 0


# 对目标文件进行处理
def do_operation(target_file_path):
    # 写入文件
    # record_deleted_files_name(target_file_path)
    # 移动文件
    # move_file_to_new_dir(target_file_path)
    # 删除文件
    # saved_delete_file(target_file_path)
    # 重命名
    rename_file(target_file_path)


def rename_file(target_file_path):
    global COUNT
    if os.path.isfile(target_file_path):
        extension = os.path.splitext(target_file_path)[1]  # 扩展名
        ''' e.g. /E/dd/cc/test.txt 
            dirname = /E/dd/cc  
            basename = test.txt'''
        new_name = (os.path.dirname(target_file_path) + '/rename_ %s' + extension) % (COUNT)  # 重命名为rename
        COUNT += 1
        try:
            shutil.move(target_file_path, new_name)
        except IOError:  # 对于被别的程序占用的文件，直接操作会报错
            print('[文件被占用] = ' + target_file_path)


def saved_delete_file(target_file):
    if os.path.isfile(target_file):
        try:
            send2trash.send2trash(target_file)  # 使用send2trash安全删除（丢到回收站）
        except IOError:  # 对于被别的程序占用的文件，直接操作会报错
            print('[文件被占用] = ' + target_file)


def move_file_to_new_dir(target_file):
    if not os.path.exists(MOVED_DIR):
        os.mkdir(MOVED_DIR)
    try:
        shutil.move(target_file, MOVED_DIR)
    except IOError:
        print('[文件被占用] = ' + target_file)


def record_deleted_files_name(target_file):
    print('[Deleted File] = ' + target_file)
    write_file = open(DELETED_FILES_NAME, 'a')  # a是追加模式，否则文件会被覆盖
    write_file.write(target_file)
    write_file.write('\n')
    write_file.close()


def delete_file(target_path):
    result = DELETE_PATTERN.match(os.path.basename(target_path))
    if result is not None:  # 找到待删除文件
        do_operation(target_path)


def find_delete_file(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            delete_file(os.path.join(root, f))


if __name__ == '__main__':
    find_delete_file(TARGET_DIR)
