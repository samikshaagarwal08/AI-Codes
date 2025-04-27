# Facts: Known weather conditions
facts = {
    'cloudy': False,
    'rainy': False,
    'windy': False,
    'temperature': 30  # Temperature in Celsius
}

# Rules: Inference rules for weather prediction
rules = [
    {'condition': ['cloudy', 'rainy'], 'conclusion': 'rain'},
    {'condition': ['windy', 'cloudy'], 'conclusion': 'stormy'},
    {'condition': ['temperature > 25'], 'conclusion': 'hot'},
    {'condition': ['temperature <= 25'], 'conclusion': 'cool'}
]

# Function for Forward Chaining
def forward_chaining(facts, rules):
    conclusions = []
    while True:
        progress = False
        for rule in rules:
            # Check if all conditions are met
            if all(check_condition(cond, facts) for cond in rule['condition']):
                if rule['conclusion'] not in facts:
                    facts[rule['conclusion']] = True
                    conclusions.append(rule['conclusion'])
                    progress = True
        if not progress:
            break
    return conclusions

# Function to check conditions for facts
def check_condition(cond, facts):
    if cond in facts:
        return facts[cond]  # Check if the fact is True or False
    elif cond == 'temperature > 25':
        return facts['temperature'] > 25  # Check temperature condition
    elif cond == 'temperature <= 25':
        return facts['temperature'] <= 25  # Check temperature condition
    return False

# Input conditions (can be modified as needed)
facts['cloudy'] = True
facts['rainy'] = True
facts['temperature'] = 20  # Modify for different outputs

# Running the expert system
conclusions = forward_chaining(facts, rules)

# Output the weather prediction
if conclusions:
    print("Weather Prediction:", ', '.join(conclusions))
else:
    print("No prediction can be made based on the conditions.")
