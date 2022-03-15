[ IMPORTANT ]

1) This conda environment MUST be run in Ubuntu 20.04.
2) Conda must be installed.
3) Python 3.7.11 is used in this environment to get best compatibilities with all required software.
4) The name of this conda environment is "oohfish-env". This conda environment must be activated first, followed by the virtual environment as explained in the flask section below.
5) Virtual environment is used within this conda environment so it must be activated after the conda environment is activated. All packages are installed in the virtual environment.
    This should be taken care of in the "unpack-env.sh" script.
6) The following has been tested successfully in this environment:
    a) Spacy and NLTK
    b) ChatterBot
    c) Bert (sentence comparison)
7) To deactivate the virtual environment, type "deactivate" at the shell prompt.
8) To deactivate the conda environment, type "conda deactivate". Deactivate virtual environment first then conda environment.


[ To unpack the environment ]

1) Download the two tar.gz files and the "unpack-env.sh" file into a directory of your choice. 
    Please ensure you have at least 3 GB of available space for the compressed and uncompressed files. 
2) Run the script "unpack-env.sh" to unpack both compressed files.


[ Flask ]

1) At the "oohfish_app" directory, activate virtual environment by typing ". venv/bin/activate".
2) Start the Flask server by typing "./start.sh" at the "oohfish_app" directory.
3) The HTML files should be placed in "flaskr/templates" directory.
4) The "tests" directory contains a testBert.py script that I wrote for testing the environment.
5) Server-side scripts should be placed under the "flaskr" directory.
6) I wrote a simple "testGraphDB.py" server-side script in "flaskr" directory that tests the query to the neo4j graph database and output the result to the web page.
    The neo4j database must be started first. Then after starting the flask web server, type this URL to access the example: http://localhost:5000/testGraphDB/symptom.
7) The credentials to the neo4j graph database can be changed in the "db.py" file. The database can be indicated in the session method.
8) The "software_list.txt" file contains version of the major software installed
