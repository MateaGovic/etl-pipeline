# ETL Pipeline Project

## Project Description
The goal of the project is to build an ETL pipeline. ETL (Extract, Transform, Load) is a data pipeline used to collect data from various sources, transforms the data according to business requirements, and loads the data into a destination data storage.

This project contains the following files:
- ``src/extract.py`` - a python script that contains instructions to connect to Amazon Redshift data warehouse and to extract online transactions data with transformation tasks using SQL<br>
- ``src/transform.py`` - a python script that contains instructions to identify and remove duplicated records<br>
- ``src/load_data_to_s3.py`` - a python script that contains instructions to connect to Amazon S3 cloud object storage and to write the cleaned data as a CSV file into an S3 bucket<br>
- ``main.py`` - a python script that contains all instructions to execute all the steps to extract, transform, and load the transformed data using the functions from extract.py, transform.py, and load_data_to_s3.py<br>
- ``.env`` - a text document that contains the list of environment variables used in .env file<br>
- ``requirements.txt`` - a text document that contains all the libraries required to execute the code<br>
- ``.gitignore``a text document that specifies intentionally untracked files that Git should ignore

## Requirements
- Docker:
    - Docker for Mac: [Install Docker Desktop on Mac](https://docs.docker.com/desktop/install/mac-install/)
    - Docker for Windows: [Install Docker Desktop on Windows][https://docs.docker.com/desktop/install/windows-install/]

- Python 3+

## How to Run the Project

- To run the python script that runs the ETL pipeline on CLI:
    - Windows: 
    ```
        python main.py
    ```
    - Mac: 
    ```
        python3 main.py
    ```

- To run ETL pipeline using Docker on CLI
    - Important:
      - Comment out the codes ``from dotenv import load_dotenv`` and ``load_dotenv()`` in the main.py script before executing the following codes
      - Fill out the environment variables ``.env`` file g
  

    - Build an image
    ```
      docker image build -t etl-pipeline .
    ```
    - Run the etl job
    ```
      docker run --env-file .env etl-pipeline
    ```