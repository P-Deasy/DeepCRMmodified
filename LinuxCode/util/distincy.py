import os
import hashlib


def distincy(file_list):
    print('-----distincy start from %d files -------' % len(file_list))

    md5_dict = {}
    for i in range(len(file_list) - 1, -1, -1):
        file_path = file_list[i]
        md5file = open(file_path, 'rb')
        md5 = hashlib.md5(md5file.read()).hexdigest()
        md5file.close()

        if md5 in md5_dict:
            print('%s has same md5 with %s with md5 %s' % (file_path, md5_dict[md5], md5))
            os.remove(file_path)
            file_list.remove(file_path)
        else:
            md5_dict[md5] = file_path

    print('-----distincy end with %d files -------' % len(file_list))
