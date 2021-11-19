#!/bin/sh
source "/exp/rkriz/venv/bin/activate"

DATA_FOLDER=$1
OUTPUT_FOLDER=$2

mkdir -p $OUTPUT_FOLDER

python challenge_set/find_original_test.py \
-data_folder $DATA_FOLDER \
-output_folder $OUTPUT_FOLDER


# ./challenge_set/create_challenge_set.sh /exp/rkriz/data/bisect/en-final/ /exp/rkriz/data/bisect/challenge_set/