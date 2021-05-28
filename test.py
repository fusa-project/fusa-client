from client import FusaClient

def main():
    file_path = "/Users/maravenag/Desktop/fusa-client/sample.mp3"
    client = FusaClient(fusa_server="http://45.79.170.31:8000")
    client.add_audio(file_path=file_path, latitude=-30.0, longitude=-30.0, recorded_at=-1, id_=-6)
    
if __name__ == "__main__":
    main()