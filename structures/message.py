from datetime import datetime
from utils.dates import timestamp_to_str


class Message:
    _message_property = "message"
    _log_level_property = "logLevel"
    _header_property = "header"
    _timestamp_property = "timestamp"
    _timestamp_seconds_property = "seconds"
    _left_arrow = " ---> "
    _right_arrow = " <--- "

    def __init__(self, message_dict):
        self.message: str = message_dict[self._message_property]
        self.log_level: str = message_dict[self._header_property][self._log_level_property]
        timestamp = message_dict[self._header_property][self._timestamp_property][self._timestamp_seconds_property]
        self.timestamp: datetime = datetime.fromtimestamp(timestamp)

    def is_splitted(self) -> bool:
        return self.message.endswith(self._left_arrow) or self.message.startswith(self._right_arrow)

    def get_without_split_char(self):
        return self.message.replace(self._left_arrow, "").replace(self._right_arrow, "")

    def to_line(self):
        formatted_timestamp = timestamp_to_str(self.timestamp)
        return f"{self.log_level} - {formatted_timestamp}: {self.message}"

