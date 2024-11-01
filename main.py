import pandas as pd
import sqlite3
import ssl

# Disable SSL verification
ssl._create_default_https_context = ssl._create_unverified_context

con = sqlite3.connect("chicago_school")
cur = con.cursor()

df = pd.read_csv('ChicagoPublicSchools.csv')
df.to_sql("CHICAGO_PUBLIC_SCHOOLS_DATA", con, if_exists='replace', index=False)
print("Data has been converted into the database")

con.commit()
print(df)

statement = '''SELECT COUNT(name) FROM PRAGMA_TABLE_INFO('CHICAGO_PUBLIC_SCHOOLS_DATA')'''
metadata = con.execute(statement).fetchone()[0]
print(f"Metadata counted: {metadata}")

statement2 = '''SELECT name,type,length(type) FROM PRAGMA_TABLE_INFO('CHICAGO_PUBLIC_SCHOOLS_DATA')'''
metadata2 = con.execute(statement2).fetchall()
print(f"Metadata counted: {metadata2}")

#Question 1
print("-----------------------------------------------------------------------------------------------")
problem_1 = ''' SELECT COUNT(*) 
                FROM CHICAGO_PUBLIC_SCHOOLS_DATA
                WHERE Elementary_Middle_HighSchool = 'ES' '''
exe1 = con.execute(problem_1).fetchone()[0]
print(f"There are {exe1} Elementary Schools in the dataset.")

#Question 2
print("-----------------------------------------------------------------------------------------------")
problem_2 = ''' SELECT MAX(SAFETY_SCORE) FROM CHICAGO_PUBLIC_SCHOOLS_DATA '''
exe2 = con.execute(problem_2).fetchone()[0]
print(f"Max safety score: {exe2}")

#Question 3
print("-----------------------------------------------------------------------------------------------")
problem_3 = ''' SELECT NAME_OF_SCHOOL 
                FROM CHICAGO_PUBLIC_SCHOOLS_DATA
                WHERE SAFETY_SCORE = 99.0 '''
exe3 = con.execute(problem_3).fetchall()
exe3_final = [name3[0] for name3 in exe3]
print("Schools that have highest safety score: ", ', '.join(exe3_final))

#Question 4
print("-----------------------------------------------------------------------------------------------")
problem_4 = ''' SELECT NAME_OF_SCHOOL
                FROM CHICAGO_PUBLIC_SCHOOLS_DATA
                ORDER BY AVERAGE_STUDENT_ATTENDANCE DESC
                LIMIT 10
'''
exe4 = con.execute(problem_4).fetchall()
exe4_final = [name4[0] for name4 in exe4]
print("Top 10 schools with highest average student attendance:", ', '.join(exe4_final))

#Question 5
print("-----------------------------------------------------------------------------------------------")
problem_5 = ''' SELECT NAME_OF_SCHOOL
                FROM CHICAGO_PUBLIC_SCHOOLS_DATA
                ORDER BY AVERAGE_STUDENT_ATTENDANCE ASC
                LIMIT 5
'''
exe5 = con.execute(problem_5).fetchall()
exe5_final = [name5[0] for name5 in exe5]
print("5 schools with the lowest attendance:", ', '.join(exe5_final))

#Question 6
print("-----------------------------------------------------------------------------------------------")
problem_6 = ''' SELECT NAME_OF_SCHOOL
                FROM CHICAGO_PUBLIC_SCHOOLS_DATA
                WHERE CAST(REPLACE(AVERAGE_STUDENT_ATTENDANCE, '%', '') AS DOUBLE ) < 70 '''
exe6 = con.execute(problem_6).fetchall()
exe6_final = [name6[0] for name6 in exe6]
print("Schools with average attendance less than 70%:", ', '.join(exe6_final))

#Question 7
print("-----------------------------------------------------------------------------------------------")
problem_7 = ''' SELECT COMMUNITY_AREA_NAME, SUM(COLLEGE_ENROLLMENT)
                FROM CHICAGO_PUBLIC_SCHOOLS_DATA
                GROUP BY COMMUNITY_AREA_NAME '''
exe7 = con.execute(problem_7).fetchall()
exe7_final = [f"{name7[0]}: {name7[1]}" for name7 in exe7]
print("Total College Enrollment for each Community Area:", ", ".join(exe7_final))


