import os

file_path = ""


def grab_java_files(file_directory):
    files = []
    for parent, dirnames, filenames in os.walk(file_directory):
        for filename in filenames:
            files.append(os.path.join(parent, filename))
    for file in files:
        if not file.endswith('.java'):
            continue

        output_file_path = r"C:\Users\pauld\PycharmProjects\DeepCRMFYP\ClassesToAnalyse\\" + os.path.basename(file)

        with open(file, 'r') as input_file_object, open(output_file_path, 'a') as output_file_object:

            for line in input_file_object:
                output_file_object.write(line)


if __name__ == '__main__':
    grab_java_files(file_path)
