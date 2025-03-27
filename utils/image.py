from PIL import Image
from pathlib import Path


def resize(file_name: str):
    file_path = Path(file_name)
    image = Image.open(file_path)

    image_resized_1000_500 = image.resize((1000, 500))
    image_resized_200_100 = image.resize((200, 100))
    
    image_resized_1000_500.save(f"temp/{file_path.name}_1000_500.{file_path.suffix}")
    image_resized_200_100.save(f"temp/{file_path.name}_200_100.{file_path.suffix}")



if __name__ == "__main__":
    ...