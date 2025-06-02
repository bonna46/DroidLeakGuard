# DroidLeakGuard
### method signature combination is done on method signature :  # Method + Class + Parameter + Return type+ Method Description
### method signature combination_2 is done on method signature :  # Method + Class + Parameter + Return type

### package installed: sentence-transformer
### run on pycharm

# DroidLeakGuard
DroidLeakGuard is a Python-based tool designed to assist Android developers and researchers in detecting and analyzing potential resource leaks in Android applications. By leveraging method signature analysis and natural language processing (NLP) techniques, it aims to identify patterns that suggest improper resource handling, such as unreleased SQLite cursors, unclosed InputStream objects, or forgotten WakeLock.release() calls.

## :mag_right: Key Features
1) Method Signature Analysis: Combines method names, classes, parameters, return types, and descriptions to form comprehensive method signatures for analysis.

2) NLP Integration: Utilizes the sentence-transformers library to semantically compare method descriptions, aiding in the detection of similar patterns that could lead to resource leaks.

3) Data-Driven Approach: Employs CSV datasets (method signature combinations.csv and method signature combinations_2.csv) to store and compare method signatures systematically.

#### Ease of Use: Designed to run seamlessly in Python environments, with compatibility for IDEs like PyCharm.


## 🧪 Use Cases
Static Code Analysis: Identify potential resource leaks during the development phase by analyzing method signatures and their usage patterns.

Educational Tool: Serve as a learning resource for understanding common resource management pitfalls in Android development.

Research: Facilitate studies in software engineering by providing a framework to analyze and compare method behaviors related to resource handling.


## 🚀 Getting Started
### Clone the Repository:
```
git clone https://github.com/bonna46/DroidLeakGuard.git
```
### Install Dependencies:
```
pip install sentence-transformers
```
### Run the Tool:
Open main.py in your preferred Python environment (e.g., PyCharm) and execute the script to begin analysis.


## 📂 Repository Contents
main.py: The main script orchestrating the analysis process.

method signature combinations.csv: Dataset containing detailed method signatures with descriptions.

method signature combinations_2.csv: Dataset focusing on method signatures without descriptions.

android.zip: Compressed archive containing additional resources or datasets (contents should be reviewed for relevance).
