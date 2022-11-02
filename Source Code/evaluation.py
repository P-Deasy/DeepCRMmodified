import os
from util.util import create_new_dir, walk_files
from util.distincy import distincy


class Evaluation(object):
    def __init__(self, input_dir, analyzer):
        self.input_dir = input_dir
        self.analyzer = analyzer

    @staticmethod
    def create_file_with_class(file_path, file_path_with_class):
        file = open(file_path)
        tmp_file = open(file_path_with_class, 'w')
        tmp_file.write('public class TestClass {' + os.linesep + file.read() + os.linesep + '}')
        file.close()
        tmp_file.close()

    def evaluate_files(self, file_list, file_result_dict):
        marking_file_dict = {}

        dir_for_marking = 'dir_for_marking'

        create_new_dir(dir_for_marking)

        for file_path in file_list:
            new_file_path = dir_for_marking + os.sep + os.path.basename(file_path)
            self.create_file_with_class(file_path, new_file_path)
            marking_file_dict[os.path.basename(new_file_path)] = file_path

        print('------pmd start-------')
        # pmd
        output_lines = []
        cmd = './analyzer/pmd-bin-6.51.0/bin/run.sh pmd -d ' + dir_for_marking + \
              ' -R rulesets/java/basic.xml,rulesets/java/design.xml,rulesets/java/braces.xml,rulesets/java/' \
              'comments.xml,rulesets/java/codesize.xml,rulesets/java/controversial.xml,rulesets/java/naming.xml -f text'
        output_lines.extend(os.popen(cmd).readlines())
        for line in output_lines[1:]:
            if line.find('Error while parsing') != -1:
                print('ERROR while running analyzer')
                print(line)
                continue
            file_path_in_result = line[:line.find(':')]
            file_path_in_result = marking_file_dict[os.path.basename(file_path_in_result)]
            if file_path_in_result not in file_result_dict:
                file_result_dict[file_path_in_result] = 0
            file_result_dict[file_path_in_result] = file_result_dict[file_path_in_result] + 1

        print('------checkstyle start-------')
        # checkstyle
        output_lines = []
        output_lines.extend(
            os.popen(
                'java -jar ./analyzer/checkstyle-8.2-all.jar -c /google_checks.xml ' + dir_for_marking).readlines())
        output_lines.extend(
            os.popen('java -jar ./analyzer/checkstyle-8.2-all.jar -c /sun_checks.xml ' + dir_for_marking).readlines())
        for line in output_lines:
            if line.startswith('['):
                file_path_in_result = line[line.find('] ') + 2:line.find(':')]
                file_path_in_result = marking_file_dict[os.path.basename(file_path_in_result)]
                if file_path_in_result not in file_result_dict:
                    print('ERROR------------%s does not have pmd marking' % file_path_in_result)
                    continue
                file_result_dict[file_path_in_result] = file_result_dict[file_path_in_result] + 1

        total_violations_count = 0.0
        file = open(self.input_dir + '_violations.txt', 'w')
        for (k, v) in file_result_dict.items():
            file.write(k + ',' + str(v) + '\n')
            total_violations_count = total_violations_count + v
        file.close()

        print('average rule violation: %f' % (total_violations_count / len(file_result_dict)))

    def run(self):
        file_list = []
        walk_files(self.input_dir, file_list, '.java')

        distincy(file_list)

        file_result_dict = {}
        self.evaluate_files(file_list, file_result_dict)

        return file_result_dict
