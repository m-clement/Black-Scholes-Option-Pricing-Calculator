# Black-Scholes formula for European-style options

import numpy as np
from scipy.stats import norm

# Gather inputs from the user
S = float(input("Enter the current price of the underlying asset: "))
K = float(input("Enter the strike price of the option: "))
T_days = int(input("Enter the time to maturity of the option (in days): "))
T = T_days / 365.0  # Convert days to years for the formula
sigma = float(input("Enter the volatility of the underlying asset: "))
r = float(input("Enter the risk-free interest rate (as a decimal, e.g., 0.05 for 5%): "))
option_type = input("Enter the type of option (Call or Put): ").lower()

# Convert shorthand to full option type for clarity in later calculations
if option_type in ["c", "call"]:
    option_type = "call"
elif option_type in ["p", "put"]:
    option_type = "put"

# Function to calculate the price using Black-Scholes formula
def blackScholes(r, S, K, T, sigma, option_type):   
    # Calculate d1 and d2 parameters
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    
    try:
        # Return call option price
        if option_type == "call":
            return S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        # Return put option price
        elif option_type == "put":
            return K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
    except:
        print("Error: Please check your inputs.")

# Display the calculated option price
print("\nThe price of the option is: ", round(blackScholes(r, S, K, T, sigma, option_type), 2))