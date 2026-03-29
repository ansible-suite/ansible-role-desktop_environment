def prune_nulls(data):
    """
    Recursively remove keys with None values from nested dictionaries.
    Works on dicts, lists of dicts, and mixed structures.
    """
    if isinstance(data, dict):
        return {
            k: prune_nulls(v)
            for k, v in data.items()
            if v is not None and prune_nulls(v) != {}
        }
    elif isinstance(data, list):
        return [prune_nulls(v) for v in data]
    else:
        return data


class FilterModule(object):
    def filters(self):
        return {
            "prune_nulls": prune_nulls,
        }
