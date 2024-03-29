# Twitter-ETL-Pipeline (Please read the Twitter-ETL.pdf from this repo for full documentation)

## Overview

This project provides a basic implementation of an ETL (Extract, Transform, Load) pipeline for extracting data from the Twitter API, transforming it, and loading it into an Amazon S3 bucket. The pipeline utilizes Python, Pandas, AWS services (S3 and EC2), Apache Airflow, Twitter API, and Linux Terminal commands.

## Steps Involved

1. **Extracting Data from Twitter API:** Data is extracted from the Twitter API, converted into a Pandas DataFrame, and stored as a '.csv' file in an Amazon S3 bucket.

2. **Writing DAGs (Directed Acyclic Graphs):** DAGs are written for the ETL process using Apache Airflow, defining the workflow and dependencies between tasks.

3. **Setting up an AWS EC2 Instance:** An AWS EC2 instance (t3.medium) is set up to run the ETL pipeline, providing the necessary computing resources for Apache Airflow.

4. **Setting up an S3 Bucket:** An S3 bucket is configured to collect the data generated by the ETL pipeline.

5. **Setting up Apache Airflow:** After the EC2 instance is set up, Apache Airflow is run in standalone mode. The Python script and DAG are imported into Airflow and executed, managing the ETL workflow.

## Limitations and Future Improvements

- **High Computing Costs:** The document acknowledges the limitation of high computing costs and recommends turning off the EC2 instance to prevent unaffordable expenses.

- **Possible Improvements:**
  - Regularly updating the pipeline.
  - Adding or dropping columns based on evolving data requirements.
  - Allowing inputs from analysts for custom data transformations and analyses.

## Technical Resources

For detailed technical instructions and code examples, please refer to the following external resources:

- [Twitter API Documentation](https://developer.twitter.com/en/docs)
- [Apache Airflow Documentation](https://airflow.apache.org/docs/)
- [AWS Documentation](https://docs.aws.amazon.com/)

For further details and specific technical instructions, it is recommended to consult the mentioned external resources.
