The input for our experiments are located in the folder data/non-sarcastic.txt

The generation for our paper is a three staged pipeline process

We convert a non-sarcastic utterance to a sarcastic

# R-3

conda create --name R3 python=3.6

conda activate R3

#point your LD_LIBRARY_PATH to your miniconda or anaconda library

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/nas/home/tuhinc/miniconda3/lib/



Clone this repo.

  - cd SarcasmGeneration-ACL2020
  - install nltk
  
  - <h1> To just reverse the valence of the input (REVERSE) </h1>
  
    - Run python reverse.py $input
    - This will print the output in the console

  
  - <h1> To retrieve the commonsense keyword associated with the input you need to do the below(RETRIEVE) </h1>
    - Download a chunk of the retreival corpus from the timestamp of the experiment from the link below and put inside data folder
      (https://drive.google.com/file/d/1cX-iy58B0F1K2nVD5sMiSIxd-8lFx7ok/view?usp=sharing) 
      
    - cd comet-commonsense
    
       To run the setup scripts to acquire the pretrained model files from OpenAI, as well as the ATOMIC and ConceptNet datasets

      ```
      bash scripts/setup/get_atomic_data.sh
      bash scripts/setup/get_conceptnet_data.sh
      bash scripts/setup/get_model_files.sh
      ```

      Then install dependencies (assuming you already have Python 3.6 ):

      ```
      pip install torch==1.3.1
      pip install tensorflow
      pip install ftfy==5.1
      conda install -c conda-forge spacy
      python -m spacy download en
      pip install tensorboardX
      pip install tqdm
      pip install pandas
      pip install ipython
      pip install inflect
      pip install pattern
      pip install pyyaml==5.1
      
      ```
      <h1> Making the Data Loaders </h1>

      Run the following scripts to pre-initialize a data loader for ATOMIC or ConceptNet:

      ```
      python scripts/data/make_atomic_data_loader.py
      python scripts/data/make_conceptnet_data_loader.py
      ```
      
      <h1> Download pretrained COMET </h1>
      
      First, download the pretrained models from the following link:

      ```
      https://drive.google.com/open?id=1FccEsYPUHnjzmX-Y5vjCBeyRt1pLo8FB
      ```

      Then untar the file:

      ```
      tar -xvzf pretrained_models.tar.gz
      
    
 Make sure your directory resembles this 
 https://github.com/tuhinjubcse/SarcasmGeneration-ACL2020/blob/master/comet-commonsense/directory.md
 
 
 
  - <h1> Finally to generate sarcasm , pick an utterance from data/non-sarcastic.txt and run the following command which inclueds REVERSE , RETRIEVE , RANK together </h1>
  
    - Run python generate_sarcasm.py $input
    - This will print the output in the console
    
 
 If you use code or data please cite us
 ```
       @article{chakrabarty2020r,
        title={$ R\^{} 3$: Reverse, Retrieve, and Rank for Sarcasm Generation with Commonsense Knowledge},
        author={Chakrabarty, Tuhin and Ghosh, Debanjan and Muresan, Smaranda and Peng, Nanyun},
        journal={arXiv preprint arXiv:2004.13248},
        year={2020}
      }
  ```
