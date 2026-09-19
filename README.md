## Installation Instructions

1. Open a terminal and move into the project folder:

  ```bash
  cd smu-cce-starter_mina
  ```

2. Create and activate a virtual environment:

  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  ```

3. Install the required packages:

  ```bash
  pip install -r requirements.txt
  ```

4. Start Jupyter Notebook:

  ```bash
  jupyter notebook
  ```

5. Open a notebook from `notebooks/` in your browser and run its cells from top to bottom.

## Code Walkthrough

- `requirements.txt` lists the Python packages used by the project, including pandas, yfinance, and Streamlit.
- `lessons/` contains the course instructions and concepts.
- `notebooks/` contains the main analysis work:
  - `filings.ipynb` explores company filings and financial data.
  - `news.ipynb` explores financial news data.
  - `stock_price_ratings.ipynb` analyzes stock prices and ratings.
- `README.md` explains the project and how to get started.

The workflow is: read a lesson, open the related notebook, load data, clean and analyze it with Python, and view the resulting tables or charts. The notebook analyses are the starting point for building the financial-data application described in the course.

## Installation Instructions

If you are new to Python projects, follow these steps in your terminal:

1. Open a terminal in the project folder.
2. Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. Start Jupyter Notebook:

```bash
jupyter notebook
```

5. In the browser, open one of the notebooks in the `notebooks/` folder and run the cells.

That is the basic setup for this project. If you are using GitHub Codespaces, the environment is usually already prepared for you.

## Code Walkthrough

This repository is a starter project for learning how to work with financial data and build a simple cloud-based analytics app.

### Main folders and files

- `lessons/`: course notes and step-by-step instructions for the project.
- `notebooks/`: the main working files for exploring and analyzing data.
  - `filings.ipynb`: looks at company filings and financial information.
  - `news.ipynb`: explores news-related data and text-based insights.
  - `stock_price_ratings.ipynb`: analyzes stock prices and ratings.
- `requirements.txt`: lists the Python packages needed to run the notebooks.
- `README.md`: project overview and course context.

### How it works

The project usually starts with the lessons, which explain the tasks and concepts. After that, you open a notebook in `notebooks/` and run the code cells. The notebook loads data, cleans it, transforms it into useful tables or charts, and then helps you understand patterns in the data.

In simple terms:

1. Read the lesson instructions.
2. Open a relevant notebook.
3. Load the dataset.
4. Clean and organize the data.
5. Run analysis and create visual outputs.
6. Use what you learned as building blocks for the final app or cloud deployment.

This is the beginning of a bigger workflow: data analysis in notebooks, then turning those ideas into a usable app that can be shared online.

 # Cloud Computing for Economics: Starter Repo 

  This repository contains the starter code and lesson materials for building a Python financial-data application and deploying it to AWS.

  Students will use GitHub Codespaces, Python, Jupyter notebooks, Streamlit, Git, and AWS CloudFormation.

  ## Learning outcomes

  By the end of the course, you will be able to:

   1.  Build and deploy an analytics application with a simple Front End / back-end (using AI)
   2.  Host and share the application on a cloud platform (e.g., AWS EC2 or similar) so that others can access it securely over the web
   3.  Integrate data sources and APIs into the app to enable interactive, real-time analytics
   4.  Apply cloud architecture best practices, ensuring the app demonstrates scalability, performance efficiency, and basic security
   5.  Showcase your work on GitHub as part of a personal portfolio, demonstrating practical cloud and analytics skills through a shareable, explorable repository

  
  ## Repository structure

  ```text
  .
  ├── lessons/          # Step-by-step course instructions
  ├── notebooks/        # Starter financial-data notebooks
  ├── requirements.txt  # Python dependencies
  └── README.md         # Course overview