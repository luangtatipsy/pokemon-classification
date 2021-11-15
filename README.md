# Pokémon Classification

# Datasets
- [pokemon-image-dataset](https://www.kaggle.com/hlrhegemony/pokemon-image-dataset) as a training set.
- [pokemon-images-and-types](https://www.kaggle.com/vishalsubbiah/pokemon-images-and-types) as a test set.

## Prerequisites
- Git
- Python 3.8.7

## Setup
0. Clone the repository
```sh
git clone https://github.com/luangtatipsy/pokemon-classification.git
cd intel-image-classification
```
1. Create and activate a virtual environment for Python _(recommended)_. If you do not prefer using a virtual environment, skip to step 4.
```sh
python -m venv env
source env/bin/activate
```
2. Update pip to latest version
```sh
python -m pip install --upgrade pip
```
3. Install requirements
```sh
python -m pip install -r requirements.txt
```
4. Download relevant datasets (as mentioned above) then, unzip archive files as directories below:
```
pokemon-classification
  datasets
    train
      Abomasnow
      Abra
      Absol
      ...
      Zygarde
      Zubat
      Zweilous
    test
      images
        abomasnow.png
        abra.png
        absol.png
        ...
        zygarde-50.png
        zweilous.png
        zubat.png
  ...
```
5. Run `prepare_dataset.py` to change test images coresponding to classes in the training set.
```sh
python prepare_dataset.py
```
