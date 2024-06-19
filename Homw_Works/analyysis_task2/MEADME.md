Exercise 2
Create project which will calculate base statistics of (mean, median and std) of every column except variety from data/iris.csv file.

Project structure should be:

├── iris_analysis
│   ├── __init__.py
│   ├── io
│   │   ├── __init__.py
│   │   ├── load.py
│   │   └── save.py
│   └── calculate.py
└── run_analysis.py
File iris_analysis/io/load.py should contain functions needed to load and parse data/iris.csv. File iris_analysis/io/save.py should contain functions needed to save result to .csv file. File iris_analysis/calculate.py should contain functions needed for statistic calculation. File run_analysis.py should be script which import proper functions from iris_analysis package and call them to calculate statistics. Each task should be performed using code from module with proper semantic name. Script should have two arguments: path to ada file and path to result file.

Example run:

$ python run_analysis.py data/iris.csv result.csv