# R-3

The input for our experiments are located in the folder data/non-sarcastic.txt

The generation for our paper is a three staged pipeline process

We convert a non-sarcastic utterance to a sarcastic

To do this follow the steps below

Clone this repo.

  - cd R-3
  - install nltk
  
  - To reverse the valence of the input (REVERSE) 
    - Run python reverse.py $input
    - This will print the output in the console , you can change it to output to a file
  
  - To retrieve the commonsense keyword associated with the input (RETRIEVE) follow below
  
    - cd comet-commonsense
    
       To run the setup scripts to acquire the pretrained model files from OpenAI, as well as the ATOMIC and ConceptNet datasets

      ```
      bash scripts/setup/get_atomic_data.sh
      bash scripts/setup/get_conceptnet_data.sh
      bash scripts/setup/get_model_files.sh
      ```

      Then install dependencies (assuming you already have Python 3.6 and Pytorch >= 1.0:

      ```
      pip install tensorflow
      pip install ftfy==5.1
      conda install -c conda-forge spacy
      python -m spacy download en
      pip install tensorboardX
      pip install tqdm
      pip install pandas
      pip install ipython
      ```
      <h1> Making the Data Loaders </h1>

      Run the following scripts to pre-initialize a data loader for ATOMIC or ConceptNet:

      ```
      python scripts/data/make_atomic_data_loader.py
      python scripts/data/make_conceptnet_data_loader.py
      ```
      
      First, download the pretrained models from the following link:

      ```
      https://drive.google.com/open?id=1FccEsYPUHnjzmX-Y5vjCBeyRt1pLo8FB
      ```

      Then untar the file:

      ```
      tar -xvzf pretrained_models.tar.gz

