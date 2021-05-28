import requests

from data_models import Audio
from audio_converter import AudioFile, AudioInfo

class FusaClient():
    def __init__(self, fusa_server:str):
        self.fusa_server = fusa_server
        self._check_server_connection()
    
    def _check_server_connection(self) -> bool:
        endpoint = "health"
        uri = f"{self.fusa_server}/{endpoint}"
        request = requests.get(uri)
        if request.status_code == 200:
            return True
        else:
            raise RuntimeError(f"Could not get connection to FUSA server at: \
                                {self.fusa_server}, status code: {request.status_code}")

    def add_audio(self, file_path:str,
                        latitude:float,
                        longitude:float,
                        recorded_at: int,
                        id_: int):
        audio_file = AudioFile(file_path).process_audio()
        audio_info = audio_file.get_audio_info()

        encoded_audio = audio_file.convert_audio_to_bytes_str()
        
        #TODO cachar de donde sacar el id
        body_data = Audio(
            id=id_,
            filename=audio_info.filename,
            file_path=audio_info.file_path,
            duration=audio_info.duration,
            size=audio_info.size,
            data=encoded_audio,
            latitude=latitude,
            longitude=longitude,
            recorded_at=recorded_at,
        )

        endpoint = "add_audio"
        uri = f"{self.fusa_server}/{endpoint}"
        request = requests.post(uri, data=body_data.json())
        #TODO: hacer clase logger generica
        print(request.content)
        if request.status_code != 200:
            print(request.content)
            raise RuntimeError(f"Could not get connection to FUSA server at: \
                                {self.fusa_server}, status code: {request.status_code}")