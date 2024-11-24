import requests
import os

url = "https://cataas.com/cat"

def save_image():
    try:
        response = requests.get(url)

        if response.status_code == 200:
            content_type = response.headers.get('Content-Type', '')
            if 'image/' in content_type:
                file_extension = content_type.split('/')[1]

                output_file = f"cat_photo.{file_extension}"
                with open(output_file, "wb") as file:
                    file.write(response.content)
                return output_file
                print(f"saved picture succesfully as: {output_file}")
            else:
                print("the api didn't respond")
        else:
            print(f"error {response.status_code}")
    except Exception as e:
        print(f"an error has occured: {e}")
