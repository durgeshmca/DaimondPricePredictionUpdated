#Machine Learning Project 
#Daimond Price Prediction

Download and Install anaconda
in ubuntu to install run 
bash DOWNLOADED_FILE.sh 
To run anaconda base environment
run following command
conda activate
now change to the project directory
open vscode by running following command
code .
create requirements.txt
create new environment
conda create venv python=3.8 
venv is the environment name and 3.8 is the python version specific environment
Now activate the venv environment by running following command
conda activate venv/

create setup.py
add following code

---------------------------------------------------------------
from setuptools import setup,find_packages
from typing import List

HYPHON_E_DOT = '-e .'
def get_requirements(file_path:str)->List:
    with open(file_path) as fp:
        requirements = fp.readlines()
        reqList = [req.replace('\n','') for req in requirements]
        if HYPHON_E_DOT in reqList:
            reqList.remove(HYPHON_E_DOT)

    return reqList



setup(
    name="DaimondPricePrediction",
    version='0.0.1',
    author="Durgesh Chandra Mishra",
    author_email="durgeshcmishra@live.in",
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)

-------------------------------------------------------------------

run
python setup.py install

Alternatively you can add a line in requirements.txt as
-e .

By adding this line you can install the required package by installing using requirements.txt
pip install -r requirements.txt
