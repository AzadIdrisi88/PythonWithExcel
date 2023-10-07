import pandas as pd


def readExcel():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    df = pd.read_csv('test.csv')
    rollno = df["rollno"]
    name = df["name"]
    english = df["english"]
    physics = df["physics"]
    math = df["math"]
    print(df)
    return name, english, physics, rollno, math
    
name, english, physics, rollno, math=readExcel()


def calculate_result_percentage_division(english, physics, math):
    results = []
    for e, p, m in zip(english, physics, math):
        total_marks = e + p + m
        percentage = round((total_marks / 3), 2)
        if e < 40 or p < 40 or m < 40:
            result = "Fail"
            division = "N/A"
        elif percentage >= 75:
            result = "Pass"
            division = "First"
        elif percentage >= 60:
            result = "Pass"
            division = "Second"
        elif percentage >= 40:
            result = "Pass"
            division = "Third"
        else:
            result = "Fail"
            division = "N/A"

        results.append((result, percentage, division))

    return results


name, english, physics, rollno, math = readExcel()
results = calculate_result_percentage_division(english, physics, math)

# Create a new DataFrame to store the results
result_df = pd.DataFrame({
    "Roll No": rollno,
    "Name": name,
    "Result": [result for result, _, _ in results],
    "Percentage": [percentage for _, percentage, _ in results],
    "Division": [division for _, _, division in results]
})

# Print the result DataFrame
print(result_df)

# read data from csv
# write data to csv
# 
