import pandas as pd

dataset = pd.read_csv("dataset.csv")

language = "Spanish"
mode = "Silent"
pace = "Normal"
words = 132
output = {}

final_data = dataset[dataset["Language"] == language]
final_data = final_data[final_data["Type"] == mode]
final_data = final_data[final_data["Pace"] == pace]
words_per_second = dataset["Words"] / dataset["Time"]
average_reading_speed = sum(words_per_second) / len(words_per_second)
output["average_reading_speed"] = average_reading_speed

# calculating average error
error = abs((final_data["Words"] / final_data["Time"]) - average_reading_speed)
print(error)
average_error = sum(error) / len(error)
output["average_reading_speed_error"] = average_error

# calculating results regarding parameters given

output["time"] = words / average_reading_speed
output["time_error"] = output["time"] / average_error
print(output)