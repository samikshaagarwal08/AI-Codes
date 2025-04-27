# Facts: Known facts
facts = {'fever': True, 'cough': True}

# Rules: Inference rules for diagnosing cold or flu
rules = [
    {'conclusion': 'flu', 'condition': ['fever', 'cough']},
    {'conclusion': 'cold', 'condition': ['cough', 'runny_nose']}
]

# Function for backward chaining
def backward_chaining(goal, facts, rules):
    if goal in facts:
        return True  # Goal is a fact
    for rule in rules:
        if rule['conclusion'] == goal:
            if all(backward_chaining(cond, facts, rules) for cond in rule['condition']):
                return True  # All conditions for the goal are true
    return False

# Example usage
goal = 'flu'  # The goal we want to prove
if backward_chaining(goal, facts, rules):
    print(f"Goal '{goal}' can be inferred!")
else:
    print(f"Goal '{goal}' cannot be inferred.")
