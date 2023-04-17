import os

file_path = r"C:\Users\pauld\PycharmProjects\DeepCRMFYP\InputRepositories"


def grab_java_files(file_directory):
    files = []
    for parent, dirnames, filenames in os.walk(file_directory):
        for filename in filenames:
            files.append(os.path.join(parent, filename))
    for file in files:
        if not file.endswith('.java'):
            continue
        output_file_path = r"C:\Users\pauld\PycharmProjects\DeepCRMFYP\TrialClasses\\" + os.path.basename(file)

        with open(file, 'r') as input_file_object, open(output_file_path, 'a') as output_file_object:
            try:
                for line in input_file_object:
                    if line[:7] != "package" and line[:6] != "import":
                        output_file_object.write(line)
            except UnicodeDecodeError:
                output_file_object.close()
                os.remove(output_file_path)


if __name__ == '__main__':
    grab_java_files(file_path)
