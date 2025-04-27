# Facts: Symptoms provided by the user
facts = {
    'fever': False,
    'cough': False,
    'runny_nose': False
}

# Rules: Inference rules for medical diagnosis
rules = [
    {'condition': ['fever', 'cough'], 'conclusion': 'flu'},
    {'condition': ['cough', 'runny_nose'], 'conclusion': 'cold'}
]

# Function for Forward Chaining
def forward_chaining(facts, rules):
    conclusions = []
    while True:
        progress = False
        for rule in rules:
            if all(facts.get(symptom, False) for symptom in rule['condition']):
                if rule['conclusion'] not in facts:
                    facts[rule['conclusion']] = True
                    conclusions.append(rule['conclusion'])
                    progress = True
        if not progress:
            break
    return conclusions

# User input to update symptoms
facts['fever'] = True
facts['cough'] = True

# Running the expert system
conclusions = forward_chaining(facts, rules)

# Output the diagnosis
if conclusions:
    print("Diagnosis:", ', '.join(conclusions))
else:
    print("No diagnosis can be made based on the symptoms.")
