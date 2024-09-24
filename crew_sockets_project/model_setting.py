from crew_finance.crew_tools_project.Tool_algorithms import show_algorithms, show_algorithm_code
from crew_finance.crew_tools_project.Tool_finance import *
from crew_finance.crew_tools_project.Tool_exa_search import exa_search, exa_find_similar
from crew_finance.crew_tools_project.Tool_scrapegraph import *
from crew_finance.crew_tools_project.Tool_serper import *

# Omni_SearchGraph, fetch_timesfm, fetch_pattern_detection_yola8, fetch_repo1, fetch_repo2, fetch_repo3, fetch_repo4, fetch_repo5, fetch_repo6, fetch_repo7, fetch_repo8, fetch_repo9, fetch_repo10, fetch_repo11, fetch_repo12, fetch_repo13, fetch_repo14, fetch_repo15
def function_callback(function:str, instruction:str) -> str:
    if function == 'algorithms_show':
        algorithms = show_algorithms()
        algorithms = str(algorithms)
        return algorithms
    
    elif function == 'algorithm_search':
        algorithm = show_algorithm_code(instruction)
        return algorithm
    elif function =='Serper_news_Search':
        search_result = Serper_news_Search(instruction)
        return search_result
    
    elif function =='Serper_Scholar_Search':
        search_result = Serper_Scholar_Search(instruction)
        return search_result
    
    elif function == 'Serper_Search':
        search_result = Serper_Search(instruction)
        return search_result
    #elif function == 'alphavantage_get_stock_data':
        #data = alphavantage_get_stock_data(instruction)
        #return data
    elif function == 'exa_search':
        search_result = exa_search(instruction)
        return search_result
    elif function == 'exa_find_similar':
        search_result = exa_find_similar(instruction)
        return search_result
    elif function == 'Omni_SearchGraph':
        search_result = Omni_SearchGraph(instruction)
        return search_result
    elif function == 'Omni_ScrapeGraph':
        search_result = Omni_ScrapeGraph(instruction)
        return search_result
    
    else:
        return 'tool_name not found'
        