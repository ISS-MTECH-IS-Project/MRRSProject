#pip install sklearn

#import library
from operator import index
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import os

def getBOW(file_name='FishDB_Symptom.csv', index_col='ID'):
    # get folder path
    file_path = os.getcwd()
    if os.name == 'posix':
        file_path += "/RawCSV/"
    else:
        file_path +=  "\\RawCSV\\" 
    
    # read csv into Dataframe
    symptom_df = pd.read_csv(file_path + file_name, encoding="ISO-8859-1", index_col=index_col)

    # read 'Symptom' column in array
    symptom_array = []
    for i in range(1, symptom_df.shape[0]+1):
        if symptom_df.loc[i, 'Symptom']:
            symptom_array.append(symptom_df.loc[i, 'Symptom'])

    # instantiate CountVectorizer
    vectorizer = CountVectorizer(stop_words='english')

    # fit vectorizer to get bag-of-words vector then convert it to dataframe
    X = vectorizer.fit_transform(symptom_array)
    bow_df = pd.DataFrame(X.toarray(),columns=vectorizer.get_feature_names())
    print('Bag-of-words vectorization completed - dataframe of shape ', bow_df.shape) 
    
    return bow_df

def getGlossary(file_name='FishDB_Symptom.csv', index_col='ID'):
    # get Bag-of-words dataframe by calling the getBOW function
    bow_df = getBOW(file_name=file_name, index_col=index_col)
    bow_df[bow_df.columns] = bow_df[bow_df.columns].astype(int)

    # get count for each of the words (cols in bow_df) and return a df where col 1 is word and col 2 is word count
    wordcount = bow_df.sum(axis=0)
    wordcount_df = wordcount.to_frame()
    wordcount_df.columns = ['count']

    # get folder path
    file_path = os.getcwd()
    if os.name == 'posix':
        file_path += "/RawCSV/"
    else:
        file_path +=  "\\RawCSV\\" 

    # write df to csv file
    csv_filename = 'SymptomsGlossary.csv'
    wordcount_df.to_csv(file_path+csv_filename, header=False)
    print('SymptomsGlossary.csv updated!')


