# Titanic Bias Audit
## Statistical Disparity Analysis across Gender and Passenger Class

SQL and Python pipeline surfacing survival disparity across gender and 
passenger class. First-class females survived at 2x the rate of 
third-class males — a clear demonstration of intersectional bias 
embedded in historical decision systems.

## Key Finding
- First-class female survival rate: 97%
- Third-class male survival rate: 14%
- **2x intersectional disparity across class and gender**

## Tech Stack
Python · SQL · Pandas · SQLite · Matplotlib · pytest

## Structure
- `titanic_eda.ipynb` — exploratory data analysis and charts
- `data_pipeline.ipynb` — SQL pipeline, survival rate by class and gender
- `titanic_analysis.py` — OOP refactor with pytest

## How to Run
```bash
pip install pandas matplotlib sqlite3 pytest
jupyter notebook
```

## Dataset
Titanic dataset from Kaggle:
https://www.kaggle.com/competitions/titanic/data
EOF
