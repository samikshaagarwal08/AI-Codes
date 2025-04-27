import spacy

# Load the pre-trained spaCy model for English
nlp = spacy.load("en_core_web_sm")

# Define the text
text = "Barack Obama was born on August 4, 1961, in Honolulu, Hawaii. He was the 44th President of the United States."

# Process the text with spaCy to get a doc object
doc = nlp(text)

# Iterate through the entities in the doc and print them
for entity in doc.ents:
    print(f"Entity: {entity.text}, Label: {entity.label_}")




# Entity: Barack Obama, Label: PERSON
# Entity: August 4, 1961, Label: DATE
# Entity: Honolulu, Label: GPE
# Entity: Hawaii, Label: GPE
# Entity: 44th, Label: ORDINAL
# Entity: United States, Label: GPE
