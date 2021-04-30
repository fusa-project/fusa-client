from client import FusaClient

client = FusaClient(fusa_server="http://localhost:8000")

file_path = "/home/victor/Desktop/FUSA/ARQUITECTURA/fast_api/audio_1.wav"
latitude = 70.0
longitude = 120.0
recorded_at = 1619795993

client.add_audio(file_path, latitude, longitude, recorded_at)