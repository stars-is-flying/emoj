# only for lower letter, it is just a cyfer joke, dont use it for official place!


# author:ablajan
# mail:2770532197@qq.com
# time:2024.3.20

text_box = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

emo_box = [
    "*_*", "^_^", "-_-", "#_#", "+_+", "@_@", "q_q", "$_$", "o_O", "O_o", "6_6", ")_(", "._.", ":_:", "'_'", "k_k", "?_?", "!_!", "<_>", ">_<", "n_N", "N_n", "e_e", "V_v", "v_V", ",_,"
]

def find_index_for_en(letter: str)->int:
    return text_box.index(letter)

def find_index_for_de(letter: str)->int:
    return emo_box.index(letter)

def split_into_chuk(text: str)->list:
    chunks = []
    for i in range(0, len(text), 3):
        chunk = text[i:i+3]
        chunks.append(chunk)
    
    return chunks

def encode(text: str)->str:
    res = ""
    for c in text:
        res += emo_box[find_index_for_en(c)]
    return res

def decode(text: str)->str:
    res = ""
    for c in split_into_chuk(text):
        res += text_box[find_index_for_de(c)]
    return res