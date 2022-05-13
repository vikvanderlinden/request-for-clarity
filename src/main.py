import rfc_map
import rfc_track
import rfc_download


def run():
    print("Initializing...")
    rfc_map.fetch_index()
    print("  Index fetched")
    rfc_map.create()
    print("  Map created")
    print("Ready!")
    print("")
    print("Usage:")
    print("  <number>[:<maxdepth>]  - Search for this RFC")
    print("  +<number>              - Download this RFC as PDF (if available)")
    print("  *<number>[:<maxdepth>] - Both of the above")
    print("  <others>               - End the program (empty, text or invalid character)")
    print("")

    while True:
        download = False
        combine = False
        max_depth = None

        nb = input("RFC to search: ")

        if ':' in nb:
            nb, max_depth = nb.split(':')
            if max_depth == "" or not max_depth.isdigit():
                max_depth = None
            else:
                max_depth = int(max_depth)

        if len(nb) > 0 and nb[0] == '+':
            download = True
            nb = nb[1:]
        if len(nb) > 0 and nb[0] == '*':
            combine = True
            nb = nb[1:]

        if nb == "" or not nb.isdigit() or int(nb) == 0:
            break

        if not download or combine:
            print("")
            rfc_track.follow(int(nb), max_depth)
        if download or combine:
            print("")
            rfc_download.download(int(nb), "../data/papers/rfc/")
        print("")


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\n\n>> Bye\n")
