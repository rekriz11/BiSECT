#!/bin/sh
source "/exp/rkriz/venv/bin/activate"

DATA_FOLDER=$1
OUTPUT_FOLDER=$2
echo "DATA_FOLDER: ${DATA_FOLDER}"
echo "OUTPUT_FOLDER: ${OUTPUT_FOLDER}"
mkdir -p $OUTPUT_FOLDER

python challenge_set/find_original_test.py \
-data_folder $DATA_FOLDER \
-output_folder $OUTPUT_FOLDER

cd our_model/preprocess/classifier/

python classifier.py \
-r "${OUTPUT_FOLDER}/test.complex" \
-s "${OUTPUT_FOLDER}/test.simple" \
-o "${OUTPUT_FOLDER}/test.labels"

# ./challenge_set/create_challenge_set.sh /exp/rkriz/data/bisect/en-final/ /exp/rkriz/data/bisect/challenge_set/
