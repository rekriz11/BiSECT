import argparse

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
	for i, instance in enumerate(labeled_test_data):
		if int(instance[3]) == 3:
			original_test['complex'].append(instance[0])
			original_test['simple'].append(instance[2])


	print("\n{} original test complex, {} original test simple".format(len(original_test["complex"]), len(original_test["simple"])))

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
-data_folder data/challenge_set/ \
-output_folder data/challenge_set/
'''