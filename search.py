import pandas as pd
import json

def scopus_search():
    import requests as rq
    
    #This is the gate the API exposes:
    URL='https://api.elsevier.com/content/search/scopus'

    #These are the required parameters by the Scopus' API:
    header_params = {'apiKey':'my_key',
                    'httpAccept': 'application/json',
                    #This is the query, encoded with URL phrasing
                    #This one will return info about every paper in Scopus with Pipe sticking and prediction 
                    #in their titles... 
                    'query': 'KEY(keyword) AND TITLE(titleword)'}


    #This is the GET call to the request instance:
    q = rq.get(URL,header_params)
    
    return q.json() #This gets the json from the q response object.

def tabular_results(q):
    ''' Used for creating a DataFrame of the JSON file. 
    '''
    df = pd.DataFrame(q['search-results']['entry'])
    df.rename(columns={"dc:title":"Title", 
                       "dc:creator": "Author", 
                       'prism:publicationName':'Platform', 
                       'subtypeDescription':'Type',
                       'prism:coverDate':'Date',
                       'prism:doi':'DOI'},inplace=True)

    Results = df[['Date','Title', 'Author', 'Platform', 'Type', 'DOI']].copy()
    Results['DOI']='https://doi.org/'+Results['DOI']
    Results.sort_values(by='Date')
    Results.set_index('Date', inplace=True)
    pd.set_option('display.max_colwidth', None)
    return Results

q_json = scopus_search()
table = tabular_results(q_json)

# table.to_csv('Searched_Articles.csv')
