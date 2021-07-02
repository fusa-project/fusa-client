import requests

from data_models import AudioSchema, UserSchema, TagSchema, ParentSchema
from audio_converter import AudioFile

class FusaClient():
    def __init__(self, fusa_server:str, api_key:str=None):
        if api_key == None:
            raise ValueError("No api_key provided!")
        self.api_key = api_key
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
                        recorded_at: int,
                        uploaded_at: int,
                        latitude: float,
                        longitude: float,
                        has_parent: bool,
                        user_category: str,
                        username: str,
                        tags: list,
                        parent_id: str,
                        parent_chunk: list):
        audio_file = AudioFile(file_path).process_audio()
        audio_info = audio_file.get_audio_info()
        encoded_audio = audio_file.convert_audio_to_bytes_str()

        user=UserSchema(
            category=user_category,
            username=username
        )
        tags=[TagSchema(
            username=username,
            source_tags=tags
        )]
        parent=ParentSchema(
            parent_id=parent_id,
            parent_chunk=parent_chunk
        )

        body_data = AudioSchema(
            name=audio_info.filename,
            format=audio_info.format_name,
            duration=audio_info.duration,
            size=audio_info.size,
            recorded_at=recorded_at,
            uploaded_at=uploaded_at,
            latitude=latitude,
            longitude=longitude,
            data=encoded_audio,
            has_parent=has_parent,
            user=user,
            tags=tags,
            parent=parent,
        )
        endpoint = "audios"
        uri = f"{self.fusa_server}/{endpoint}"
        headers = { "X-Api-Key": self.api_key }
        request = requests.post(uri, data=body_data.json(), headers=headers)
        if request.status_code != 200:
            raise RuntimeError(f"Could not get connection to FUSA server at: \
                                {self.fusa_server}, status code: {request.status_code}")
        else request.status_code == 200:
            return True