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

# Usage:
data = feed_data('example.csv', 'column_1')

single_feed = random.choice(data)

# print(single_feed)

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

raw_data = product_description('product_info.csv', 'column_1')


client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)

output = []

for i in range(len(raw_data)):
  response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are an experienced product description and feature writer with a decade of professional experience. To begin, you'll familiarize yourself with an 'example' script, paying close attention to its tone, sentence structure, and overall voice. Afterward, you'll review the provided 'data,' which includes the specifications of the product. Your task is to craft a product description and feature that is concise, within 70 words, and follows the writing style demonstrated in the provided 'example.' Your writing should read like authentic human-written content, avoiding the use of technical jargon. Begin the review with the product's name followed by its description and features, and refrain from including a separate conclusion paragraph."},
    {"role": "user", "content": f"Analyze the following 'example' text for tone, voice, vocabulary and sentence structure. Apply the identified elements to all your future output. Example- {single_feed}."},
    # {"role": "assistant", "content": r"Tone- The tone of this text is informative and positive. It provides detailed information about the Elegu Neptune three Pro 3D printer and its various features, highlighting its affordability and high quality. The tone is enthusiastic and praises the printer for its capabilities and upgrades. Voice- The voice in this text is authoritative and objective. It presents facts and features of the Neptune three Pro without expressing personal opinions or biases. The voice is focused on conveying information to potential buyers. Vocabulary- The vocabulary used in the text is technical and specific to 3D printing. It includes terms such as 'direct drive,' 'dual z-axis,' 'PEI coated build plate,' 'slicing software,' and 'automatic bed leveling.' These terms are used to describe the printer's features accurately and cater to a target audience familiar with 3D printing technology. Sentence Structure- The sentences in the text are generally well-structured and concise. They provide clear and detailed information about the product, its features, and its advantages. The sentences are a mix of short and longer sentences, ensuring readability and variety in the text. Applying Identified Elements to Future Output- In future output, I will aim to maintain an informative and positive tone when providing information or recommendations. I will use an authoritative and objective voice to convey facts and details, especially when discussing technical or specialized topics. I will select appropriate vocabulary that is specific to the subject matter and catered to the target audience's knowledge level. Additionally, I will continue to use a mix of sentence structures to ensure clarity and readability in the text."},
    {"role": "user", "content": raw_data[i]}
  ],
  temperature=1, max_tokens=256, top_p=1, frequency_penalty=0, presence_penalty=0
  )

  chat_response = response.choices[0].message.content
  output.append(chat_response)

with open('gadget.text', 'w') as file:
    file.writelines(output)
#
