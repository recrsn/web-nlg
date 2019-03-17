mkdir nmt_model
cd nmt
python3 -m nmt.nmt \
    --src=triples --tgt=en \
    --vocab_prefix=../data/v2_cooked/vocab \
    --train_prefix=../data/v2_cooked/train.json \
    --dev_prefix=../data/v2_cooked/dev.json  \
    --test_prefix=../data/v2_cooked/test.json \
    --out_dir=../nmt_model \
    --num_train_steps=12000 \
    --steps_per_stats=100 \
    --num_layers=2 \
    --num_units=128 \
    --dropout=0.2 \
    --metrics=bleu
