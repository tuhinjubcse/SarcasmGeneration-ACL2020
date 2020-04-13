# R-3

conda create --name R3 python=3.6

conda activate R3

#point your LD_LIBRARY_PATH to your miniconda or anaconda library

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/nas/home/tuhinc/miniconda3/lib/


The input for our experiments are located in the folder data/non-sarcastic.txt

The generation for our paper is a three staged pipeline process

We convert a non-sarcastic utterance to a sarcastic

To do this follow the steps below



Clone this repo.

  - cd R-3
  - install nltk
  
  - <h1> To just reverse the valence of the input (REVERSE) </h1>
  
    - Run python reverse.py $input
    - This will print the output in the console

  
  - <h1> To just retrieve the commonsense keyword associated with the input (RETRIEVE) </h1>
  
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
      
    - Run python retrieve.py $input
    - Remember your directory should resemble this (https://github.com/PlusLabNLP/R-3/blob/master/comet-commonsense/README.md)
