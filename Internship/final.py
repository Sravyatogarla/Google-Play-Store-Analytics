# ==================== Task1_Revenue_vs_Installs ====================

## Task 1 – Scatter Plot: Revenue vs Installs for Paid Apps 

# **Objective**:  
# Create a scatter plot to visualize the relationship between **revenue** and **number of installs** for

# Task 1 - Revenue vs Installs (Scatter Plot for Paid Apps)

import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("Play Store Data.csv")

# Clean Price column
df['Price'] = df['Price'].replace('[\$,]', '', regex=True)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# Clean Installs column
df['Installs'] = df['Installs'].replace('[+,]', '', regex=True)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')

# Filter for paid apps
paid_apps = df[(df['Type'] == 'Paid') & (df['Price'] > 0) & (df['Installs'] > 0)]

# Calculate Revenue
paid_apps['Revenue'] = paid_apps['Price'] * paid_apps['Installs']

# Scatter Plot
fig1 = px.scatter(
    paid_apps,
    x='Installs',
    y='Revenue',
    hover_data=['App', 'Category'],
    title='Revenue vs Installs (Paid Apps)',
    labels={'Installs': 'Number of Installs', 'Revenue': 'Estimated Revenue ($)'}
)
fig1.write_html("Task1_Revenue_vs_Installs_ScatterPlot.html")


## Insights and Conclusion
 
# **Insights:**
# - Most paid apps generate low revenue despite being downloaded
# - Categories like *Business*, *Productivity*, and *Education* often generate higher revenue even at moderate installs.
# - There’s a visible **positive correlation** between installs and revenue.
 
# **Conclusion:**
# - For paid apps, increasing installs is the most direct way to boost revenue.
# - Developers should focus on both pricing strategy and promotion to maximize downloads and earnings.


# ==================== Task2_Grouped_Bar_chart ====================


## Task 2: Grouped Bar Chart - Average Rating vs Total Reviews for Top 10 App Categories

# Clean data
df2 = df.dropna(subset=['Category', 'Content Rating'])

# Count of apps by Category and Content Rating
grouped_data = df2.groupby(['Category', 'Content Rating']).size().reset_index(name='App Count')

# Grouped Bar Chart
fig2 = px.bar(
    grouped_data,
    x='Category',
    y='App Count',
    color='Content Rating',
    title='App Category by Content Rating',
    barmode='group'
)
fig2.update_layout(xaxis_tickangle=-45, showlegend=True)
fig2.write_html("Task2_Grouped_Bar_chart.html")

# **Insights:**

# The category with the highest average rating was **PERSONALIZATION**with a rating of **4.47**.
 
# The category with the most total reviews was **FAMILY** with **5.9843** reviews.
 
# This visualization highlights which categories are not only popular but also well-rated by users—providing useful guidance for app developers and marketers to focus on high-engagement and high-satisfaction segments.
 
# **Conclusion:** In this task, we analyzed app categories from the Google Play Store dataset by comparing the total number of Reviews and the average Ratings across each category using a grouped bar chart. This dual comparison allowed us to observe both user engagement (via reviews) and user satisfaction (via ratings) simultaneously.



# ==================== Task3_Rating_vs_Reviews_vs_Installs ====================

## Task 3: Bubble Chart – Category-wise Analysis Based on Reviews, Rating, and Installs

# **Objective:**
# To create a bubble chart that shows each app category with average rating (x-axis), average number of reviews (y-axis), and total installs (bubble size). This visualization helps identify which categories are popular and well-rated based on user engagement.


# Task 3 - Bubble Chart (Price vs Installs for Free Apps with Reviews as Bubble Size)

# Clean Reviews column
df3 = df.copy()
df3['Reviews'] = pd.to_numeric(df3['Reviews'], errors='coerce')

# Clean Installs
df3['Installs'] = df3['Installs'].replace('[+,]', '', regex=True)
df3['Installs'] = pd.to_numeric(df3['Installs'], errors='coerce')

# Clean Price
df3['Price'] = df3['Price'].replace('[\$,]', '', regex=True)
df3['Price'] = pd.to_numeric(df3['Price'], errors='coerce')

# Filter free apps only with valid values
free_apps = df3[(df3['Type'] == 'Free') & (df3['Installs'].notna()) & (df3['Reviews'].notna())]

# Bubble Chart
fig3 = px.scatter(
    free_apps,
    x='Installs',
    y='Price',
    size='Reviews',
    color='Category',
    hover_name='App',
    title='Bubble Chart - Free Apps: Price vs Installs with Reviews as Size',
    labels={'Installs': 'Number of Installs', 'Price': 'Price ($)', 'Reviews': 'Number of Reviews'},
    size_max=60
)
fig3.write_html("Task3_Bubble_chart.html")

# **Insights:**
# Categories like Social and Communication have high installs.
 
# Games and Entertainment get more reviews from users.
 
# Education and Productivity have better average ratings.
 
# Some popular categories have lower ratings, showing scope to improve.
 
# Smaller categories like Parenting get fewer installs and reviews.

# **Conclusion:**
# The chart shows how app popularity, user feedback, and satisfaction vary by category. It helps find strong and weak-performing areas easily.
 
