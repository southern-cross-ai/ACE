import os
import re
import pandas as pd


directory = 'data'


data = []
#regex to find paras
paragraph_splitter = re.compile(r'\.\n')


for filename in os.listdir(directory):
    if filename.endswith("plain.txt"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            content = file.read()
            # Split content into paragraphs 
            paragraphs = paragraph_splitter.split(content)
            for paragraph in paragraphs:
                data.append({"paragraph": paragraph.strip()})


df = pd.DataFrame(data)


regex_output_csv = 'regex_paragraphs.csv'
df.to_csv(regex_output_csv, index=False)

print(f"Data from .txt files saved to {regex_output_csv}")
