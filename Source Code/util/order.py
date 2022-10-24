import shutil
from util.util import create_new_dir
import os


def order_and_move(file_mark_dict, output_dir_prefix):
    sorted_file_marks = sorted(file_mark_dict.items(), key=lambda x: x[1], reverse=False)

    count = len(sorted_file_marks)
    top_file_marks = sorted_file_marks[0: count / 4]
    bottom_file_marks = sorted_file_marks[count * 3 / 4:]

    top_file_dir = output_dir_prefix + '_readable'
    create_new_dir(top_file_dir)

    for (top_file_path, mark) in top_file_marks:
        shutil.copy(top_file_path, top_file_dir + os.sep + os.path.basename(top_file_path))

    bottom_file_dir = output_dir_prefix + '_unreadable'
    create_new_dir(bottom_file_dir)

    for (bottom_file_path, mark) in bottom_file_marks:
        shutil.copy(bottom_file_path, bottom_file_dir + os.sep + os.path.basename(bottom_file_path))
