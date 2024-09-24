import socket
import os
from dotenv import load_dotenv
from crewai_tools import tool
from crew_finance.crew_tools_project.Tool_finance import yf_get_stock_data

def recv_all(socket_instance, size):
    data = b''
    while True:
        part = socket_instance.recv(size)
        data += part
        if len(part) < size:
            break
    return data.decode()

def send_all(socket_instance, data, size):
    data = data.encode()
    for i in range(0, len(data), size):
        socket_instance.sendall(data[i:i+size])

def server_interaction(msg):
    load_dotenv()
    # What tools they use?
    print(msg)
    HOST = os.environ.get('SERVER_IP')
    PORT = int(os.environ.get('SERVER_PORT'))
    SIZE = 1024
    ADDR = (HOST, PORT)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tool_socket:
        try:
            tool_socket.connect(ADDR)
            print("Tool client connected to server at", ADDR)

            send_all(tool_socket, msg, SIZE)
            response = recv_all(tool_socket, SIZE)
            return response
        except Exception as e:
            return "Something went wrong." + str(e)

    



@tool('algorithms_show')
def algorithms_show():
    """
    Returns a list of available algorithm names that can be searched for. 
    
    
    Args:
        Don't pass arguments to this function.
        
    Usage:
        Call this function to get a list of algorithms. 
        Then use 'algorithm_search' to retrieve the code for a specific algorithm.

    Example:
        algorithms = algorithms_show()
        return algorithms
    """
    msg = 'algorithms_show:'
    output = server_interaction(msg)
    return output


@tool('yf_stock_data')
def yf_stock_data(ticker:list[str], interval:str) -> str:
    """
    Returns the yahoo finance stock data
    
    Args:
        symbol: The stock symbol that you want to know
        interval: The interval of the data (e.g., '1m','2m','5m','15m','30m','60m','90m','1h','1d','5d','1wk','1mo','3mo')
        
    Example 1:
        data = yf_stock_data(['AAPL'], '1d')
        return data
        
    Example 2:
        data = yf_stock_data(['AAPL','MSFT'], '5d')
        return data
    """
    output = yf_get_stock_data(ticker=ticker, interval=interval)
    return output

@tool('algorithm_search')
def algorithm_search(algorithm:str) -> str:
    """
    Retrieves the code for a specific algorithm from the-algorithms.com.

    Args:
        algorithm: The name of the algorithm to search for (e.g., 'quick-sort').

    Usage:
        First, call 'algorithms_show' to get a list of available algorithms.
        Then pass a valid algorithm name from that list to this function.

    Example:
        code = algorithm_search('bubble-sort')
        return code
    """
    msg = 'algorithm_search:' + algorithm
    output = server_interaction(msg)
    return output



"""@tool('DocsSearch')
def DocsSearch(instruction:str) -> str:
    Useful to search a query from a Docs content. Just pass the instruction about the code docs content.
    msg = 'DocsSearch:' + instruction
    output = server_interaction(msg)
    return output
    """


"""@tool('alphavantage_get_stock_data')
def alphavantage_get_stock_data(symbol:str) -> str:
    Returns the alphavantage stock data
    
    Args:
        symbol: The stock symbol that you want to know (e.g., 'AAPL')
    
    Example:
        data = alphavantage_get_stock_data('AAPL')
        return data
    msg = 'alphavantage_get_stock_data:' + symbol
    output = server_interaction(msg)
    return output"""

@tool('Serper_Search')
def serper_search(query:str) -> str:
    """
    Search the query in the Serper Search Engine.
    
    Args:
        query: The query to search in the Serper Search Engine. (e.g., 'Give me full documentation from Finhub API')
        
    Example:
        data = serper_search('Tell me about LSTM python code')
        return data
    """
    msg = 'Serper_Search:' + query
    output = server_interaction(msg)
    return output

@tool('Serper_news_Search')
def Serper_news_Search(query:str) -> str:
    """
    Search the query in the Serper News Search Engine.
    
    Args:
        query: The query to search in the Serper News Search Engine. (e.g., 'What's the most influential technical indicator?')
        
    Example:
        data = Serper_news_Search('What's the most influential technical indicator?')
        return data
    """
    msg = 'Serper_news_Search:' + query
    output = server_interaction(msg)
    return output

@tool('Serper_Scholar_Search')
def Serper_Scholar_Search(query:str) -> str:
    """
    Search the query in the Serper Scholar Search Engine.
    
    Args:
        query: The query to search in the Serper Scholar Search Engine. (e.g., What's the best perfomance models for stock prediction?')
    
    Example:
        data = Serper_Scholar_Search('What's the best perfomance models for stock prediction?')
        return data
    """
    msg = 'Serper_Scholar_Search:' + query
    output = server_interaction(msg)
    return output

    
@tool('exa_search')
def exa_search(query:str) -> str:
    """
    Search the exa content based on the query.
    
    Args:
        query: The query to search in exa content. (e.g., 'Give me python code LSTM for stock prediction')
        
    Example:
        data = exa_search('Give me python code LSTM for stock prediction')
        return data
    """
    msg = 'exa_search:' + query
    output = server_interaction(msg)
    return output


@tool('exa_find_similar')
def exa_find_similar(url:str) -> str:
    """
    Find the similar content based on the url.
    
    Args:
        url: The url to find the similar content. (e.g., 'https://www.exa.com/stock-prediction')
    
    Example:
        data = exa_find_similar('https://www.exa.com/stock-prediction')
        return data
    """
    msg = 'exa_find_similar:' + url
    output = server_interaction(msg)
    return output


"""@tool('Omni_SearchGraph')
def Omni_SearchGraph(query:str) -> str:
    
    Search the query in the Omni Search Graph.
    
    Args:
        query: The query to search in the Omni Search Graph. (e.g., 'Give me full documentation at Alphavantage')
    
    Example:
        data = Omni_SearchGraph('Tell me about LSTM')
        return data
    
    msg = 'Omni_SearchGraph:' + query
    output = server_interaction(msg)
    return output"""

"""@tool('Omni_ScrapeGraph')
def Omni_ScrapeGraph(url:str, query:str) -> str:
    
    Scrape the url and search the query in the Omni Search Graph.
    
    Args:
        url: The url to scrape and search
        query: The query to search in the Omni Search Graph. (e.g., 'Give me robust accuracy AI model name for stock prediction in github')
        
    Example:
        data = Omni_ScrapeGraph('https://www.example.com', 'Give me robust accuracy AI model name for stock prediction in github')
        return data
    """
    
