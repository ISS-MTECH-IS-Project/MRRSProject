# Installation Guide on Linux

## Install Neo4j

- Run the below command to install prerequisite

```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```

- Add the GPG key for the official Neo4j package repository to your system

```bash
curl -fsSL https://debian.neo4j.com/neotechnology.gpg.key | sudo apt-key add -
```

- Add the Neo4j 4.4 repository to your APT

```bash
sudo add-apt-repository "deb https://debian.neo4j.com stable 4.4"
```

- Install Neo4j database

```bash
sudo apt install neo4j
```

- Start Neo4j service

```bash
sudo service neo4j start
```

- Update password
  - Open Neo4j browser http://localhost:7474/browser
  - Login with default username **neo4j** and default password **neo4j**
  - Update **neo123456** as new password _this is the default password used by the application_

## Install Anaconda (Optional)

If you have Python 3.9 environment ready, you can activate it and skip this step.

- Run the below command to download the Anaconda installer

```bash
wget https://repo.anaconda.com/archive/Anaconda3-2021.11-Linux-x86_64.sh
```

- Install Anaconda

```bash
bash Anaconda3-2021.11-Linux-x86_64.sh
```

Follow the guide to complete the installation.

- Create a new python 3.9.12 environment

```bash
conda create --name py39 python=3.9.12
```

- Activate the environment

```bash
conda activate py39
```

## Setup the application

- Download the code repository from github and save the code under ~/MRRSProject https://github.com/TeamEightIS04/MRRSProject
- Go to the SystemCode folder

```bash
cd ~/MRRSProject/SystemCode
```

- Install the dependencies (make sure the py39 environment is activated)

```bash
pip install sklearn spacy neo4j neomodel nltk pandas Flask flask_cors
```

- Setup the data in the DB

```bash
python dataSetup.py
```

- Verify the data in Neo4j http://localhost:7474/browser
- Start the application

```bash
flask run
```

- Open the application in browser http://localhost:5000
