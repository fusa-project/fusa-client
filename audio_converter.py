import os
from dataclasses import dataclass
import base64

from mutagen.mp3 import MP3

@dataclass
class AudioInfo:
    duration: float
    size: float
    filename: str
    format_name: str
    file_path: str

class AudioFile():    
    duration = None
    size = None
    file_name = None
    format_name = None
    file_path = None

    def __init__(self, file_path: str):
        #TODO: check that files exists
        self.file_path = file_path
    
    def _get_audio_name_and_format(self, file_path:str):
        splited_path = file_path.split("/")
        file_name = splited_path[-1]
        format_name = file_name.split(".")[-1]
        allowed_files_format = ["mp3"]
        if format_name not in allowed_files_format:
            raise RuntimeError(f"Format {format_name} not allowed!, allowed values are: {allowed_files_format}")
        return file_name, format_name

    def _process_mp3_file(self, file_path:str):
        audio = MP3(file_path)
        self.duration = audio.info.length
        self.size = os.stat(file_path).st_size

    def process_audio(self):
        file_name, format_name = self._get_audio_name_and_format(self.file_path)
        if format_name == "mp3":
            self._process_mp3_file(self.file_path)
        return self

    def get_audio_info(self) -> AudioInfo:
        return AudioInfo(
            duration=self.duration,
            size=self.size,
            filename=self.file_name,
            format_name=self.format_name,
            file_path=self.file_path
        )

    def convert_audio_to_bytes_str(self) -> str:
        byte_content = open(self.file_path, "rb").read()
        base64_bytes = base64.b64encode(byte_content)
        base64_string = base64_bytes.decode("utf-8")
        return base64_string

if __name__ == "__main__":
    audio_data = AudioFile("/Users/maravenag/Desktop/fusa-client/sample.mp3").process_audio()
    info = audio_data.get_audio_info()
    audio_str = audio_data.convert_audio_to_bytes_str()