from scrapegraphai.graphs import OmniScraperGraph, OmniSearchGraph, SmartScraperGraph
import os
from dotenv import load_dotenv
def get_graph_config() -> dict:
    load_dotenv()

    graph_config = {
        "llm":{
            "api_key" : os.environ.get('OPENAI_API_KEY'),
            "model": "gpt-4o",
        }
    }
    return graph_config

def Omni_ScrapeGraph(prompt:str, source:str) -> str:
    omni_scrape_graph = OmniScraperGraph(
        prompt=prompt,
        source=source,
        config=get_graph_config(),
    )
    result = omni_scrape_graph.run()
    return result

def Omni_SearchGraph(prompt:str) -> str:
    omni_search_graph = OmniSearchGraph(
        prompt=prompt,
        config=get_graph_config(),
    )
    result = omni_search_graph.run()
    return result

def Smart_ScrapeGraph(prompt:str, source:str) -> str:
    smart_scrape_graph = SmartScraperGraph(
        prompt=prompt,
        source=source,
        config=get_graph_config(),
    )
    result = smart_scrape_graph.run()
    return result

