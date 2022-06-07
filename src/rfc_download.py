import rfc_track
import requests
import re
import file

HOST = "https://www.rfc-editor.org/"
OLD_PATH = "rfc/pdfrfc/rfc"
NEW_PATH = "rfc/rfc"
OLD_EXTENSION = ".txt.pdf"
NEW_EXTENSION = ".pdf"


def download(number, filepath):
    title = rfc_track.get_title(number)
    pdf_filename = f"{str(number).rjust(4, '0')}_{_transform_title(title)}.pdf"

    old_url = f"{HOST}{OLD_PATH}{number}{OLD_EXTENSION}"
    new_url = f"{HOST}{NEW_PATH}{number}{NEW_EXTENSION}"

    if number >= 8650: # This is the first RFC using the new url
        url = new_url
    else:
        url = old_url

    print(f"Downloading from: {url}")
    r = requests.get(url, stream=True)

    if r.status_code != 200:
        print(f"Error downloading file: status {r.status_code}")
        return

    file.write_binary(filepath, pdf_filename, r.content)

    print(f"File downloaded as {pdf_filename}")

def _transform_title(title):
    title = re.sub(": ", "_", title)
    title = re.sub(" ", "-", title)
    title = re.sub("\/", "-", title)
    title = re.sub("[\-]+", "-", title)
    title = re.sub("[^a-zA-Z\d\-_\.]", "", title)

    return title.lower()
