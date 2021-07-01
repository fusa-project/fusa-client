from client import FusaClient
import os

client = FusaClient(fusa_server="http://localhost:8000") #http://localhost:8000") http://45.79.170.31:8000"

file_path = "/home/victor/Desktop/FUSA/ARQUITECTURA/fast_api/audio_samples/street_traffic-helsinki-164-5042-a.wav"
if os.path.exists(file_path):
    latitude = -39.88422 
    longitude = -73.29589
    recorded_at = 1622736261
    uploaded_at = 1622736269
    has_parent = True
    user_category = "citizen"   #"sensor"
    username = "username"
    source_tags = ["dog", "cat", "car"]
    parent_id = "1"
    parent_chunk = [1, 9]

    client.add_audio(
        file_path, recorded_at, uploaded_at, latitude, longitude,
        has_parent,user_category, username, source_tags, parent_id, parent_chunk)
    print("Archivo de audio enviado con éxito")
else:
    print("Archivo de audio no existe")