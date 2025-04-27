# Facts: Known information about the student's preferences and skills
facts = {
    'maths': False,
    'science': False,
    'arts': False,
    'sports': False,
    'communication_skills': False,
}

# Rules: Inference rules for career guidance
rules = [
    {'condition': ['maths', 'science'], 'conclusion': 'Engineer'},
    {'condition': ['maths', 'communication_skills'], 'conclusion': 'Data Analyst'},
    {'condition': ['arts', 'communication_skills'], 'conclusion': 'Writer'},
    {'condition': ['sports'], 'conclusion': 'Athlete'},
    {'condition': ['science', 'arts'], 'conclusion': 'Researcher'},
]

# Function for Forward Chaining to deduce career
def forward_chaining(facts, rules):
    conclusions = []
    while True:
        progress = False
        for rule in rules:
            if all(facts.get(cond, False) for cond in rule['condition']):
                if rule['conclusion'] not in facts:
                    facts[rule['conclusion']] = True
                    conclusions.append(rule['conclusion'])
                    progress = True
        if not progress:
            break
    return conclusions

# User input: Ask student about their skills and preferences
facts['maths'] = True  # Student likes maths
facts['science'] = True  # Student is interested in science
facts['communication_skills'] = True  # Student has good communication skills

# Run the expert system
conclusions = forward_chaining(facts, rules)

# Output the career guidance
if conclusions:
    print("Suggested Career Paths:", ', '.join(conclusions))
else:
    print("No suitable career path can be suggested based on the given preferences and skills.")
