# Australian Corpus of English (ACE)	

## Overview

**Keywords**: Australian English; Corpus linguistics

The [Australian Corpus of English (ACE)](https://figshare.mq.edu.au/articles/dataset/Australian_Corpus_of_English_ACE_/24629712?file=43778418) corpus was compiled to match Australian data from 1986 to the standard American and British corpora (Brown and LOB) from the 1960s. It includes **1 million words of published text** in **500 samples from 15 categories of nonfiction and fiction**.

## Data Source

The original dataset is from [Macquarie University Research Data - Australian Corpus of English (ACE)](https://figshare.mq.edu.au/articles/dataset/Australian_Corpus_of_English_ACE_/24629712?file=43778418)  and licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). For any data usage concern, please refer to [Fair Self Assessment Summary](https://figshare.com/articles/dataset/Australian_Corpus_of_English_ACE_/24629712?file=43778418).

## Dataset Structure

After unzipping `ACE/ACE.zip`, the dataset contains:

- `data`: There are 1717 `.txt` files in total, where 17 `.txt` files summary all documents under its category, e.g. `ace_a.txt` is a **summary** of `A01a-plain.txt`, `A01a-raw.txt`, `A01b-plain.txt`, `A01b-raw.txt` and so on. Notice that there are 850 unique documents, and each document has **plain** and **raw** two formats.
- `Manul`: There are 18 `.HTM` files in total, where `INDEX.HTM` serves as an index file, and the other 17 `.HTM` files includes **source subtitles** and **author information** for each category, e.g., `KATA.HTM` contains information of `A01a-plain.txt`, `A01a-raw.txt`, `A01b-plain.txt`, `A01b-raw.txt` and so on.

`ACE_clean/ACE_clean.csv` is a cleaned dataset created by [Gillian Law](https://github.com/GillianLaw). The cleaned dataset can also be downloaded from [Hugging Face - SouthernCrossAI/ACE_Australian_Corpus_of_English](https://huggingface.co/datasets/SouthernCrossAI/ACE_Australian_Corpus_of_English).

## Download

You can download it directly from [Macquarie University Research Data - Australian Corpus of English (ACE)](https://figshare.mq.edu.au/articles/dataset/Australian_Corpus_of_English_ACE_/24629712?file=43778418).

You can also download it by running `utils/download.py` in your terminal:

```bash
$ python3 download.py --help                       
usage: download.py [-h] [--save_path SAVE_PATH] [--unzip]

Download a file and optionally unzip it.

options:
  -h, --help            show this help message and exit
  --save_path SAVE_PATH
                        Path to save the downloaded file.
  --unzip               Unzip the file if it's a zip archive.
```

For example:

- `python3 download.py --save_path my_data --unzip` will download and unzip the dataset `ACE.zip` under the directory `my_data`.
- `python3 download.py` will only download under the current directory.

## License

This repository is licensed under [MIT](https://opensource.org/license/mit).
