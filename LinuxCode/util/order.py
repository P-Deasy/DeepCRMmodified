import shutil
from util.util import create_new_dir
import os


def order_and_move(file_mark_dict, output_dir_prefix):
    sorted_file_marks = sorted(file_mark_dict.items(), key=lambda x: x[1], reverse=False)

    count = len(sorted_file_marks)
    print(count)
    top_file_marks = sorted_file_marks[0: count // 4]
    top_mid_file_marks = sorted_file_marks[count // 4:count * 2 // 4]
    bottom_mid_file_marks = sorted_file_marks[count * 2// 4: count * 3 // 4]
    bottom_file_marks = sorted_file_marks[count * 3 // 4:]

    top_file_dir = output_dir_prefix + '_1best'
    create_new_dir(top_file_dir)

    for (top_file_path, mark) in top_file_marks:
        shutil.copy(top_file_path, top_file_dir + os.sep + os.path.basename(top_file_path))
        
    top_mid_file_dir = output_dir_prefix + '_2mid'
    create_new_dir(top_mid_file_dir)

    for (top_mid_file_path, mark) in top_mid_file_marks:
        shutil.copy(top_mid_file_path, top_mid_file_dir + os.sep + os.path.basename(top_mid_file_path))

    bottom_mid_file_dir = output_dir_prefix + '_3mid'
    create_new_dir(bottom_mid_file_dir)

    for (bottom_mid_file_path, mark) in bottom_mid_file_marks:
        shutil.copy(bottom_mid_file_path, bottom_mid_file_dir + os.sep + os.path.basename(bottom_mid_file_path))

    bottom_file_dir = output_dir_prefix + '_4worst'
    create_new_dir(bottom_file_dir)

    for (bottom_file_path, mark) in bottom_file_marks:
        shutil.copy(bottom_file_path, bottom_file_dir + os.sep + os.path.basename(bottom_file_path))
