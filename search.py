def scopus_search(query):
    import requests as rq

    #This is the gate the API exposes:
    URL='https://api.elsevier.com/content/search/scopus'

    #These are the required parameters by the Scopus' API:
    header_params = {'apiKey':'your_key',
                    'httpAccept': 'application/json',
                    #This is the query, encoded with URL phrasing
                    #This one will return info about every paper in Scopus with Pipe sticking and prediction 
                    #in their titles... 
                    'query': 'TITLE("pipe sticking" AND "prediction")'} 


    #This is the GET call to the request instance:
    q = rq.get(URL,header_params)
    return q.json() #This gets the json from the q response object. 