import getopt
from util.order import order_and_move
from evaluation import Evaluation
import sys

if __name__ == '__main__':

    args = sys.argv[1:]
    input_dir = ''
    analyzer = ''
    output_dir_prefix = ''

    try:
        (opts, filenames) = getopt.getopt(args, '', ['input-dir=',
                                                     'analyzer=',
                                                     'output_dir_prefix='
                                                     ])

        for (key, val) in opts:
            if key == '--input-dir':
                input_dir = val
            elif key == '--analyzer':
                analyzer = str(val).lower()
            elif key == '--output_dir_prefix':
                output_dir_prefix = val

        evaluation = Evaluation(input_dir, analyzer)
        order_and_move(evaluation.run(), output_dir_prefix)

    except getopt.GetoptError:
        print("Invalid arguments.")
