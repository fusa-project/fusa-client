from client import FusaClient
import os
import random
import time

client = FusaClient(fusa_server="http://45.79.170.31:8000", api_key="RXXceb89Vv30H3FhGaCg") #http://localhost:8000") http://45.79.170.31:8000"
tag_options = ["dog", "bird", "car", "truck", "motor", "bus", "alarm", "bus"]
files_folder = "/home/victor/Desktop/FUSA/ARQUITECTURA/fast_api/audio_samples/"

for wav_file in os.listdir(files_folder):
    try:
        file_path = files_folder + wav_file
        latitude = -39.88400 + random.uniform(-0.00099, 0.00099)
        longitude = -73.29500 + random.uniform(-0.00099, 0.00099)
        recorded_at = int(time.time())
        uploaded_at = int(time.time()) + random.randint(10, 90)
        has_parent = True
        user_category = random.choice(["citizen", "sensor"])
        username = "username_" + str(random.randint(1, 99))
        source_tags = random.sample(tag_options, random.randint(1, 5))
        parent_id = random.randint(1, 99)
        parent_chunk = [1, random.randint(2, 99)]

        client.add_audio(
            file_path, recorded_at, uploaded_at, latitude, longitude,
            has_parent,user_category, username, source_tags, parent_id, parent_chunk)
        print("Archivo de audio enviado con éxito")
    except Exception as e:
        print(e)
        print("Se ha producido en error en la subida de archivos")