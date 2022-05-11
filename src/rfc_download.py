import rfc_track
import requests
import re
import file

URL = "https://www.rfc-editor.org/rfc/pdfrfc/rfc"
EXTENSION = ".txt.pdf"


def download(number, filepath):
    title = rfc_track.get_title(number)
    pdf_filename = f"{str(number).rjust(4, '0')}_{_transform_title(title)}.pdf"

    url = f"{URL}{number}{EXTENSION}"
    r = requests.get(url, stream=True)

    if r.status_code != 200:
        print(f"Error downloading file: status {r.status_code}")
        return

    file.write_binary(filepath, pdf_filename, r.content)

    print(f"File downloaded as {pdf_filename}")

def _transform_title(title):
    title = re.sub(": ", "_", title)
    title = re.sub(" ", "-", title)
    title = re.sub("[^a-zA-Z\d\-_]", "", title)

    return title.lower()
