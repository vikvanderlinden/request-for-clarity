import re
import file
import requests

RFC_INDEX_URL = "https://www.rfc-editor.org/rfc-index.txt"

def fetch_index():
    r = requests.get(RFC_INDEX_URL, stream=True)

    if r.status_code != 200:
        print(f"Downloading RFC index failed with status: {r.status_code}")
        return False

    file.write_binary("../data/", "rfc-index.txt", r.content)

    return True

def create():
    content = file.read("../data/rfc-index.txt")

    list_start = content.find("\n\n\n")

    content = content[list_start + 4:]
    raw_rfc_list = content.split("\n\n")

    processed_rfcs = {}

    for rfc in raw_rfc_list:
        rfc = re.sub("[ ]+", " ", rfc.replace("\n", ""))

        if "Not Issued" in rfc:
            continue

        number     = int(rfc.split(" ")[0])
        rfc_number = f"RFC{number}"
        title      = " ".join(rfc.split(". ")[0].split(" ")[1:])

        obsoletes    = re.findall("\(Obsoletes ([RFC\d+ ?,?]+)\)", rfc)
        obsoleted_by = re.findall("\(Obsoleted by ([RFC\d+ ?,?]+)\)", rfc)
        updates      = re.findall("\(Updates ([RFC\d+ ?,?]+)\)", rfc)
        updated_by   = re.findall("\(Updated by ([RFC\d+ ?,?]+)\)", rfc)

        processed_rfcs[number] = {
            "rfc_number": rfc_number,
            "title": title,
            "obsoletes": obsoletes[0].split(", ") if obsoletes else [],
            "obsoleted_by": obsoleted_by[0].split(", ") if obsoleted_by else [],
            "updates": updates[0].split(", ") if updates else [],
            "updated_by": updated_by[0].split(", ") if updated_by else [],
        }

    file.write_json("../data/map.json", processed_rfcs)
