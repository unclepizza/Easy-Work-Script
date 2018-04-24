import os
import re
import shutil
import send2trash

MOVED_DIR = 'D:\\Users\\gaok\\.gradle\\move'  # 移动后的路径
TARGET_DIR = 'D:\\Users\\gaok\\.gradle\\daemon'  # 待处理的路径
DELETED_FILES_NAME = 'D:\\Users\\gaok\\.gradle\\deleteFiles.txt'  # 被删除文件的名字
DELETE_PATTERN = re.compile('daemon-\w*\.out')  # 待删除文件名的格式


# 对目标文件进行处理
def do_operation(target_file):
    # 写入文件
    # record_deleted_files_name(target_file)
    # 移动文件
    # move_files_to_new_dir(target_file)
    # 删除文件
    saved_delete_files(target_file)


def saved_delete_files(target_file):
    if os.path.isfile(target_file):
        try:
            send2trash.send2trash(target_file)  # 使用send2trash安全删除（丢到回收站）
        except IOError:  # 对于被别的程序占用的文件，直接操作会报错
            print('[文件被占用] = ' + target_file)


def move_files_to_new_dir(target_file):
    if not os.path.exists(MOVED_DIR):
        os.mkdir(MOVED_DIR)
    try:
        shutil.move(target_file, MOVED_DIR)
    except IOError:
        print('[文件被占用] = ' + target_file)


def record_deleted_files_name(target_file):
    print('[Deleted File] = ' + target_file)
    writeFile = open(DELETED_FILES_NAME, 'a')  # a是追加模式，否则文件会被覆盖
    writeFile.write(target_file)
    writeFile.write('\n')
    writeFile.close()


def delete_file(target_path, target_file):
    result = DELETE_PATTERN.match(target_file)
    if result is not None:  # 找到待删除文件
        do_operation(target_path)


def find_delete_file(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for f in files:
            delete_file(os.path.join(root, f), f)


if __name__ == '__main__':
    find_delete_file(TARGET_DIR)
