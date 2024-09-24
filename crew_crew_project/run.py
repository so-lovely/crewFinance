from Agents import StockPricePredictionAgents as Agents
from Tasks import Stock_Tasks as Tasks
from crewai import Crew, Process
from dotenv import load_dotenv
#from langchain_openai import ChatOpenAI
import os



if __name__ == '__main__':
    load_dotenv()
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    os.environ["OPENAI_MODEL_NAME"]="gpt-4o"
    Agent = Agents()
    Data_Agent = Agent.get_Data_Ingestion_Agent()
    Market_Analyst = Agent.get_Market_Analyst()
    Sentiment_Analyst = Agent.get_Sentiment_Analyst()
    AI_Model_Developer = Agent.get_AI_Model_Developer()
    Model_Ensemble_Agent = Agent.get_Model_Ensemble_Agent()
    Risk_Manager = Agent.get_Risk_Manager()
    Project_Manager = Agent.get_Model_Project_Manager()
    Task = Tasks(Data_Agent, Market_Analyst, Sentiment_Analyst, AI_Model_Developer, Model_Ensemble_Agent, Risk_Manager, Project_Manager)
    # Tasks
    Market_Analysis = Task.get_Task_Market_Analysis()
    Sentiment_Analysis = Task.get_Task_Sentiment_Analysis()
    AI_Modeling = Task.get_Task_AI_Modeling()
    Model_Ensemble = Task.get_Task_Model_Ensemble()
    Manage_Project = Task.get_Task_Manage_Project()
    Data_Ingestion = Task.get_Task_Data_Ingestion()
    Risk_Management = Task.get_Task_Risk_Management()
    
    
    crew = Crew(
        agents = [Data_Agent, Market_Analyst, Sentiment_Analyst, AI_Model_Developer, Model_Ensemble_Agent, Risk_Manager],
        tasks = [Market_Analysis, Sentiment_Analysis, AI_Modeling, Model_Ensemble, Manage_Project, Data_Ingestion, Risk_Management],
        full_output=True,
        verbose=2,
        process = Process.hierarchical,
        manager_agent=Project_Manager,
        cache=True,
        memory=True,
        output_log_file=True
    )
    result = crew.kickoff()
    print(result)
    with open ('result.csv', 'w') as f:
        f.write(result)