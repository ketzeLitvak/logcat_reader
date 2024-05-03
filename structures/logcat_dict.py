from structures.message import Message
from utils.dates import timestamp_to_str
from typing import List
from pathlib import Path
import json


class LogcatDict:
    _logcat_messages_property = "logcatMessages"
    logcat_messages: List[Message] = []

    def __init__(self, path: Path):
        file = open(path, "r")
        logcat_json = json.loads(file.read())
        logcat_message_list = logcat_json[self._logcat_messages_property]
        for logcat_message in logcat_message_list:
            message = Message(logcat_message)
            self.logcat_messages.append(message)

    def print_lines(self, path: Path) -> str:
        new_name = f"{path.stem}-formatted.txt"
        file = open(f"{path.parents[0]}/{new_name}", "w", 1)
        splitted_message = ""
        start_date = None
        last_message = None
        for logcat_message in self.logcat_messages:
            if logcat_message.is_splitted():
                splitted_message += logcat_message.get_without_split_char()
                if start_date is None:
                    start_date = logcat_message.timestamp
                last_message = logcat_message
            else:
                if splitted_message != "":
                    start_date_timestamp = timestamp_to_str(start_date)
                    end_date_timestamp = timestamp_to_str(last_message.timestamp)
                    file.write(f"{last_message.log_level} - {start_date_timestamp} to {end_date_timestamp}: {splitted_message}\n")
                    splitted_message = ""
                    start_date = None
                file.write(f"{logcat_message.to_line()}\n")
        return new_name
