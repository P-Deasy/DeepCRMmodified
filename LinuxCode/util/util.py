import os


def walk_files(input_dir, file_list, ex):
    print('input dictionary: %s' % input_dir)
    for parent, dirNames, filenames in os.walk(input_dir):
        for dirname in dirNames:
            print('the full name of the dir is:' + os.path.join(parent, dirname))

        for filename in filenames:
            if not filename.endswith(ex):
                continue
            file_list.append(os.path.join(parent, filename))

    print('%d %s files in %s' % (len(file_list), ex, input_dir))


def create_new_dir(dir_path):
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        os.popen('rm -rf ' + dir_path)
        os.mkdir(dir_path)
    else:
        os.mkdir(dir_path)
