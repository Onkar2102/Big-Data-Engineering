
**📌 README.md: Credit Card Data Processing Pipeline**
------------------------------------------------------

**🚀 End-to-End Credit Card Data Processing Pipeline using Apache Spark on Google Cloud Dataproc**
==================================================================================================

**📌 Project Overview**
-----------------------

This project demonstrates an **end-to-end data processing pipeline** for **credit card approval prediction** using **Apache Spark**.

The primary goal is to showcase **real-world data engineering practices**, covering:\
✅ **Data Ingestion** → Extracting data from multiple sources (CSV, SQL, GCS).\
✅ **Data Cleaning & Transformation** → Handling missing values, feature engineering.\
✅ **Data Integration** → Joining multiple datasets efficiently.\
✅ **Optimization & Data Serving** → Performance tuning & saving results for analysis.\
✅ **Deployment on Dataproc** → Running the pipeline using **`spark-submit`**.

**Technologies Used:**\
🛠 **Apache Spark** (PySpark)\
☁️ **Google Cloud Dataproc**\
📦 **Google Cloud Storage (GCS)**\
🐍 **Python (pyspark, pyyaml, mysql-connector-python, pytest)**\
🔄 **Modular Coding & Logging**

* * * * *

**📌 1️⃣ Initial Exploration on Dataproc Jupyter Notebook**
-----------------------------------------------------------

Before moving to a structured **modular codebase**, we first **explored the dataset interactively** in a **Jupyter Notebook** running on **Google Cloud Dataproc**.

### **🔹 Steps Followed:**

✅ **Downloaded and loaded the dataset** using PySpark.\
✅ **Performed exploratory data analysis (EDA)** to understand data distribution.\
✅ **Identified data inconsistencies** (e.g., missing values, incorrect data formats).\
✅ **Executed basic Spark transformations** (filtering, selecting, aggregating).

Once we had a **clear understanding** of the dataset, we **migrated** from Jupyter to **a production-ready modular Spark pipeline**.

* * * * *

**📌 2️⃣ Transition to a Structured Project for Production**
------------------------------------------------------------

To ensure **scalability & reusability**, we structured the project as follows:

### **📂 Project Directory Structure**

```
credit_card_approval_project/
│── configs/                  # YAML configuration files
│   ├── config_local.yaml      # Local execution config
│   ├── config_dataproc.yaml   # Dataproc execution config
│── logs/                      # Log files
│   ├── spark_app.log
│── src/                       # Source code
│   ├── main.py                # Pipeline entry point
│   ├── data_ingestion.py       # Reads data from CSV/GCS/SQL
│   ├── data_cleaning.py        # Handles missing values & transformations
│   ├── data_integration.py     # Merges datasets & prepares ML features
│   ├── optimization_serving.py # Optimizes & stores final data
│   ├── logger.py               # Centralized logging
│── tests/                      # Unit tests for each module
│── requirements.txt            # Dependencies
│── setup.py                    # Project setup file
│── run_spark_local.sh          # Shell script to run locally
│── run_spark_dataproc.sh       # Shell script to run on Dataproc
│── README.md                   # Project documentation

```

* * * * *

**📌 3️⃣ Modular Code Development**
-----------------------------------

Each **step of the pipeline** was converted into a **separate Python module**, following **best practices**.

### **🔹 Data Ingestion (`src/data_ingestion.py`)**

-   Reads data from **CSV (Local)** or **Parquet (GCS)** based on `config.yaml`.
-   Uses **Spark DataFrame API** for efficient I/O.

✅ **How to run data ingestion?**

```
python src/data_ingestion.py --config configs/config_local.yaml

```

* * * * *

### **🔹 Data Cleaning (`src/data_cleaning.py`)**

-   Handles **missing values**, incorrect **data formats**, and **feature extraction**.
-   Standardizes categorical values and prepares the data for integration.

✅ **How to run data cleaning?**

```
python src/data_cleaning.py --config configs/config_local.yaml

```

* * * * *

### **🔹 Data Integration (`src/data_integration.py`)**

-   Joins `application_record` with `credit_record`.
-   Resolves **inconsistent data** and **ensures referential integrity**.
-   Implements **partitioning & caching** to optimize performance.

✅ **How to run data integration?**

```
python src/data_integration.py --config configs/config_local.yaml

```

* * * * *

### **🔹 Optimization & Data Serving (`src/optimization_serving.py`)**

-   **Optimizes Spark execution** via caching, repartitioning, and predicate pushdown.
-   Saves the final dataset **back to GCS** for further analysis.

✅ **How to run optimization & serving?**

```
python src/optimization_serving.py --config configs/config_local.yaml

```

* * * * *

**📌 4️⃣ Logging & Error Handling**
-----------------------------------

To track execution progress, a **centralized logger** was implemented (`src/logger.py`), storing logs in **`logs/spark_app.log`**.

✅ **Example log entry:**

```
2025-03-22 00:30:52 - INFO - ✅ Data Integration Completed.
2025-03-22 00:32:04 - INFO - 🚀 Step 4: Optimization & Data Serving

```

* * * * *

**📌 5️⃣ Testing the Pipeline (`tests/`)**
------------------------------------------

To validate correctness, **unit tests** were implemented for each module using **`pytest`**.

### **✅ Running all tests:**

```
pytest tests/

```

### **✅ Running a specific test:**

```
pytest tests/test_data_ingestion.py

```

* * * * *

**📌 6️⃣ Deployment to Google Cloud Dataproc**
----------------------------------------------

### **🔹 Running the Pipeline on Dataproc**

Instead of running Spark jobs **locally**, we deployed the pipeline on **Google Cloud Dataproc** using `spark-submit`.

### **📝 `run_spark_dataproc.sh` (Final Execution Script)**

```
#!/bin/bash

MASTER_NODE="your-dataproc-master-ip"
ZONE="us-central1-a"
PROJECT_DIR="credit_card_pipeline"
VENV_NAME="credit_card_env"

echo "📤 Uploading project to Dataproc master node..."
scp -r src/ configs/ requirements.txt run_spark_local.sh run_spark_dataproc.sh $MASTER_NODE:~/$PROJECT_DIR/

echo "🚀 Connecting to Dataproc Master Node and Running the Pipeline..."

gcloud compute ssh $MASTER_NODE --zone=$ZONE --command "
    cd ~/$PROJECT_DIR
    python3 -m venv $VENV_NAME
    source $VENV_NAME/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    spark-submit src/main.py --config configs/config_dataproc.yaml
    echo '🎉 Pipeline Execution Completed!'
"

```

### **✅ Running the Script:**

```
chmod +x run_spark_dataproc.sh
./run_spark_dataproc.sh

```

* * * * *

**📌 Conclusion**
-----------------

This project follows **real-world best practices** in **data engineering**, demonstrating:\
✅ **Scalable Spark Pipelines** (Structured & modular)\
✅ **Seamless Local & Cloud Execution** (CSV, SQL, GCS)\
✅ **Efficient Data Processing** (Joins, caching, optimization)\
✅ **Automated Deployment on Dataproc**

🔥 **This guide can be used to reference key concepts for real-world Spark projects.**

