\# AI Business Analytics Assistant



A Streamlit-based business analytics application that allows users to upload CSV or Excel datasets, explore their data, generate automated business insights, visualize metrics, and ask natural-language analytical questions.



The project combines \*\*Python, Pandas, Streamlit, data visualization, and LLM-driven analytical planning\*\* to turn business questions into structured data-analysis operations.



\## Features



\* Upload CSV and Excel datasets

\* Dataset overview:



&#x20; \* Row count

&#x20; \* Column count

&#x20; \* Missing values

&#x20; \* Duplicate rows

&#x20; \* Memory usage

\* Interactive data preview

\* Automated business insights

\* Interactive bar, line, and pie charts

\* Natural-language analytics interface

\* Structured LLM analysis planning

\* Pandas-based execution of analytical plans

\* CSV and Excel export

\* PDF business report generation



\## LLM-Powered Analytics Architecture



The application is designed so that the LLM interprets the user's business question while Pandas performs the actual calculation.



```text

User Question

&#x20;     ↓

Dataset Schema / Context

&#x20;     ↓

LLM Analysis Planner

&#x20;     ↓

Structured Analysis Plan

&#x20;     ↓

Plan Validation

&#x20;     ↓

Pandas Execution

&#x20;     ↓

Verified Result

&#x20;     ↓

Text / Table / Visualization

```



This separation helps prevent the language model from inventing numerical results.



For example:



> "Which advisor has the most open job cards?"



The LLM can interpret the question as:



```text

Operation: group\_by

Group: Advisor

Filter: Status = Open

Aggregation: Count

```



The application then performs the calculation locally using Pandas.



\## Business Analytics Use Cases



The application is designed to support questions such as:



\* How many open job cards are there?

\* Which advisor has the most open jobs?

\* What is the average ageing of open jobs?

\* Which technician has the highest workload?

\* What are the highest-value transactions?

\* Show the top 10 records by a numeric metric.

\* How many records match a particular status?

\* Summarize the dataset statistically.



The same architecture can be adapted to datasets from areas such as:



\* Service operations

\* Sales

\* Finance

\* Inventory

\* Customer analytics

\* Operations management

\* Business reporting



\## Technology Stack



\*\*Language\*\*



\* Python



\*\*Data \& Analytics\*\*



\* Pandas

\* NumPy

\* Scikit-learn



\*\*Visualization\*\*



\* Plotly



\*\*Application\*\*



\* Streamlit



\*\*LLM Integration\*\*



\* OpenAI API

\* Structured analytical planning



\*\*Reporting\*\*



\* ReportLab

\* Excel export with OpenPyXL



\*\*Environment\*\*



\* Python virtual environment

\* Git / GitHub



\## Project Structure



```text

AI-Business-Analytics-Assistant/

│

├── app.py

├── requirements.txt

├── .gitignore

├── .gitattributes

│

└── utils/

&#x20;   ├── data\_loader.py

&#x20;   ├── analyser.py

&#x20;   ├── insights.py

&#x20;   ├── ai\_engine.py

&#x20;   ├── llm\_engine.py

&#x20;   ├── plan\_executor.py

&#x20;   ├── chart\_generator.py

&#x20;   ├── exporter.py

&#x20;   └── report\_generator.py

```



\## Running the Application



\### 1. Clone the repository



```bash

git clone https://github.com/sibisundarram-star/AI-Business-Analytics-Assistant.git

cd AI-Business-Analytics-Assistant

```



\### 2. Create a virtual environment



```bash

python -m venv venv

```



Activate it on Windows:



```powershell

venv\\Scripts\\activate

```



\### 3. Install dependencies



```bash

pip install -r requirements.txt

```



\### 4. Configure the LLM API



Create a `.env` file in the project root:



```text

OPENAI\_API\_KEY=your\_api\_key\_here

OPENAI\_MODEL=your\_model\_name

```



Never commit the `.env` file or API credentials to GitHub.



\### 5. Start the application



```bash

streamlit run app.py

```



The application will open in the browser.



\## Data Privacy



Uploaded datasets are processed locally by the application's Pandas analytics layer.



The LLM planning component is designed to work from dataset schema and contextual information rather than blindly sending the entire dataset for every question.



Users should still review the data-handling requirements of their chosen LLM provider before using confidential or sensitive business data.



\## Current Development Status



The core application is functional, including:



\* Dataset ingestion

\* Data profiling

\* Automated insights

\* Interactive visualization

\* Export functionality

\* Structured LLM planning architecture

\* Local analytical plan execution



Live LLM inference requires a valid API account with available usage/credits.



\## Future Improvements



Planned improvements include:



\* Conversational memory across analytical questions

\* More advanced analytical operations

\* Automatic chart selection

\* Date and time-series intelligence

\* KPI detection

\* Anomaly detection

\* Forecasting

\* Role-specific business dashboards

\* Support for larger datasets

\* Additional LLM providers

\* Deployment as a hosted analytics application



\## Author



\*\*B. Sibi Sundar Ram\*\*



M.Sc. Business Statistics

Data Analytics | Business Analytics | Operations Analytics | AI/ML



GitHub:

https://github.com/sibisundarram-star



