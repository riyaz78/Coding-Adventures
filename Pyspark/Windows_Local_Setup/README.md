# Requirements for Spark Setup in Windows

### Introduction
This document provides detailed instructions for setting up Apache Spark on a Windows machine. Apache Spark is an open-source, distributed computing system that offers a robust framework for data processing and analytics.

### Prerequisites
Before proceeding with the Spark installation, ensure your Windows machine meets the following prerequisites:

1. **Operating System**: Windows 8 or later.
2. **Java Development Kit (JDK)**: Spark requires JDK to be installed. JDK version 8 or 11 is recommended.
    * Download JDK from [Oracle's website](https://jdk.java.net/java-se-ri/11-MR2) or adopt an open-source JDK distribution.
    * Set the JAVA_HOME environment variable to your JDK installation path *Using cmd*.
        * To set the JAVA_HOME variable, use the following command in the cmd:
           ```
           setx JAVA_HOME "C:\Program Files\Java\jdk-11.0.0.1"
           ```
        * Verify by using the command:
           ```
           echo %JAVA_HOME%
           ```
        * Add bin folder to path environment variable
            ```
            setx PATH "%PATH%;%JAVA_HOME%\bin"
            ```
        * Make sure java -version is showing JAVA 8 or JAVA 11

3. **Python** (optional): For PySpark, Python 3.6 or later is required.
    * Download Python from the official [Python website](https://www.python.org/).
    * Add Python to the system PATH.
        * Verify in cmd by using command python --version




## Installation Guide

1. **Install Winutils**
    * Spark on Windows requires Hadoop's winutils.exe.
    * Download the [winutils repository](https://github.com/cdarlint/winutils)
    * Extract the zip file and copy the latest version (Currently it's 3.3.5)
    * Set the HADOOP_HOME variable, using the following command
        ```
        setx HADOOP_HOME "C:\hadoop\hadoop-3.3.5"
        ```
    * Add the bin folder into path variable
        ```
        setx PATH "%PATH%;%HADOOP_HOME%\bin"
        ```
2. **Download Apache Spark**
    * Download the latest version of Apache Spark from the [official website](https://spark.apache.org/downloads.html)
    * Since it's .tgz you can either use 7 zip file to extract or using below bash command
        ```
        tar -xzvf "spark-3.5.0-bin-hadoop3.tgz"
        ```
    * Add the SPARK_HOME variable, using the following command
        ```
        setx SPARK_HOME "C:\spark\spark-3.5.0"
        ```
    * Add bin folder to the path variable
        ```
        setx PATH "%PATH%;%SPARK_HOME%\bin"
        ```
    * Add PYTHONPATH variable
        ```
        setx PYTHONPATH "C:\spark\spark-3.5.0\python;C:\spark\spark-3.5.0\python\lib\pyspark.zip"
        ```
    * Add PYSPARK_PYTHON variable
        ```
        setx PYSPARK_PYTHON "C:\Users\testversion\AppData\Local\Programs\Python\Python312\python.exe"
        ```