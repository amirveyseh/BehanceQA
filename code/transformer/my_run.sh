# python run_ner_no_trainer.py \
#   --model_name_or_path bert-base-cased \
#   --train_file ../data/processed/train.json \
#   --validation_file ../data/processed/dev.json \
#   --task_name ner \
#   --per_device_train_batch_size 32 \
#   --learning_rate 2e-5 \
#   --num_train_epochs 3 \
#   --output_dir ../data/processed/model


CUDA_VISIBLE_DEVICES=1 python3 run_ner_no_trainer.py \
  --model_name_or_path bert-base-cased \
  --train_file ../../data/processed/train.json \
  --validation_file ../../data/processed/dev.json \
  --output_dir ../../data/processed/model \
  --per_device_eval_batch_size 6 \
  --per_device_train_batch_size 6 \
