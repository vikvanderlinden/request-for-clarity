import json

already_printed = set()
global print_list

def get_title(number):
    rfc_map = None

    with open("data/map.json", 'r') as mapfile:
        rfc_map = json.loads(mapfile.read())

    if rfc_map is None:
        return False

    rfc = rfc_map.get(str(number), False)
    if not rfc:
        return False

    return rfc["title"]

def follow(nb, max_depth=None):
    global print_list
    already_printed.clear()
    print_list = []

    _search_map(True, nb, max_depth=max_depth)

    to_print = print_list[1:][::-1]

    already_printed.clear()
    print_list = []

    _search_map(False, nb, max_depth=max_depth)

    to_print.extend(print_list)

    for line in to_print:
        print(line)

def _search_map(mode, number, depth=0, type=">", max_depth=None):
    global print_list

    if max_depth is not None and depth > max_depth:
        return

    rfc_map = None

    with open("data/map.json", 'r') as mapfile:
        rfc_map = json.loads(mapfile.read())

    rfc = rfc_map.get(str(number), False)
    if rfc:
        _print_rfc(mode, rfc, depth, type, max_depth)
    else:
        print_list.append(" RFC not found")


def _print_rfc(mode, rfc, depth=0, type=">", max_depth=None):
    global print_list

    depth_plus_one = depth + 1

    if _get_num(rfc["rfc_number"]) in already_printed:
        print_list.append("| "*depth + f"{type} [P] {rfc['rfc_number']} - {rfc['title']}")
        return

    print_list.append("| "*depth + f"{type} {rfc['rfc_number']} - {rfc['title']}")
    already_printed.add(_get_num(rfc["rfc_number"]))

    if mode:
        if len(rfc["obsoletes"]) > 0:
            for o in rfc["obsoletes"]:
                _search_map(mode, _get_num(o), depth_plus_one, "-", max_depth)

        if len(rfc["updates"]) > 0:
            for o in rfc["updates"]:
                _search_map(mode, _get_num(o), depth_plus_one, "+", max_depth)
    else:
        if len(rfc["obsoleted_by"]) > 0:
            for o in rfc["obsoleted_by"]:
                _search_map(mode, _get_num(o), depth_plus_one, "-", max_depth)

        if len(rfc["updated_by"]) > 0:
            for o in rfc["updated_by"]:
                _search_map(mode, _get_num(o), depth_plus_one, "+", max_depth)

def _get_num(number_string):
    return int(number_string[3:])
