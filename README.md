# 🧬 Genetic Algorithm Optimization

An interactive **Genetic Algorithm Optimization** project built with Python, NumPy, Matplotlib, and Streamlit.

The application demonstrates how evolutionary algorithms can be used to find optimal solutions for different mathematical objective functions.

## 🚀 Features

* 🧬 Genetic Algorithm optimization
* 🎯 Multiple objective functions
* 🔼 Maximization and minimization
* 👥 Adjustable population size
* 🔁 Adjustable number of generations
* 🧬 Adjustable mutation rate
* 🔀 Adjustable crossover rate
* 📊 Best solution and fitness metrics
* 📈 Fitness convergence visualization
* 🧬 Population evolution visualization
* 📉 Objective function visualization
* ⚙️ Optimization parameter summary
* 🖥️ Interactive Streamlit interface

## 📌 Objective Functions

The application currently supports:

### 1. Non-linear Function

```text
f(x) = x sin(10πx) + 1
```

Search range:

```text
[-1, 2]
```

### 2. Sphere Function

```text
f(x) = x²
```

Search range:

```text
[-10, 10]
```

### 3. Rastrigin Function

```text
f(x) = 10 + x² - 10 cos(2πx)
```

Search range:

```text
[-5.12, 5.12]
```

### 4. Ackley Function

A standard benchmark function used for testing optimization algorithms.

Search range:

```text
[-5, 5]
```

## 🧠 How the Genetic Algorithm Works

The optimization process follows these steps:

```text
Initialize Population
        ↓
Evaluate Fitness
        ↓
Select Parents
        ↓
Crossover
        ↓
Mutation
        ↓
Create New Population
        ↓
Evaluate New Population
        ↓
Repeat for Generations
        ↓
Best Solution
```

## 🛠️ Technologies Used

* **Python**
* **NumPy**
* **Matplotlib**
* **Streamlit**

## 📂 Project Structure

```text
Genetic-Algorithm-Optimization/
│
├── app.py
├── genetic_algorithm.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/prabhuti256-collab/Genetic-Algorithm-Optimization.git
```

Move into the project directory:

```bash
cd Genetic-Algorithm-Optimization
```

Create a virtual environment:

```bash
py -3.12 -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

Or:

```bash
py -3.12 -m streamlit run app.py
```

The application will open in your browser.

## 📊 Results

The application provides:

* Best solution
* Best fitness
* Number of generations
* Fitness improvement
* Fitness convergence graph
* Population distribution
* Objective function graph

## 🎓 Learning Outcomes

This project demonstrates practical understanding of:

* Evolutionary computation
* Genetic algorithms
* Optimization techniques
* Fitness evaluation
* Selection
* Crossover
* Mutation
* Population evolution
* Data visualization
* Python programming
* Streamlit application development

## 🔮 Future Improvements

Possible future enhancements include:

* Multi-variable optimization
* Additional benchmark functions
* Genetic algorithm parameter comparison
* Elitism strategies
* Tournament and roulette-wheel selection comparison
* Real-world optimization problems
* Downloadable optimization results
* Deployment using Streamlit Cloud

## 👩‍💻 Author

**Prabhuti**

B.Tech – Artificial Intelligence & Machine Learning

## ⭐ Project Purpose

This project was developed as an AI/ML portfolio project to demonstrate practical implementation of evolutionary optimization techniques using Python.

Intern ID- CITS9069

