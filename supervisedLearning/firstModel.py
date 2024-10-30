average_height = 160 / 251
average_speed = 3 / 9
weather = {"cloudy":10/14,
           "rainy":2/14,
           "sunny":14/14}

# How much each input contibutes
weights = {
     "weight_height":0.4,
     "weight_speed":0.5,
     "weight_weather":0.1
}

def neuralNetwork(input):
    contribution_speed = input[0] * weights["weight_speed"]
    contribution_height = input[1] * weights["weight_height"]
    contribution_weather = input[2] * weights["weight_weather"]
    output = contribution_speed + contribution_height + contribution_weather
    return output

# Using the nework
input = [average_speed, average_height, weather["cloudy"]]
result = neuralNetwork(input=input)
print(result)