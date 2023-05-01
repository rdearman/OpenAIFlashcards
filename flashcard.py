#!/usr/bin/python
#!/usr/bin/env python

import openai
import csv
import os
import configparser
import traceback
import csv

# Method to read config file settings
def read_config():
    config = configparser.ConfigParser()
    config.read('configurations.ini')
    return config

config = read_config()
openai.api_key = config['OPENAPI']['OPENAI_API_KEY']

def generate_flashcards(topic):
    # Define the prompt for generating flashcards
    prompt = f"Generate aproximately 200 flashcards for the topic '{topic}' in csv format, with no duplication. The format of the csv should be like this: 'Question';;'Answer'"

    # Generate the flashcards using OpenAI's GPT-3 API
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # Parse the response to extract the generated flashcards
    flashcards = response.choices[0].text.strip().split("\n")

    # Write the flashcards to a CSV file
    filename = f"{topic}_flashcards.csv"
    with open(filename, "w", newline="") as f:
        for flashcard in flashcards:
            print (flashcard,file=f)

    print(f"{len(flashcards)} flashcards generated and saved to {filename}.")

# Example usage
generate_flashcards("Geography of the United Kingdom")
