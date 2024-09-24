import os
from exa_py import Exa
from dotenv import load_dotenv
def exa_search(query:str):
    load_dotenv()
    exa = Exa(os.environ.get('EXA_API_KEY'))
    results = exa.search_and_contents(
        query=query,
        start_published_date='2021-01-01',
        use_autoprompt=True
    )
    results = str(results)
    return results

def exa_find_similar(url:str):
    load_dotenv()
    exa = Exa(os.environ.get('EXA_API_KEY'))
    results = exa.find_similar_and_contents(
        url=url,
        num_results=3,
        start_published_date='2021-01-01',
    )
    results = str(results)
    return results




