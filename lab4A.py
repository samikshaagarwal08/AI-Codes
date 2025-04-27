# Facts: Symptoms the user has
facts = {
    'fever': False,
    'cough': False,
    'runny_nose': False
}

# Rules: Inference rules for diagnosing cold or flu
rules = [
    {'condition': ['fever', 'cough'], 'conclusion': 'flu'},
    {'condition': ['cough', 'runny_nose'], 'conclusion': 'cold'}
]

# Function to apply forward chaining
def forward_chaining(facts, rules):
    inferred_facts = facts.copy()
    conclusions = []
    
    # Track if new facts were inferred
    progress = True
    
    while progress:
        progress = False  # Reset progress flag
        for rule in rules:
            # Check if all conditions in the rule are true in the facts
            if all(inferred_facts.get(condition, False) for condition in rule['condition']):
                if rule['conclusion'] not in inferred_facts:  # Only add conclusion if not already inferred
                    inferred_facts[rule['conclusion']] = True
                    conclusions.append(rule['conclusion'])
                    progress = True  # Mark progress to continue the loop
    return conclusions

# User input to update symptoms
facts['fever'] = True
facts['cough'] = True

# Run the forward chaining algorithm
conclusions = forward_chaining(facts, rules)

# Print the results
if conclusions:
    print("Diagnosis:", ', '.join(conclusions))
else:
    print("No conclusion can be made based on the symptoms.")
