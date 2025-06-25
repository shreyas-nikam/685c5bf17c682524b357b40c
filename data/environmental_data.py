
# data/environmental_data.py

ECONOMIC_CLIMATE_SCENARIOS = {
    "Neutral": 1.0,
    "Recession (Mild)": 1.1, # Higher risk in recession
    "Recession (Severe)": 1.2, # Even higher risk
    "Economic Boom (Mild)": 0.9, # Lower risk in boom
    "Economic Boom (Strong)": 0.8, # Even lower risk
}

AI_INNOVATION_SCENARIOS = {
    "Neutral": 1.0,
    "Rapid Breakthroughs": 1.2, # Higher risk with rapid innovation
    "Slowdown in Innovation": 0.9, # Lower risk with slowdown
    "AI Winter": 0.8, # Even lower risk if AI development stagnates
    "Accelerated Adoption": 1.1, # Moderate increase if adoption is fast
}
