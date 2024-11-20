import requests
import os

# URL van de Cataas API voor een willekeurige kattenfoto
url = "https://cataas.com/cat"

def save_image():
    try:
        # Verzoek versturen om de afbeelding te downloaden
        response = requests.get(url)

        # Controleren of het verzoek succesvol was
        if response.status_code == 200:
            # Content-Type header ophalen om het bestandstype te bepalen
            content_type = response.headers.get('Content-Type', '')
            if 'image/' in content_type:
                # Bestandstype (bijv. jpg, png) extraheren
                file_extension = content_type.split('/')[1]

                # Bestand opslaan met de juiste extensie
                output_file = f"cat_photo.{file_extension}"
                with open(output_file, "wb") as file:
                    file.write(response.content)
                return output_file
                print(f"Kattenfoto succesvol opgeslagen als {output_file}")
            else:
                print("De API retourneerde geen afbeelding.")
        else:
            print(f"Fout bij het ophalen van de afbeelding. Statuscode: {response.status_code}")
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")
