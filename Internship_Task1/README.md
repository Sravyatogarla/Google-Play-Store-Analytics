# 📊 Google Play Store Data Analytics – Internship Task 1

This repository contains the implementation of **Task 1** for the internship project titled **"Real-Time Google Play Store Data Analytics"** using Python. This task focuses on analyzing the relationship between the **number of installs** and **revenue** for **paid apps**, visualized through a scatter plot.

---

## 🧾 Task 1 Objective

Create a **scatter plot** to visualize the relationship between revenue and the number of installs for **paid apps only**. The plot includes:

- A **trendline** to display the correlation
- **Color-coded points** based on app categories
- Calculated revenue using the formula:  
  `Revenue = Installs × Price`

---

## 🗃️ Repository Structure

Google-Play-Store-Analytics/
│
├── Internship_Task1/
│ ├── Task1_Revenue_vs_Installs.ipynb # Jupyter notebook with step-by-step code and insights
│ ├── revenue_vs_installs.html # Saved interactive plot as HTML file
│ ├── googleplaystore.csv # Dataset used (filtered as per task)
│ └── README.md # Task-specific documentation
│
└── main_project_files/ # (Optional) Main project directory from training

---

## 📈 Output – Scatter Plot

- The plot displays revenue on the Y-axis and installs on the X-axis.
- Each point is colored based on the app's category.
- A trendline is included to visualize correlation.

🔗 **Preview HTML file**: `revenue_vs_installs.html` (Open in browser for interaction)

---

## 📦 Dataset Information

- **Source:** Dataset provided during NullClass training
- **Relevant Columns Used:**
  - `Category`
  - `Installs`
  - `Type`
  - `Price`
- **Preprocessing:**
  - Converted string values (`Installs`, `Price`) to float
  - Filtered only `Paid` apps
  - Calculated `Revenue`

---

## 🔍 Key Insights & Conclusions

- Apps in specific categories like **Productivity** and **Education** show higher revenues despite lower installs.
- There is a **positive correlation** between installs and revenue among paid apps.
- Some **outliers** suggest high pricing with low installs leading to comparable revenue.

---

## 🧑‍💻 Tools & Libraries Used

- Python
- Pandas
- Plotly
- NumPy
- Jupyter Notebook

---

## 📥 How to View the Plot

To view the interactive plot:

1. Clone or download this repository.
2. Open `revenue_vs_installs.html` in any browser.

---

## 🧾 Submission Note

This task is part of the internship assignment under **Real-Time Google Play Store Analytics (Python)**. The code and files are submitted as per the internship instructions under Task 1.

---


