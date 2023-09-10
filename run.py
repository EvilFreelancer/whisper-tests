import os
import aiohttp
import aiofiles
import asyncio
import time
import eyed3

PORT = 9001


def get_duration(filepath):
    """Returns the duration of the mp3 file in seconds."""
    audiofile = eyed3.load(filepath)
    return audiofile.info.time_secs


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
    duration = get_duration(filepath)
    print(f"Processed {filepath} (Duration: {duration:.2f} seconds) in {elapsed_time:.2f} seconds")
    async with aiofiles.open(save_to, 'w') as f:
        await f.write(txt)


async def processing():
    files = [os.path.join("./audios", f"{i}.mp3") for i in range(1, 11)]
    for file in files:
        await post(file)


asyncio.run(processing())
