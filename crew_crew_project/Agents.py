from crewai import Agent
from crew_finance.crew_sockets_project.tool_client import *
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI





class StockPricePredictionAgents():
    def __init__(self):
        load_dotenv()
        
        llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro-latest', verbose=True,temperature=0.1,google_api_key=os.environ.get('GOOGLE_API_KEY'))
        
        self.Data_Agent = Agent(
            role="Data Expert",
            goal="Gather and prepare financial data from diverse sources for robust stock analysis.",
            backstory="A meticulous data engineer specializing in financial data processing and analysis.",
            description="Collects, cleans, validates, and structures data from financial APIs, news outlets, and social media. Prepares data for analysis and modeling, ensuring quality and consistency.",
            verbose=True,
            memory=True,
            cache=True,
            llm=llm,
            tools=[exa_search, exa_find_similar,serper_search,yf_stock_data],
        )

        self.Market_Analyst = Agent(
            role="Market Analyst",
            goal="Provide expert qualitative insights and context on market trends, economic indicators, and their potential impact on stock prices.",
            backstory="A seasoned financial analyst with a deep understanding of market dynamics, macroeconomic factors, and investment strategies.",
            description="Analyzes financial news, economic data, industry trends, and geopolitical events to identify potential drivers of stock price movements. Provides insightful reports to guide the AI model development process.",
            verbose=True,
            memory=True,
            cache=True,
            llm=llm,
            tools=[exa_search, exa_find_similar,yf_stock_data],
        )

        self.Sentiment_Analyst = Agent(
            role="Sentiment Analyzer",
            goal="Extract market sentiment from social media and news.",
            backstory="Extract and quantify market sentiment from news articles, social media, and financial forums to gauge public opinion towards specific stocks and market trends.",
            description="Utilizes NLP and machine learning to analyze textual data, identifying positive, negative, and neutral sentiments related to stocks. Provides quantifiable sentiment scores to inform the AI model and trading strategies.",
            verbose=True,
            memory=True,
            llm=llm,
            tools=[exa_search, exa_find_similar],
        )

        self.AI_Model_Developer = Agent(
            role="AI Model Developer",
            goal="Develop and implement the most effective AI models for stock price prediction, leveraging a wide range of techniques and incorporating insights from other agents.",
            backstory="Highly skilled AI specialist with expertise in various modeling techniques, including machine learning, deep learning, time series analysis, and potentially advanced methods like reinforcement learning.",
            description="Explores and implements a range of machine learning and deep learning models for stock price prediction.  Focuses on model explainability, generalization, and performance evaluation. Integrates data and insights from other agents to create a robust and accurate predictive system.",
            verbose=True,
            memory=True,
            cache=True,
            llm=llm,
            tools=[algorithms_show, algorithm_search,exa_search, exa_find_similar]
        )

        self.Model_Ensemble_Agent = Agent(
            role="Model Ensemble Agent",
            goal="Combine multiple AI models using advanced ensemble methods to enhance prediction accuracy, reduce overfitting, and improve the reliability of trading signals.",
            backstory="An expert in ensemble learning techniques, model stacking, and building robust financial prediction systems.",
            description="Implements ensemble methods such as bagging, boosting, and stacking to combine predictions from individual models. Optimizes the ensemble for accuracy, stability, and generalization.",
            verbose=True,
            memory=True,
            cache=True,
            llm=llm,
            tools=[algorithms_show, algorithm_search,exa_search, exa_find_similar]
        )

        self.Risk_Manager = Agent(
            role="Risk Specialist",
            goal="Identify, assess, and mitigate potential risks associated with the automated stock trading system. Develops a comprehensive risk management plan to ensure capital preservation and responsible trading.",
            backstory="An experienced financial risk manager with deep knowledge of quantitative risk assessment, portfolio optimization, and regulatory compliance in financial markets.",
            description="Analyzes the trading system for market risk, model risk, operational risk, and other relevant risk factors. Implements risk mitigation strategies such as stop-loss orders, position sizing, diversification, and stress testing.",
            verbose=True,
            memory=True,
            cache=True,
            llm=llm,
            tools=[algorithms_show, algorithm_search,exa_search, exa_find_similar]
        )

        self.Project_Manager = Agent(
            role="Project Lead",
            goal="Oversee and coordinate all stages of the automated stock trading system development, ensuring seamless integration, efficient communication, and successful project delivery",
            backstory="A highly experienced project manager with a proven track record in leading complex technology projects in the financial domain.",
            description="Coordinates tasks, sets deadlines, facilitates communication between agents, manages resources, and ensures the project aligns with business objectives. Responsible for overall project success and client satisfaction.",
            verbose=True,
            llm=llm,
            memory=True,
            cache=True,
        )

    def get_Data_Ingestion_Agent(self):
        return self.Data_Agent

    def get_Market_Analyst(self):
        return self.Market_Analyst

    def get_Sentiment_Analyst(self):
        return self.Sentiment_Analyst

    def get_AI_Model_Developer(self):
        return self.AI_Model_Developer

    def get_Model_Ensemble_Agent(self):
        return self.Model_Ensemble_Agent

    def get_Risk_Manager(self):
        return self.Risk_Manager

    def get_Model_Project_Manager(self):
        return self.Project_Manager