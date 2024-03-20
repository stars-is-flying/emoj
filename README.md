# Author: ablajan
# Mail: 2770532197@qq.com
# Time: 2024.3.20

text_box = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

emo_box = [
    "*_*", "^_^", "-_-", "#_#", "+_+", "@_@", "q_q", "$_$", "o_O", "O_o", "6_6", ")_(", "._.", ":_:", "'_'", "k_k", "?_?", "!_!", "<_>", ">_<", "n_N", "N_n", "e_e", "V_v", "v_V", ",_,"
]

def find_index_for_en(letter: str) -> int:
    return text_box.index(letter)

def find_index_for_de(letter: str) -> int:
    return emo_box.index(letter)

def split_into_chunk(text: str) -> list:
    chunks = []
    for i in range(0, len(text), 3):
        chunk = text[i:i+3]
        chunks.append(chunk)
    return chunks

def encode(text: str) -> str:
    res = ""
    for c in text:
        res += emo_box[find_index_for_en(c)]
    return res

def decode(text: str) -> str:
    res = ""
    for c in split_into_chunk(text):
        res += text_box[find_index_for_de(c)]
    return res

# README.md 内容
readme_content = """
# Cyfer Joke README

This is a simple Python script for encoding and decoding text using a "Cyfer Joke" encryption scheme.

## Author
- **Author:** ablajan
- **Mail:** 2770532197@qq.com
- **Time:** 2024.3.20

## Description
This script encodes text into "Cyfer Joke" emojis and decodes "Cyfer Joke" emojis back into text.

## Usage
To encode text, use the `encode(text)` function.
To decode "Cyfer Joke" emojis, use the `decode(text)` function.

## Example
```python
# Encode text
encoded_text = encode("hello")
print(encoded_text)  # Output: "*_*@@n_N@@q_q@@q_q@@v_V"

# Decode "Cyfer Joke" emojis
decoded_text = decode("*_*@@n_N@@q_q@@q_q@@v_V")
print(decoded_text)  # Output: "hello"
