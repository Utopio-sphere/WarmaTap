import base64
import json
import os

MAIN_PATH = "decoded_data/main"
TRACK_PATH = "decoded_data/track"

JSON_DATA_PREFIX = "data:audio/mp3;base64,"

MAIN_TARGET = "Site/data/main/main.json"
TRACK_TARGET = "Site/data/track/track.json"

def main() -> None:
    json_main = {}
    json_track = {}

    for key in os.listdir(MAIN_PATH):
        with open(os.path.join(MAIN_PATH, key), "rb") as f:
            raw = f.read()
            encoded_str = base64.b64encode(raw).decode()
            encoded_str = JSON_DATA_PREFIX + encoded_str
        
        json_main[key] = encoded_str
    

    for key in os.listdir(TRACK_PATH):
        with open(os.path.join(TRACK_PATH, key), "rb") as f:
            raw = f.read()
            encoded_str = base64.b64encode(raw).decode()
            encoded_str = JSON_DATA_PREFIX + encoded_str
        
        json_track[key] = encoded_str

    
    write_to_file(json_main, MAIN_TARGET)
    write_to_file(json_track, TRACK_TARGET)
    




def write_to_file(data : dict, target_file_path : str) -> None:
    with open(target_file_path, "w+", encoding="utf-8") as f:
        f.write("\n")
        f.write("{\n")
        for i, k in enumerate(data):
            if i == len(data) - 1:
                f.write(f'"{k}":"{data[k]}"\n')
            else:
                f.write(f'"{k}":"{data[k]}",\n')
        f.write("}\n")


if __name__ == "__main__":
    main()