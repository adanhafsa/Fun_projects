def get_weather_input():
    """Get valid weather input from user with retry on invalid input"""
    valid_weather = ['sunny', 'rainy', 'cold', 'windy', 'snowy', 'humid']
    while True:
        weather = input("What's the weather? (sunny/rainy/cold/windy/snowy/humid): ").lower()
        if weather in valid_weather:
            return weather
        print("Invalid weather condition. Please try again.")

def get_temperature_input():
    """Get valid temperature input from user with retry on invalid input"""
    while True:
        try:
            temp = float(input("Enter temperature (°C): "))
            return temp
        except ValueError:
            print("Invalid temperature. Please enter a number.")

def generate_recommendation(weather, temp):
    """Generate weather recommendation based on conditions and temperature"""
    recommendations = {
        'sunny': "Wear a t-shirt and sunglasses",
        'rainy': "Wear a waterproof jacket and carry an umbrella",
        'cold': "Wear a warm coat and scarf",
        'windy': "Wear a windbreaker and secure loose items",
        'snowy': "Wear waterproof boots and gloves",
        'humid': "Wear light, breathable clothing"
    }
    
    base_recommendation = recommendations.get(weather, "")
    
    # Add temperature-based additions
    additions = []
    if weather == 'sunny' and temp > 25:
        additions.append("apply sunscreen")
    if weather == 'cold' and temp < 0:
        additions.append("wear thermal layers")
    
    # Combine base recommendation with additions
    if additions:
        return f"{base_recommendation}, and {', '.join(additions)}."
    else:
        return f"{base_recommendation}."

def main():
    print("Advanced Weather Recommendation System")
    print("------------------------------------")
    
    weather = get_weather_input()
    temp = get_temperature_input()
    
    recommendation = generate_recommendation(weather, temp)
    print(f"Recommendation: {recommendation}")

if __name__ == "__main__":
    main()      

