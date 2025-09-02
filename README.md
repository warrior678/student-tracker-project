# Student Tracker Dashboard
# 🎓 Student Tracker Project  
A Python and SQL-based analytics solution for monitoring student performance across grades, attendance, and engagement—built for BI roles in academic and EdTech environments.

---

## 📌 Project Overview  
This project simulates a real-world academic analytics workflow where student data is collected, cleaned, analyzed, and visualized to uncover performance trends and identify at-risk students. The solution is built using Python (Pandas, Matplotlib) and SQL, with a modular structure that allows easy extension into dashboards or reporting pipelines.

The goal is to demonstrate how raw student data can be transformed into actionable insights for academic institutions, HR departments, or EdTech platforms.

---

## 🧠 What This Project Does  
- Loads and cleans student performance data (grades, attendance, participation)
- Uses SQL queries to segment students based on risk factors
- Applies Pandas for data wrangling and transformation
- Visualizes trends using Matplotlib (e.g., attendance over time, grade distribution)
- Generates summary insights to support academic decision-making

---

## 📈 Analytics Highlights  
- **Descriptive Analytics**:  
  - Average grades and attendance across semesters  
  - Distribution of students by performance tier  
  - Identification of top-performing and underperforming cohorts  

- **Diagnostic Analytics**:  
  - Correlation between attendance and academic performance  
  - Impact of extracurricular participation on grades  
  - Flagging students with declining trends over time  

- **Segmentation Logic (SQL)**:  
  - Students with <75% attendance  
  - Grade-based clustering (A/B/C/D/F)  
  - Multi-factor risk profiling using SQL joins and filters  

---

## ❓ Questions This Project Can Answer  
- Which students are consistently underperforming across subjects?  
- Is there a correlation between attendance and academic success?  
- How many students fall below the acceptable attendance threshold?  
- Which grade bands show the highest improvement or decline over time?  
- Are students with extracurricular involvement performing better academically?  
- What percentage of students are at risk based on combined metrics?

---

## 🛠️ Tech Stack  
- Python (Pandas, Matplotlib)  
- SQL (SQLite or MySQL)  
- Jupyter Notebook  
- Git & GitHub  

---

## 📂 Folder Structure  
├── data/              # Sample datasets
├── notebooks/         # Jupyter analysis scripts
├── sql/               # SQL queries and schema
├── visuals/           # Charts and screenshots
├── README.md          # Project documentation 
## 📊 Analytics Questions & Insights

This section highlights the analytical depth of the project, showcasing how data was used to uncover trends, segment students, and support academic decision-making. Each question is backed by statistical logic and sample insights based on a hypothetical dataset of 500 students.

---

### 1. Which students are consistently underperforming across subjects?
- **Method**: Grouped by student ID and calculated mean grade across subjects.
- **Insight**: *42 students (8.4%) scored below 60% in all subjects—flagged for academic support.*

---

### 2. Is there a correlation between attendance and academic success?
- **Method**: Pearson correlation between attendance % and average grade.
- **Insight**: *Correlation coefficient: **0.68** — moderately strong positive relationship.*

---

### 3. How many students fall below the acceptable attendance threshold?
- **Threshold**: 75% attendance
- **Insight**: *117 students (23.4%) fall below the threshold.*

---

### 4. Which grade bands show the highest improvement or decline over time?
- **Method**: Compared semester-wise averages by grade band.
- **Insight**: *Grade B students improved by +6.2%, Grade D declined by -3.8%.*

---

### 5. Are students with extracurricular involvement performing better academically?
- **Method**: Compared average grades of involved vs. non-involved students.
- **Insight**: *Involved students averaged **74.5%**, others averaged **66.2%**.*

---

### 6. What percentage of students are at risk based on combined metrics?
- **Criteria**: Attendance < 75%, Avg. Grade < 60%, No extracurriculars
- **Insight**: *28 students (5.6%) meet all risk criteria.*

---

### 7. What is the distribution of grades across the student population?
- **Insight**: *Grade A: 18%, B: 32%, C: 28%, D: 15%, F: 7%*

---

### 8. Which subjects have the highest failure rates?
- **Insight**: *Math: 12.4%, Science: 9.8%, English: 6.2%*

---

### 9. What is the average improvement in grades across semesters?
- **Insight**: *Average improvement: +4.1 percentage points*

---

### 10. Are students with high attendance but low grades an exception?
- **Insight**: *Only 9 students (1.8%) had >90% attendance but <60% grades—suggesting attendance alone isn't always predictive.*

---Python codes to find Failure subject rate 
import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David'],
    'math': [35, 60, 45, 25],
    'science': [55, 30, 65, 40],
    'english': [70, 50, 38, 42]
}
df = pd.DataFrame(data)


subjects = ['math', 'science', 'english']


fail_rates = [(df[sub] < 40).mean() * 100 for sub in subjects] 




plt.bar(subjects, fail_rates, color='crimson')
plt.title('Failure Rate by Subject')
plt.ylabel('Failure Rate (%)')
plt.show() 
<img width="638" height="474" alt="image" src="https://github.com/user-attachments/assets/a0e4c2d7-2c4d-4cfd-b780-c578ffdbca07" /> 
import pandas as pd
import matplotlib.pyplot as plot
data = {
    'Student': ['Alice', 'Bob', 'Charlie'],
    'First_Term': [80, 70, 90],
    'Final_Term': [85, 75, 95]
}
df = pd.DataFrame(data)


ax = df.set_index('Student').plot(kind='bar', stacked=True, figsize=(8, 6))
ax.set_title('Performance Comparison: First vs Final Term')
ax.set_ylabel('Scores')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

df['Improvement'] = df['Final_Term'] - df['First_Term']


ax = df.plot(x='Student', y='Improvement', kind='line', marker='o', figsize=(8, 6))
ax.set_title('Improvement from First Term to Final Term')
ax.set_ylabel('Score Improvement')
plt.grid(True)
plt.tight_layout()
plt.savefig('charts/improvement_trend.png', dpi=300)
plt.close()
<img width="800" height="600" alt="Performance Comparison First vs Final" src="https://github.com/user-attachments/assets/6c4aff6e-eff9-454e-98c2-6dd76aeada0a" />




---

## 🚀 How to Run  
1. Clone the repository  
2. Install dependencies: `pip install -r requirements.txt`  
3. Open `student_analysis.ipynb` in Jupyter Notebook  
4. Run SQL queries from the `sql/` folder to explore segmentation logic  

---

## 📚 Use Case Alignment  
This project is ideal for:  
- BI Analyst roles in EdTech, HR, or institutional reporting  
- Candidates preparing for SQL + Python analytics interviews  
- Recruiters evaluating modular, role-specific analytics portfolios  
- Academic institutions seeking data-driven student performance tracking
-  

---

## 🧠 Author  
**Gautam** — Freelance BI Analyst & Prompt Engineering Tutor  
📧 Email: [your email]  
🔗 LinkedIn: [your LinkedIn]  











---
