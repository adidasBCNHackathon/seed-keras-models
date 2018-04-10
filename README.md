# SEED AI models

## Must have

- [python 3.x](https://www.python.org/downloads/)
- pip3
- [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html) *If you are using windows powershell it might not work unless you run it with CMD*
- [anaconda](https://anaconda.org/anaconda/python)

** Use anaconda or virtualenvwrapper

## Set workspace

```bash
# with virtualenvwrapper
$ mkvirtualenv -p python3 bot # create virtual environment
$ workon bot # enter VE
(bot) $ pip install -r requirements.txt # install dependencies (make sure you are in the bot VE)
(bot) $ deactivate # exit VE

# with anaconda
$ conda env create -f environment.yml # create virtual environment
$ conda activate bot # enter VE
(bot) $ conda deactivate # exit VE
```

## Run

```bash
(bot) $ python -m pkg_name.cmd -h # to train the pkg

(bot) $ python -m api # to run the api endpoint to predict
```

## Folder Structure

Split each NN into different packages

```bash
.
├── README.md
├── api.py # main API handler
├── requirements.txt
├── setup.py # package information
├── pkg_name # summarizer PKG
│   ├── __init__.py
│   ├── api.py # API to consume the model predictions
│   ├── cmd.py # CLI to train the model
│   ├── model.py # Keras model
│   └── task.py # training logic
└── utils # commons
    └── __init__.py
```
