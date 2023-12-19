import os
import csv
import random
from openai import OpenAI

def feed_data(filename, column_name, limit=23):
    examples = []

    with open(filename, encoding='unicode_escape') as f:
        reader = csv.DictReader(f)
        count = 0

        for row in reader:
            count += 1
            examples.append(row[column_name])
            if count > limit:
                break

    return examples

def get_random_example(data):
    return random.choice(data)

def product_description(filename, column_name, limit=5):
    input_list = []

    with open(filename, encoding='unicode_escape') as f:
        reader = csv.DictReader(f)
        count = 0

        for row in reader:
            count += 1
            input_list.append(row[column_name])
            if count > limit:
                break

    return input_list

def generate_product_descriptions(raw_data):
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    output = []

    for i in range(len(raw_data)):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an experienced product description and feature writer with a decade of professional experience. To begin, you'll familiarize yourself with an 'example' script, paying close attention to its tone, sentence structure, and overall voice. Afterward, you'll review the provided 'data,' which includes the specifications of the product. Your task is to craft a product description and feature that is concise, within 70 words, and follows the writing style demonstrated in the provided 'example.' Your writing should read like authentic human-written content, avoiding the use of technical jargon. Begin the review with the product's name followed by its description and features, and refrain from including a separate conclusion paragraph."},
                {"role": "user", "content": f"Analyze the following 'example' text for tone, voice, vocabulary, and sentence structure. Apply the identified elements to all your future output. Example- {get_random_example(raw_data)}."},
                {"role": "user", "content": raw_data[i]}
            ],
            temperature=1, max_tokens=256, top_p=1, frequency_penalty=0, presence_penalty=0
        )

        chat_response = response.choices[0].message.content
        output.append(chat_response)

    return output

def save_descriptions_to_file(output, filename='gadget.txt'):
    with open(filename, 'w') as file:
        file.writelines(output)

if __name__ == "__main__":
    example_data = feed_data('example.csv', 'column_1')
    raw_data = product_description('product_info.csv', 'column_1')
    descriptions = generate_product_descriptions(raw_data)
    save_descriptions_to_file(descriptions)
