# Australian Corpus of English (ACE)	

## Overview

The [Australian Corpus of English (ACE)](https://figshare.mq.edu.au/articles/dataset/Australian_Corpus_of_English_ACE_/24629712?file=43778418) corpus was compiled to match Australian data from 1986 to the standard American and British corpora (Brown and LOB) from the 1960s. It includes **1 million words of published text** in **500 samples from 15 categories of nonfiction and fiction**.

**Keywords**: Australian English, Corpus linguistics.

## Data Source

The original dataset is from [Macquarie University Research Data - Australian Corpus of English (ACE)](https://figshare.mq.edu.au/articles/dataset/Australian_Corpus_of_English_ACE_/24629712?file=43778418)  and licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Dataset Structure

After unzipping `ACE.zip`, the dataset under `ACE` contains:

- `data` contains 1718 `.txt` files including **plain** and **raw** two formats for each document.
- `Manul` contains 18 `.HTM` files with **source subtitles** and **author** information for each document.

## Download

You can download it directly from [Macquarie University Research Data - Australian Corpus of English (ACE)](https://figshare.mq.edu.au/articles/dataset/Australian_Corpus_of_English_ACE_/24629712?file=43778418).

You can also download it by running `download.py` in your terminal:

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
