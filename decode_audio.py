import base64
import json
import os


def main() -> None:
    

    with open("Site/data/main/main.json", encoding='utf-8') as f:
        audio_js = json.load(f)
        for k in audio_js:
            target_path = os.path.join("decoded_data/main", k)
            decode_audio(audio_js[k], target_path)

    with open("Site/data/track/track.json", encoding="utf-8") as f:
        audio_js = json.load(f)
        for k in audio_js:
            target_path = os.path.join("decoded_data/track", k)
            decode_audio(audio_js[k], target_path)
        


def decode_audio(data : str, target_path : str) -> None:
    base_64_data = data.split(",")[1]
    
    decode_data = base64.b64decode(base_64_data)
    with open(target_path, "wb+") as f:
        f.write(decode_data)

    return


if __name__ == "__main__":
    main()