from PIL import Image
from pathlib import Path
from config import cache


def resize(file_name: str):
    file_path = Path(file_name)
    image = Image.open(file_path)

    image_resized_1000_500 = image.resize((1000, 500))
    image_resized_200_100 = image.resize((200, 100))

    image_resized_1000_500.save(f"temp/{file_path.name}_1000_500.{file_path.suffix}")
    image_resized_200_100.save(f"temp/{file_path.name}_200_100.{file_path.suffix}")


def image_subscribe():
    image_channel = cache.pubsub()
    image_channel.subscribe("images")
    print("Подписан на канал images")
    for message in image_channel.listen():
        if message['type'] == "message":
            resize(message['data'].decode())
            print(f"{message['data']} resized")



if __name__ == "__main__":
    image_subscribe()