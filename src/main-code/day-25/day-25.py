import pandas

# Reading a CSV file
data = pandas.read_csv("weather_data.csv")

# Converting DataFrame to dictionary
data_dict = data.to_dict()
print(data_dict)

# Converting Series to list
temp_list = data.temp.to_list()
print(temp_list)

# Getting the average/mean temperature
average_temp = round(data.temp.mean())
print(average_temp)

# Getting the max temperature
max_temp = round(data.temp.max())
print(max_temp)

# Get data in columns
conditions = data.condition
print(conditions)

# Get data in row
hottest_day = data[data.temp == max_temp]
print(hottest_day)

monday = data[data.day == "Monday"]
monday_temp = (int(monday.temp) * 9/5) + 32
print(monday_temp)

# Create DataFrame from scratch
student_dict = {
    "students": ["Shin Thant Kaung", "Bhong Myat Linn", "Lin Yati Ko", "May Yuya Thet"],
    "scores": [85, 90, 97, 86.7]
}

student_data = pandas.DataFrame(student_dict)
student_data.to_csv("student_scores.csv")
