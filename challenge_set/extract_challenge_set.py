import argparse
from collections import Counter

def read_file(filepath):
	data = []
	with open(filepath) as f:
		for line in f:
			data.append(line.strip().split("\t"))
	return data

def write_output(data, output_path):
	with open(output_path, 'w') as f:
		for d in data:
			f.write(d + "\n")

def main(args):
	labeled_test_data = read_file(args.labeled_test_file)

	original_test = {"complex": [], "simple": []}
	length_diffs, source_endings, target_endings = 0, [], []
	for i, instance in enumerate(labeled_test_data):
		if int(instance[3]) == 3:
			if len(instance[0].split()) < 0.8 * len(instance[2].split()) or len(instance[2].split()) < 0.8 * len(instance[0].split()):
				#print("\nComplex: {}\nSplit: {}".format(instance[0], instance[2]))
				length_diffs += 1
			elif instance[0][-1] not in ['.', '?', '!']:
				source_endings.append(instance[0][-1])
			elif instance[2][-1] not in ['.', '?', '!']:
				target_endings.append(instance[2][-1])
			else:
				original_test['complex'].append(instance[0])
				original_test['simple'].append(instance[2])
	print("Source Endings: {}".format(source_endings))
	print("Source Endings: {}, Target Endings: {}".format(dict(Counter(source_endings)), dict(Counter(target_endings))))

	print("Length diffs: {}, Not complete source: {}, Not complete target: {}".format(length_diffs, len(source_endings), len(target_endings)))


	print("\n{} challenge test complex, {} challenge test simple".format(len(original_test["complex"]), len(original_test["simple"])))

	write_output(original_test['complex'], args.output_folder + "challenge_test.src")
	write_output(original_test['simple'], args.output_folder + "challenge_test.dst")



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compute model score...')
    parser.add_argument('-labeled_test_file', type=str, required=True, help='Path to labeled test data')
    parser.add_argument('-output_folder', type=str, required=True, help='Path to output folder')
    args = parser.parse_args()
    main(args)


'''
python challenge_set/extract_challenge_set.py \
-labeled_test_file data/challenge_set/test_original.labels \
-output_folder data/challenge_set/
'''