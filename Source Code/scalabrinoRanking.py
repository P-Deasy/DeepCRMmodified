import os
from pandas import read_csv


input_code = r"C:\Users\pauld\OneDrive\Documents\DSA\FYP\ScalabrinoDataset\Snippets"
ranking = read_csv(r"C:\Users\pauld\OneDrive\Documents\DSA\FYP\ScalabrinoDataset\scores_updated.csv")


def scalabrino_ranking(file_directory):
    files = []
    for parent, dirnames, filenames in os.walk(file_directory):
        for filename in filenames:
            files.append(os.path.join(parent, filename))
    ranking_entry = 1
    rank = 0
    for file in files:
        if ranking.iloc[10][ranking_entry] <= ranking.iloc[11][1]:
            rank = "1"
        elif ranking.iloc[10][ranking_entry] <= ranking.iloc[12][1]:
            rank = "2"
        elif ranking.iloc[10][ranking_entry] <= ranking.iloc[13][1]:
            rank = "3"
        elif ranking.iloc[10][ranking_entry] > ranking.iloc[13][1]:
            rank = "4"
        output_file_path = r"C:\Users\pauld\OneDrive\Documents\DSA\FYP\ScalabrinoDataset\Ranked_Snippets\\" \
                           + rank + r"\\" + os.path.basename(file[:-4] + "java")
        with open(file, 'r') as input_file_object, open(output_file_path, 'a') as output_file_object:
            try:
                for line in input_file_object:
                    output_file_object.write(line)
            except UnicodeDecodeError:
                output_file_object.close()
                os.remove(output_file_path)
        ranking_entry += 1


if __name__ == '__main__':
    scalabrino_ranking(input_code)