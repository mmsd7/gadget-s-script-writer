import os
import csv
from openai import OpenAI

with open ('example.csv', encoding='unicode_escape') as f:
    reader = csv.DictReader(f)

    count = 0
    examples = []

    for row in reader:
        count += 1
        # print(row['c_one'])
        examples.append(row['column_1'])
        if count >23:
            break
# print(examples)
#
# client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)
#
# # input_list = ['Who won the Champions League in 2017?', 'Who won the World Cup in 2014?']
# input_list = data
#
# output= []
#
# for i in range(len(input_list)):
#   response = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are an experienced product review writer with a decade of professional experience. To begin, you'll familiarize yourself with an 'example' review, paying close attention to its tone, sentence structure, and overall voice. Afterward, you'll review the provided 'data,' which includes the specifications of the product. Your task is to craft a product review that is concise, within 150 words, and follows the writing style demonstrated in the provided 'example.' Your reviews should read like authentic human-written content, avoiding the use of technical jargon. Begin each review with the product's name followed by its description, and refrain from including a separate conclusion paragraph."},
#     {"role": "user", "content": r"Analyze the following 'example' text for tone, voice, vocabulary and sentence structure. Apply the identified elements to all your future output. Example- The Elegu Neptune three Pro is a top recommendation for those seeking an affordable yet high quality 3d printer. As of 2024, it stands as one of the best value for money options on the market. The Neptune three Pro doese nott compromise on features. Despite its attractive price point, it boasts advanced functionalities such as a direct drive and dual zaxis that are typically found in premium models. This user friendly device arrives 90% preassembled, ensuring a hassle free setup from unboxing to first print within half an hour. The Pro version introduces several enhancements, including a direct drive that firmly handles slippery filaments like TPU, dual Z screws for stable printing, and an inbuilt task plate. All the beloved features of the predecessor, the Neptune three, have been retained or improved upon in this model. One of the standout features of the Neptune three Pro is its PEI coated build plate. This plate optimally adheres to prints during the printing process and easily releases them when cooled. The bed leveling process is swift and accurate, requiring minimal adjustments. The removable touchscreen interface is user friendly and displays thumbnails when using Elegu's slicing software. The Neptune three Pro package includes all the necessary tools for assembly and maintenance. Spare nozles, a micro SD card with a USB adapter, and a sample of white PLA for your first print. A short instructional video provided on the micro SD card guides users through the assembly process. Aesthetically, the Neptune three Pro is a significant upgrade from its predecessor. The earlier plain black frame has been replaced with a sleek gray aluminum one featuring painted stripes, an inspiring create the future slogan on the front. One of the major upgrades is the Gantry ride, which now includes a dual gear direct drive that effectively handles materials like TPU. This machine also boasts three cooling fans and an enhanced aluminum heatsink. Elegu has incorporated a new TC four titanium alloy throat tube, although it still includes a piece of PTFE tubing. While this limits the hot end to 260 degrees, it is more than sufficient for most 3d printing enthusiasts. The Neptune three Pro arrives mostly assembled, requiring just a few screws to complete its setup. It features automatic bed leveling using an inductive probe, which checks 36 points across the bed. Thumbs up, that's for sure."},
#     {"role": "assistant", "content": r"Tone- The tone of this text is informative and positive. It provides detailed information about the Elegu Neptune three Pro 3D printer and its various features, highlighting its affordability and high quality. The tone is enthusiastic and praises the printer for its capabilities and upgrades. Voice- The voice in this text is authoritative and objective. It presents facts and features of the Neptune three Pro without expressing personal opinions or biases. The voice is focused on conveying information to potential buyers. Vocabulary- The vocabulary used in the text is technical and specific to 3D printing. It includes terms such as 'direct drive,' 'dual z-axis,' 'PEI coated build plate,' 'slicing software,' and 'automatic bed leveling.' These terms are used to describe the printer's features accurately and cater to a target audience familiar with 3D printing technology. Sentence Structure- The sentences in the text are generally well-structured and concise. They provide clear and detailed information about the product, its features, and its advantages. The sentences are a mix of short and longer sentences, ensuring readability and variety in the text. Applying Identified Elements to Future Output- In future output, I will aim to maintain an informative and positive tone when providing information or recommendations. I will use an authoritative and objective voice to convey facts and details, especially when discussing technical or specialized topics. I will select appropriate vocabulary that is specific to the subject matter and catered to the target audience's knowledge level. Additionally, I will continue to use a mix of sentence structures to ensure clarity and readability in the text."},
#     {"role": "user", "content": input_list[i]}
#   ],
#   temperature=1, max_tokens=256, top_p=1, frequency_penalty=0, presence_penalty=0
#   )
#
#   chat_response = response.choices[0].message.content
#   output.append(chat_response)
#
# with open('workboot.text', 'w') as file:
#     file.writelines(output)