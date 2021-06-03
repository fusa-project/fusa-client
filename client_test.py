from client import FusaClient

client = FusaClient(fusa_server="http://45.79.170.31:8000") #http://localhost:8000")

file_path = "/home/victor/Desktop/FUSA/ARQUITECTURA/fast_api/audio_samples/audio_2.wav"
id = 1
latitude = -39.81422 
longitude = -73.24589
recorded_at = 1619795993

client.add_audio(id, file_path, latitude, longitude, recorded_at)