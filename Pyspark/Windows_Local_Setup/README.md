# Requirements for Spark Setup in Windows

## Introduction
This document provides detailed instructions for setting up Apache Spark on a Windows machine. Apache Spark is an open-source, distributed computing system that offers a robust framework for data processing and analytics.

## Prerequisites
Before proceeding with the Spark installation, ensure your Windows machine meets the following prerequisites:

1. **Operating System**: Windows 8 or later.
2. **Java Development Kit (JDK)**: Spark requires JDK to be installed. JDK version 8 or 11 is recommended.
    * Download JDK from [Oracle's website](https://jdk.java.net/java-se-ri/11-MR2) or adopt an open-source JDK distribution.
    * Set the JAVA_HOME environment variable to your JDK installation path *Using cmd*.
        a. To set the JAVA_HOME variable, use the following command in the cmd:
           ```cmd
           setx JAVA_HOME "C:\Program Files\Java\jdk-11.0.0.1"
           ```
        b. Verify by using the command:
           ```cmd
           echo %JAVA_HOME%
           ```

3. **Python** (optional): For PySpark, Python 3.6 or later is required.
    * Download Python from the official Python website.
    * Add Python to the system PATH.