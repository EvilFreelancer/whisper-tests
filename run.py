import os
import aiohttp
import aiofiles
import asyncio
import time

PORT = 9002


async def post(filepath):
    save_to = os.path.splitext(filepath)[0] + F"_{PORT}.txt"
    if os.path.exists(save_to):
        print(f"{save_to} exists, skip")
        return
    async with aiofiles.open(filepath, 'rb') as f:
        file = await f.read()
    form = aiohttp.FormData()
    form.add_field("audio_file", file, filename=filepath)
    url = F"http://127.0.0.1:{PORT}/asr?task=transcribe&output=txt"
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=form) as response:
            txt = await response.text()
    elapsed_time = time.time() - start_time
    print(f"Processed {filepath} in {elapsed_time:.2f} seconds")
    async with aiofiles.open(save_to, 'w') as f:
        await f.write(txt)


def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]


def similarity_coefficient(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        text1 = f1.read()
        text2 = f2.read()
    distance = levenshtein_distance(text1, text2)
    max_length = max(len(text1), len(text2))
    similarity = 1 - distance / max_length
    return similarity


async def processing():
    files = [os.path.join("./audios", f"{i}.mp3") for i in range(1, 11)]
    for file in files:
        await post(file)
        if PORT != 9001:
            base_file = os.path.splitext(file)[0] + "_9001.txt"
            current_file = os.path.splitext(file)[0] + F"_{PORT}.txt"
            sim_coeff = similarity_coefficient(base_file, current_file)
            print(f"The similarity coefficient between {base_file} and {current_file} is {sim_coeff:.2f}")


asyncio.run(processing())
