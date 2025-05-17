def extract_keys(*dicts):
    result = []

    def recurse(d):
        for key, value in d.items():
            result.append(key)
            if "children" in value:
                recurse(value["children"])

    for d in dicts:
        recurse(d)

    return result
