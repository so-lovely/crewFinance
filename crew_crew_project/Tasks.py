from crewai import Task
from dotenv import load_dotenv
from textwrap import dedent
from crew_finance.crew_sockets_project.tool_client import *

# Data_Agent, Market_Analyst, Sentiment_Analyst, Machine_Learner, Model_Ensemble_Agent, Risk_Manager, Project_Manager
# Data_Ingetstion_Agent + Machine_Learning_Specialist + Model_Ensember_Agent
# Risk_Manger + Project_Manager
# Market_Analyst + Sentiment_Analyst + Project_Manager
class Stock_Tasks():
    def __init__(self, Data_Agent, Market_Analyst, Sentiment_Analyst, Machine_Learner, Model_Ensemble_Agent, Risk_Manager, Project_Manager):
        load_dotenv()
        self.Data_Agent = Data_Agent
        self.Market_Analyst = Market_Analyst
        self.Sentiment_Analyst = Sentiment_Analyst
        self.Machine_Learner = Machine_Learner
        self.Model_Ensemble_Agent = Model_Ensemble_Agent
        self.Risk_Manager = Risk_Manager
        self.Project_Manager = Project_Manager
        self.Task_Market_Analysis = Task(
            description =dedent(f"""
                ## Task: Market Analysis
                **Objective:** Identify key market trends, economic indicators, and industry-specific factors that could impact stock prices. 

                **Instructions:**
                1. Analyze historical stock price data for relevant patterns, trends, and anomalies.
                2. Research and analyze economic indicators (e.g., interest rates, inflation, GDP growth) relevant to the target stocks or sectors.
                3. Stay informed about major news events, geopolitical developments, and regulatory changes that can influence market sentiment.
                4. Provide a concise and insightful report summarizing your findings, highlighting key trends and their potential impact on stock prices.

                **Deliverable:** A comprehensive report on market trends and influential factors. 
            """),
            expected_output = "Report on market trends and influential factors",
            output_file = 'Market_Analysis_Report.txt',
            agent = self.Market_Analyst, 
            tools = [exa_search, exa_find_similar,yf_stock_data],
        )
        
        self.Task_Sentiment_Analysis = Task(
            description = dedent(f"""
                 **Objective:** Analyze market sentiment from news articles, social media posts, and financial forums to predict potential stock price movements.

                **Instructions:**
                1. Collect a comprehensive dataset of news articles, social media posts, and financial forum discussions related to the target stocks.
                2. Develop and apply sentiment analysis models to classify the sentiment expressed in the collected data as positive, negative, or neutral.
                3. Quantify the overall sentiment towards each target stock and identify any emerging trends or shifts in sentiment.
                4. Correlate sentiment data with historical stock price movements to assess the predictive power of sentiment analysis.
                5. Provide a detailed report summarizing the sentiment analysis findings and their potential impact on stock prices.

                **Deliverable:** A comprehensive report detailing market sentiment and its predicted impact on stock prices.

            """),
            expected_output = "Report on sentiment trends for target stocks",
            agent = self.Sentiment_Analyst,
            output_file = 'Sentiment_Analysis_Report.txt',
            tools = [exa_search, exa_find_similar],
        )
        
        self.Task_AI_Modeling = Task(
            description = dedent(f"""
                ## Task: AI Model Development
                **Objective:** Develop a robust and accurate AI model for predicting stock prices, incorporating insights from the Data Expert, Market Analyst, and Sentiment Analyst.

                **Instructions:**
                1. Access and utilize the processed financial data provided by the Data Expert.
                2. Integrate the market analysis insights and sentiment scores from the respective agents to enrich the feature set of the AI model.
                3. Explore and evaluate a diverse range of machine learning and deep learning models for time series forecasting, such as ARIMA, LSTM, Prophet, or Transformers.
                4. Fine-tune the hyperparameters of the chosen models and optimize them for key performance metrics, including accuracy, precision, recall, and F1-score.
                5. Implement appropriate techniques to prevent overfitting, such as cross-validation, regularization, and dropout.
                6. Develop a clear and concise API for the AI model to generate predictions for new, unseen data.
                7. Provide well-documented and modular Python code for the AI model, making it easy to understand, maintain, and integrate into the larger trading system.

                **Deliverable:** Python code for an AI-powered stock prediction model.
                
                **Participants:** AI Model Developer, Data Expert, Market Analyst, Sentiment Analyst, Project Manager
            """),
            expected_output = "Python code for an AI stock prediction model with trading signals",
            agent = self.Machine_Learner,
            output_file = 'AI_Stock_Prediction_Model.py',  
            tools = [algorithms_show, algorithm_search,exa_search, exa_find_similar],
            async_execution=False,
        )
        self.Task_Model_Ensemble = Task(
            description = dedent(f"""
                ## Task: Model Ensemble
                **Objective:** Combine multiple AI models developed by the AI Model Developer into a more robust and accurate ensemble model. 

                **Instructions:**
                1. Receive and analyze the individual AI models developed by the AI Model Developer.
                2. Implement ensemble methods such as bagging, boosting, or stacking to combine the predictions of the individual models. 
                3. Evaluate the performance of the ensemble model against a holdout dataset and compare its performance to the individual models. 
                4. Fine-tune the ensemble model for optimal performance, balancing accuracy, generalization, and robustness. 
                5. Deliver a well-documented Python implementation of the final ensemble model. 

                **Deliverable:** Python code for an ensemble stock prediction model.
                
                **Participants:** AI Model Developer, Model Ensemble Agent, Project Manager
            """),
            expected_output = "Python code for an ensemble stock prediction model",
            agent = self.Model_Ensemble_Agent,
            output_file = 'Ensemble_Stock_Prediction_Model.py',
            tools = [algorithms_show, algorithm_search,exa_search,exa_find_similar],
            async_execution=False,
        )
        self.Task_Risk_Management = Task(
            description = dedent(f"""
                ## Task: Risk Management
                **Objective:** Develop a comprehensive risk management strategy for the automated stock trading system to mitigate potential losses and ensure responsible trading.

                **Instructions:**
                1. Identify and analyze the key risks associated with automated stock trading, including market risk, model risk, operational risk, and systemic risk.
                2. Define the risk tolerance levels and investment constraints for the trading system, taking into account factors such as capital allocation, maximum drawdown limits, and regulatory requirements.
                3. Design and implement appropriate risk mitigation strategies, including:
                    * Stop-loss orders to automatically exit positions when losses reach a predefined threshold.
                    * Position sizing to determine the optimal trade size based on the perceived level of risk.
                    * Diversification across multiple assets to reduce exposure to any single stock or sector.
                4. Develop a robust backtesting framework to evaluate the performance of the risk management strategies under various market conditions, using historical data.
                5. Prepare a comprehensive risk management plan document that outlines the identified risks, mitigation strategies, risk tolerance levels, and backtesting results.

                **Deliverable:** A detailed risk management plan for the automated stock trading system.
                
                **Participants:** Risk Manager, Project Manager, AI Model Developer
            """),
            expected_output = "Risk management plan for the automated trading system",
            agent = self.Risk_Manager,
            output_file = 'Risk_Management_Plan.txt',
            tools = [algorithms_show, algorithm_search,exa_search, exa_find_similar],
            async_execution=False,
        )
            
        self.Task_Manage_Project = Task(
            description = dedent(f"""
                ## Task: Project Management
                **Objective:** Oversee the development, integration, and deployment of all system components into a functional automated stock trading system.

                **Instructions:**
                1. Define clear project goals, scope, and deliverables in collaboration with stakeholders.
                2. Develop a detailed project plan that outlines the tasks, timelines, dependencies, and resource allocation for each stage of the project.
                3. Coordinate and supervise the work of all agents involved, ensuring effective communication, collaboration, and timely completion of tasks.
                4. Establish a robust testing and quality assurance process to identify and address any bugs, errors, or inconsistencies in the system.
                5. Oversee the integration of the individual components (data ingestion, market analysis, sentiment analysis, AI models, ensemble methods, risk management) into a cohesive and functional system.
                6. Develop a comprehensive documentation set for the system, including user manuals, technical specifications, and operational guidelines.
                7. Monitor the performance of the system post-deployment and implement necessary updates, improvements, or bug fixes.

                
                **Deliverable:** A fully functional and documented automated stock trading system.
                
            """),
            expected_output = "Fully functional and documented automated stock trading system",
            agent = self.Project_Manager,
            output_file = 'Automated_Trading_System_Documentation.txt',
            async_execution=False,
        )
        self.Task_Data_Ingestion = Task(
            description = dedent(f"""
                ## Task: Data Ingestion
                **Objective:** Collect, clean, pre-process, and prepare financial data from various sources for use in stock prediction models.

                **Instructions:**
                1. Gather data from reliable financial APIs (e.g., Yahoo Finance, Alpha Vantage, Tiingo), covering historical stock prices, trading volume, and other relevant financial metrics.
                2. Collect news articles from reputable financial news sources and social media posts related to the target companies and the overall market sentiment.
                3. Implement data cleaning procedures to handle missing values, outliers, and inconsistencies in the data.
                4. Normalize and transform the data into a suitable format for input to machine learning models.
                5. Engineer relevant features from the raw data, such as technical indicators (e.g., moving averages, RSI, MACD) and sentiment scores from news and social media.
                6. Split the data into training, validation, and testing sets for model development and evaluation.
                7. Store the processed data in an efficient and accessible format (e.g., CSV, Parquet) for use by the AI model development team. 

                **Deliverable:** Cleaned, pre-processed, and structured financial data ready for model training. 
                
                **Participants:** Data Expert, AI Model Developer, Market Analyst, Sentiment Analyst
            """),
            expected_output = "Cleaned and processed financial data",
            agent = self.Data_Agent,
            output_file = 'Processed_Financial_Data.csv',
            tools = [exa_search, exa_find_similar,yf_stock_data],
            async_execution=False,
        )
        
    def get_Task_Market_Analysis(self):
            return self.Task_Market_Analysis

    def get_Task_Sentiment_Analysis(self):
            return self.Task_Sentiment_Analysis

    def get_Task_AI_Modeling(self):
        return self.Task_AI_Modeling
    def get_Task_Model_Ensemble(self):
        return self.Task_Model_Ensemble
    def get_Task_Risk_Management(self):
        return self.Task_Risk_Management
    def get_Task_Manage_Project(self):
        return self.Task_Manage_Project
    
    def get_Task_Data_Ingestion(self):
        return self.Task_Data_Ingestion
    
