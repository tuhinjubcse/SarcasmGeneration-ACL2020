```bash
./comet-commonsense/
├── config
│   ├── atomic
│   │   ├── changes.json
│   │   ├── default.json
│   │   └── eval_changes.json
│   ├── conceptnet
│   │   ├── changes.json
│   │   ├── default.json
│   │   └── eval_changes.json
│   └── default.json
├── data
│   ├── atomic
│   │   ├── README.md
│   │   ├── sap2019atomic.pdf
│   │   ├── v4_atomic_all_agg.csv
│   │   ├── v4_atomic_all.csv
│   │   ├── v4_atomic_dev.csv
│   │   ├── v4_atomic_trn.csv
│   │   └── v4_atomic_tst.csv
│   └── conceptnet
│       ├── dev1.txt
│       ├── dev2.txt
│       ├── processed
│       │   └── generation
│       │       └── rel_language-trainsize_100-devversion_12-maxe1_10-maxe2_15-maxr_5.pickle
│       ├── test.txt
│       └── train100k.txt
├── LICENSE
├── model
│   ├── encoder_bpe_40000.json
│   ├── params_0.npy
│   ├── params_1.npy
│   ├── params_2.npy
│   ├── params_3.npy
│   ├── params_4.npy
│   ├── params_5.npy
│   ├── params_6.npy
│   ├── params_7.npy
│   ├── params_8.npy
│   ├── params_9.npy
│   ├── params_shapes.json
│   └── vocab_40000.bpe
├── parameters_names.json
├── pretrained_models
│   ├── atomic_pretrained_model.pickle
│   └── conceptnet_pretrained_model.pickle
├── pretrained_models.tar.gz
├── scripts
│   ├── classify
│   │   ├── classify_conceptnet_generations.py
│   │   ├── classify.sh
│   │   ├── convert_conceptnet_generations_to_text.py
│   │   └── demo_bilinear.py
│   ├── data
│   │   ├── make_atomic_data_loader.py
│   │   └── make_conceptnet_data_loader.py
│   ├── evaluate
│   │   ├── bleu_atomic.py
│   │   └── evaluate_atomic_generation_model.py
│   ├── generate
│   │   ├── generate_atomic_beam_search.py
│   │   ├── generate_atomic_greedy.py
│   │   ├── generate_atomic_topk.py
│   │   ├── generate_conceptnet_arbitrary.py
│   │   └── generate_conceptnet_beam_search.py
│   ├── interactive
│   │   ├── atomic_single_example.py
│   │   └── conceptnet_single_example.py
│   ├── novelty
│   │   └── compute_conceptnet_novelty.py
│   └── setup
│       ├── get_atomic_data.sh
│       ├── get_conceptnet_data.sh
│       └── get_model_files.sh
├── src
│   ├── data
│   │   ├── atomic.py
│   │   ├── conceptnet.py
│   │   ├── config.py
│   │   ├── data.py
│   │   ├── __pycache__
│   │   │   ├── atomic.cpython-36.pyc
│   │   │   ├── atomic.cpython-37.pyc
│   │   │   ├── conceptnet.cpython-36.pyc
│   │   │   ├── conceptnet.cpython-37.pyc
│   │   │   ├── config.cpython-36.pyc
│   │   │   ├── config.cpython-37.pyc
│   │   │   ├── data.cpython-36.pyc
│   │   │   ├── data.cpython-37.pyc
│   │   │   ├── utils.cpython-36.pyc
│   │   │   └── utils.cpython-37.pyc
│   │   └── utils.py
│   ├── evaluate
│   │   ├── atomic_evaluate.py
│   │   ├── conceptnet_evaluate.py
│   │   ├── conceptnet_generate.py
│   │   ├── evaluate.py
│   │   ├── generate.py
│   │   ├── __pycache__
│   │   │   ├── sampler.cpython-36.pyc
│   │   │   ├── sampler.cpython-37.pyc
│   │   │   ├── utils.cpython-36.pyc
│   │   │   └── utils.cpython-37.pyc
│   │   ├── sampler.py
│   │   └── utils.py
│   ├── interactive
│   │   ├── functions.py
│   │   └── __pycache__
│   │       ├── functions.cpython-36.pyc
│   │       └── functions.cpython-37.pyc
│   ├── main_atomic.py
│   ├── main_conceptnet.py
│   ├── main.py
│   ├── models
│   │   ├── gpt.py
│   │   ├── models.py
│   │   ├── __pycache__
│   │   │   ├── gpt.cpython-36.pyc
│   │   │   ├── gpt.cpython-37.pyc
│   │   │   ├── models.cpython-36.pyc
│   │   │   ├── models.cpython-37.pyc
│   │   │   ├── utils.cpython-36.pyc
│   │   │   └── utils.cpython-37.pyc
│   │   └── utils.py
│   └── train
│       ├── atomic_train.py
│       ├── batch.py
│       ├── conceptnet_train.py
│       ├── opt.py
│       ├── __pycache__
│       │   ├── batch.cpython-36.pyc
│       │   ├── batch.cpython-37.pyc
│       │   ├── utils.cpython-36.pyc
│       │   └── utils.cpython-37.pyc
│       ├── train.py
│       └── utils.py
├── temp
│   ├── input.json
│   ├── input.txt
│   ├── sent10.txt
│   ├── sent11.txt
│   ├── sent2.txt
│   ├── sent3.txt
│   ├── sent4.txt
│   ├── sent5.txt
│   ├── sent6.txt
│   ├── sent7.txt
│   ├── sent8.txt
│   ├── sent9.txt
│   └── sent.txt
└── utils
    ├── __pycache__
    │   ├── utils.cpython-36.pyc
    │   └── utils.cpython-37.pyc
    └── utils.py
 ```
