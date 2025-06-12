
# Google Play Store Analytics

This repository contains a comprehensive analysis of apps on the Google Play Store using Python and interactive visualizations.This project is a deep-dive analysis of Google Play Store apps. Using data wrangling, cleaning, and visualization, we explore app popularity, category distribution, ratings, installs, update patterns, sentiment trends, and revenue opportunities.  
This project was developed as part of the *NullClass* Data Science training program.

- This project also includes an **Internship Task Module** with individual assignments broken down into dedicated folders for structured execution and submission.


---

## Project Objectives:

- Analyze the relationship between app installs, ratings, and reviews.
- Understand the most popular categories and genres.
- Compare free vs paid apps revenue generation.
- Track app update frequency and its impact.
- Study the overall sentiment from user reviews.
- Derive insights into app size, pricing, and content rating trends.

---
## Internshio Task Objectives:


1. Create a scatter plot to visualize the relationship between revenue and the number of installs for paid apps only. Add a trendline to show the correlation and color-code the points based on app categories.

2. Use a grouped bar chart to compare the average rating and total review count for the top 10 app categories by number of installs. Filter out any categories where the average rating is below 4.0 and size below 10 M and last update should be Jan month . this graph should work only between 3PM IST to 5 PM IST apart from that time we should not show this graph in dashboard itself.

3. Plot a bubble chart to analyze the relationship between app size (in MB) and average rating, with the bubble size representing the number of installs. Include a filter to show only apps with a rating higher than 3.5 and that belong to the Game, Beauty ,business , commics , commication , Dating , Entertainment , social and event categories. Reviews should be greater than 500 and the app name should not contain letter "S" and sentiment subjectivity should be more than 0.5 and highlight the Game Category chart in Pink color. We have to translate the Beauty category in Hindi and Business category in Tamil and Dating category in German while showing it on Graphs. Installs should be more than 50k as well as this graph should work only between 5 PM IST to 7 PM IST apart from that time we should not show this graph in dashboard itself



---
## Dataset:

- *Play Store Data.csv*:  
  Contains app details like name, category, rating, size, installs, type (Free/Paid), price, content rating, genres, last updated date, and Android version requirements.
- *User Reviews.csv*
---

## Files:

📁 Project Structure

The repository is organized as follows:

- **Dataset/**

Play Store Data.csv

Reviews.csv

-**html/**

Contains all 10 interactive HTML visualizations

Examples: revenue_vs_installs.html, grouped_bar_chart.html, bubble_chart.html, etc.

-**Internship/**

Sub-directory containing all internship-related tasks

**Dataset/**

A copy of Play Store Data.csv used for task execution

**Task 1**

Task1_Revenue_vs_Installs.ipynb

Task1_Revenue_vs_Installs_ScatterPlot.html

images/ — related visual images

README.md — description and analysis for Task 1

**Task 2**

task2_grouped_bar_chart.ipynb

Task2_Grouped_Bar_chart.html

images/

README.md — description and analysis for Task 2

**Task 3**

Bubblechart.ipynb

Bubble_chart.html

images/

README.md — description and analysis for Task 3


**Final.ipynb**

**Task1_ScatterPlot.html**

**Task1_ScatterPlot.png**

**Task2_Grouped_Bar_chart.html**

**Task2_Grouped Bar chart.png**

**Task3_Bubble_Chart.html**

**Task3_Bubble Chart.png**

**dashboard.html**

**dashboard.png**


README.md — overview of all internship tasks

Play Store Data Analysis.ipynb — Main analysis notebook

README.md — Main project overview (this file)

---

## Technologies Used:

- Python 🐍

Pandas – Data manipulation

NumPy – Numerical operations

Matplotlib – Static visualizations

Seaborn – Statistical visualizations

Plotly – Interactive HTML visualizations

Jupyter Notebook – IDE for code and analysis
---

Internship Task Summaries

| Task       | Visualization        | Description                                                     |
| ---------- | -------------------- | --------------------------------------------------------------- |
| **Task 1** | 📉 Scatter Plot      | Relationship between **revenue** and **installs** for paid apps |
| **Task 2** | 📊 Grouped Bar Chart | Distribution of **app categories** by **Free vs Paid** types    |
| **Task 3** | 🫧 Bubble Chart      | Size of bubbles represents **total installs** per **category**  |

Each task folder includes:

.ipynb notebook

.html interactive visualization

images/ for screenshots

README.md describing the task

Final.ipynb includes all the 3 tasks code combined

Dashboard.html - Web dashboard

📈 Main Analysis Summary
The main analysis notebook (Play Store Data Analysis.ipynb) explores:

Top categories by number of apps

Category-wise installs and reviews

Rating trends

Revenue potential by app type

Comparison of free vs paid apps

Popular app genres

## Key Insights:

- *Category Dominance:* Some categories like Art & Design, Games, and Education dominate installs.
- *App Size vs Installs:* Smaller apps tend to have higher install numbers.
- *Paid Apps Revenue:* Although fewer, paid apps can generate significant revenue if targeted correctly.
- *Update Frequency:* Regular updates positively correlate with better app ratings.
- *Sentiment Trend:* Apps with timely support and bug fixes have better sentiment reviews.

---

## Future Improvements:

- Building a recommendation model for developers to optimize app ratings and installs.
- Creating a dashboard for real-time tracking of app performance.
- Using NLP to deeply analyze user review sentiments.

---

## How to Run:

1. Clone the repository.
2. Open the Jupyter Notebook or .html files in your browser.
3. Install necessary Python libraries if needed:
   ```bash
   pip install pandas matplotlib plotly

4. Explore the graphs and analysis!




---

Author:

**Sravya Togarla**
Aspiring Data Analyst | Lifelong Learner | Python & Data Enthusiast
- Passionate about transforming raw data into actionable insights  
- Continuously learning and building hands-on projects  
Training Program: NullClass - Data Science Project Series
Linkedin:[https://www.linkedin.com/in/sravya-togarla   ]
GitHub: [https://github.com/Sravyatogarla/Google-Play-Store-Analytics]

---
📌 How to Use
1.Clone this repo:

git clone https://github.com/Sravyatogarla/Google-Play-Store-Data-Analysis.git

2.Open Jupyter Notebook or VS Code to run .ipynb files.

3.Explore the interactive charts in the html/ folder by opening them in any browser.


> Project Conclusion:
 
Through the analysis of Google play store data, we gained valuable insights into preferences, app performance, and market trends. It was observed that the majority of apps are free, with a higher concentration in categories like Family and Games.

User Sentiment analysis revealed that most feedback is positive, but apps, although they are fewer in number. Overall, this project highlights the importance of regular updates, user engagement, and strategic app pricing to succeed in the competitive play store environment











---
