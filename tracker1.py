import pandas as pd
Students = pd.read_csv('Students.csv')
Grade = pd.read_csv('Grade.csv')
Attendance = pd.read_csv('Attendance.csv')
print("Students Table:")
print(Students.head(),"\n")
print("Grade Table:")
print(Grade.head(),"\n")
print("Attendance Table:")
print(Attendance.head())
#Show all students from class 6

print("\nStudents from Class 6:")
print(Students[Students["Class"]== 6])
#Average grade per Student
avg_grades = Grade.groupby('Student_id')['Grade'].mean()
print(avg_grades)
# Count of Present days per Student
print("\nAttendance Count (Present only):")
full_attendance = Attendance[Attendance['Status'] == 'Present']
attendance_count = full_attendance.groupby('Student_id').count()
print(attendance_count)
# Merge Students and Grade
print("\nMerged Students + Grade Table:")
merged = pd.merge(Students, Grade, on='Student_id')
print(merged.head())
# Top 3 Students with Highest Average Grades.
top3 = merged.sort_values( by = 'Grade',ascending= False).head(3)
print(top3)
# Show Students who scored more than 80
high_scores = Grade[Grade['Grade']>80]
print(high_scores)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Average Grades per Student
avg_grades = Grade.groupby('Student_id')['Grade'].mean().reset_index()
#Attendance Count
Present = Attendance[Attendance['Status'] == 'Present']
Attendance = Present.groupby('Student_id').size().reset_index(name= 'present_day')
#Merge all
merged = pd.merge(Students,avg_grades, on= 'Student_id')
final = pd.merge(merged,Attendance,on= 'Student_id',how= 'left'  )
print("Total Students:", final.shape[0])
print("Average Grade:",round(final['Grade'].mean(),2))
print("Average Attendance Days:",round(final['present_day'].mean(),2))
# Barchart - Average Grades by Class.
plt.figure(figsize= (8,5))
sns.barplot(data= final, x= 'Class',y= 'Grade',estimator= 'mean')
plt.title('Average Grade by Class')
plt.ylabel('Average Grade')
plt.show()
attendance_group = pd.cut(final['present_days'], bins=[0, 3, 6, 10], labels=['Low', 'Medium', 'High'])
attendance_count = attendance_group.value_counts()
plt.pie(attendance_count, labels=attendance_count.index, autopct='%1.1f%%')
plt.title('Attendance Distribution')
plt.show()
# Top 5 Students by Grade
top5 = final.sort_values(by='Grade', ascending=False).head(5)
plt.figure(figsize=(8,5))
sns.barplot(data=top5, x='Name', y='Grade')
plt.title('Top 5 Students by Grade')
plt.ylabel('Grade')
plt.show()
# Correlation: Attention vs Grade
plt.figure(figsize=(7,5))
sns.scatterplot(data=final, x='present_days', y='grade', hue='Class')
plt.title('Attendance vs Grades')
plt.xlabel('Present Days')
plt.ylabel('Grade')
plt.show()
# Final Report
final[['Name', 'Class', 'Grade', 'present_days']].to_csv('Student_dashboard_report.csv', index=False)















