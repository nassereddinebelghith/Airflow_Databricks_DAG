<!-- PROJECT SHIELDS -->
[![GPL License][license-shield]][license-url]
[![Forks][forks-shield]][forks-url]
[![Issues][issues-shield]][issues-url]
[![Code Size][cSize-shield]][cSize-url]


<!-- PROJECT LOGO -->
<br />
  <h3 align="center">Apache Airflow <> Databricks Example Pipeline</h3>

  <p align="center">
    A simple, scalable use case utilizing Apache Airflow, Databricks, Delta Tables, & PySpark!
    <br />
    <a href="https://github.com/AmirZahre/Data_Analyst_DAG/"><strong>Checkout the code »</strong></a>
    <br />
    <br />
    <a href="https://github.com/AmirZahre/Data_Analyst_DAG/releases/tag/Astronomer">Download</a>
    ·
    <a href="https://github.com/AmirZahre/Data_Analyst_DAG/issues">Report Bug</a>
    ·
    <a href="https://github.com/AmirZahre/Data_Analyst_DAG/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)


<!-- ABOUT THE PROJECT -->
## About The Project
  
[![diagram]](#)  

Databricks is powerful, as is Apache Airflow. Together, they make a compelling use case for a well-rounded, all-you-need stack for many of your data pipeline needs. This project showcases the utilization of Databricks to extract, manipulate, and upsert data into its Delta Table infrastructure, all nicely wrapped (and automated!) with Apache Airflow.
  
### Built With
* [Python](https://www.python.org/)
* [Apache Airflow](https://airflow.apache.org/)
* [Databricks](https://databricks.com/)

### Built For
* [Astronomer](https://www.astronomer.io/) as one of my many projects during my 2022 Spring internship.

<!-- PROCESS -->
## Use Case
  
> Imagine a Data Analyst who works for an investment management firm, helping clients make good decisions about their investment portfolios. To do so, the Data Analyst retrieves market data regularly, and for each client provides an analysis of how the industries they are invested in perform.
>
> The Data Analyst persists the transformed data from analyses, sends automated notifications to clients to take action when relevant, and keeps a dashboard up to date for them to check their investment health at a glance.
>
> Let’s look into this Data Analysts workflow.
  
  
  
 
  
  
## Process
### Part 1: Airflow triggers Databricks notebook with parameters
  Step 1: Passing Parameters from Airflow using <b>notebook_params = portfolio</b>
  
```
  portfolio = {
               "stocks": "MSFT AAPL IBM WMT SHOP GOOGL TSLA GME AMZN COST COKE CBRE NVDA AMD PG"
               }

   # Run the Databricks job and retrieve the job Run ID
   run_databricks_job = DatabricksRunNowOperator(
       task_id="Run_Databricks_Job",
       databricks_conn_id=DATABRICKS_CONNECTION_ID,
       job_id=137122987688189,
       do_xcom_push=True,
       notebook_params = portfolio
   )
```
  Step 2: Retrieving Parameters in Databricks
  Use dbutils.widgets.text(param, default_value) to load params pushed by Airflow into the Databricks notebook.
  [![param_get]](#)  

  
<!-- LICENSE -->
## License

Distributed under Apache License 2.0. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Amir Zahreddine - zahreddi@ualberta.ca

Project Link: [https://github.com/AmirZahre/Data_Analyst_DAG](https://github.com/AmirZahre/Data_Analyst_DAG)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [Santona Tuli](https://www.linkedin.com/in/santona-tuli/) for being an awesome mentor towards my introduction to DevOps!
* [The team @ Astronomer](https://www.astronomer.io/) for help with any questions that arose while learning Airflow.
* [Ran Aroussi](https://pypi.org/user/ranaroussi/) for creating a fabulous Yahoo Finance API library for Python.

  
<!-- MARKDOWN LINKS & IMAGES -->
[license-shield]: https://img.shields.io/github/license/AmirZahre/Data_Analyst_DAG
[license-url]: https://github.com/AmirZahre/Data_Analyst_DAG/blob/main/LICENSE.md
[issues-shield]: https://img.shields.io/github/issues/AmirZahre/Data_Analyst_DAG
[issues-url]: https://github.com/AmirZahre/Data_Analyst_DAG/issues
[forks-shield]: https://img.shields.io/github/forks/AmirZahre/Data_Analyst_DAG
[forks-url]: https://github.com/AmirZahre/Data_Analyst_Dag/network/members
[cSize-shield]: https://img.shields.io/github/languages/code-size/AmirZahre/Data_Analyst_Dag
[cSize-url]: https://github.com/AmirZahre/Data_Analyst_DAG
[diagram]: images/workflow.png
[tasks]: images/task_dependencies.png
[param_get]: images/param_get.png
