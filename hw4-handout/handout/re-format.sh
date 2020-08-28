INPUT_DIR=bert_input_data
rm -rf $INPUT_DIR
mkdir -p $INPUT_DIR

sed 's/\([^,]*\),\(.*\)/\2/' ./data/lang_id_eval.csv > ./bert_input_data/eval.csv
sed 1d ./bert_input_data/eval.csv > ./bert_input_data/eval.txt
rm ./bert_input_data/eval.csv



sed 's/\([^,]*\),\(.*\)/\2/' ./data/lang_id_train.csv > ./bert_input_data/train.csv
sed 1d ./bert_input_data/train.csv > ./bert_input_data/train.txt
rm ./bert_input_data/train.csv



sed 's/\([^,]*\),\(.*\)/\2/' ./data/lang_id_test.csv > ./bert_input_data/test.csv
sed 1d ./bert_input_data/test.csv > ./bert_input_data/test.txt
rm ./bert_input_data/test.csv

echo "Done."
echo "Press Enter."
read x