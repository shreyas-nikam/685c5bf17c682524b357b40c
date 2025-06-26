
# data/environmental_data.py
# Synthetic data for environmental modifiers

ECONOMIC_CLIMATE_SCENARIOS = {
    "Neutral": 1.0,
    "Recession (Downturn)": 1.15, # Higher risk in recession
    "Boom (Growth)": 0.85 # Lower risk in boom
}

AI_INNOVATION_SCENARIOS = {
    "Neutral": 1.0,
    "Rapid Breakthroughs": 1.2, # Higher risk with rapid AI innovation
    "Slowdown": 0.9 # Lower risk with AI innovation slowdown
}
