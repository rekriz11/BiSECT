import argparse

def read_file(filepath):
	data = []
	with open(filepath) as f:
		for line in f:
			data.append(line.strip())
	return data

def write_output(data, output_path):
	with open(output_path, 'w') as f:
		for d in data:
			f.write(d + "\n")

def main(args):
	train_complex = read_file(args.data_folder + "train.complex")
	train_simple = read_file(args.data_folder + "train.simple")
	train_dataset = read_file(args.data_folder + "train.dataset")

	original_test = {"complex": [], "simple": []}
	cr, sr = 0, 0
	for i, tc in enumerate(train_complex):
		if tc[-1] == ';':
			tc = tc[:-1] + '.'
			cr += 1
		ts = train_simple[i].replace(" _SPLIT_ ", " <SEP> ")
		ts = ts.replace("_SPLIT_ ", " <SEP> ")
		if ts[-1] == ';':
			ts = ts[:-1] + '.'
			sr += 1
		td = train_dataset[i]
		if td in ["jrc", "emea"]:
			original_test["complex"].append(tc)
			original_test["simple"].append(ts)
	print("Complex changes: {}, simple changes: {}".format(cr, sr))
	a = bbb

	print("\n{} original test complex, {} original test simple".format(len(original_test["complex"]), len(original_test["simple"])))

	write_output(original_test['complex'], args.output_folder + "test_original.complex")
	write_output(original_test['simple'], args.output_folder + "test_original.simple")



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compute model score...')
    parser.add_argument('-data_folder', type=str, required=True, help='Path to data')
    parser.add_argument('-output_folder', type=str, required=True, help='Path to write output')
    args = parser.parse_args()
    main(args)


'''
python challenge_set/find_original_test.py \
-data_folder /exp/rkriz/data/bisect/en-final/ \
-output_folder /exp/rkriz/data/bisect/challenge_set/
'''