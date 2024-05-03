timestamp_format = "%Y/%m/%d-%I:%M:%S"


def timestamp_to_str(timestamp):
    return timestamp.strftime(timestamp_format)
