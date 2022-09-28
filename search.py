def scopus_search(query):
    import requests as rq

    #This is the gate the API exposes:
    URL='https://api.elsevier.com/content/search/scopus'

    #These are the required parameters by the Scopus' API:
    header_params = {'apiKey':'f413a6b5f01f4ab8087dfce61b9b3c3f',
                    'httpAccept': 'application/json',
                    #This is the query, encoded with URL phrasing
                    'query': "KEY%28mouse+AND+NOT+cat+OR+dog%29"}





    #This is the GET call to the request instance:
    q = rq.get(URL,header_params)
    return q.json()