import openai
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Replace with your OpenAI API key
openai.api_key = "your-api-key"

# Sample function to load or simulate capital market data (you can replace it with real data)
def get_market_data():
    dates = pd.date_range(start="2023-01-01", periods=100)
    prices = [100 + i * 0.5 + (i % 10) for i in range(100)]  # Simulated market data
    return pd.DataFrame({"Date": dates, "Price": prices})

# Plotting the market data
def plot_market_data(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data["Date"], data["Price"], label="Market Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title("Capital Market Price Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()

# Function to get forecast from ChatGPT
def get_forecast_from_chatgpt(data):
    # Convert the data to a format ChatGPT can understand
    data_str = data.to_string(index=False)
    
    # Create the prompt for ChatGPT
    prompt = f"""
    Here is the recent capital market data:
    {data_str}

    Based on this data, can you provide a forecast for the next few days? Analyze the trend and give insights on potential future movements.
    """
    
    # Call the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT-3.5 model (you can use GPT-4 or newer)
        prompt=prompt,
        max_tokens=150
    )
    
    forecast = response.choices[0].text.strip()
    return forecast

# Main function to run the app
def main():
    # Step 1: Get the market data
    market_data = get_market_data()

    # Step 2: Plot the market data
    plot_market_data(market_data)

    # Step 3: Get forecast from ChatGPT
    forecast = get_forecast_from_chatgpt(market_data.tail(20))  # Use the last 20 days of data
    print("\nForecast from ChatGPT:")
    print(forecast)

if __name__ == "__main__":
    main()
