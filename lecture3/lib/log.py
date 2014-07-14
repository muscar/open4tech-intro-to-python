import os

from datetime import datetime as dt


class LogEntry(object):
    """A class for log entries."""

    ENTRY_INFO = 0
    ENTRY_WARNING = 1
    ENTRY_ERROR = 2

    def __init__(self, kind, date, msg):
        self._kind = kind
        self._date = date
        self._msg = msg

    @staticmethod
    def parse(line):
        """Returns a log entry from a log line."""

        components = line.split(' ', maxsplit=2)
        entry_date = dt.strptime(components[1], '%Y-%m-%d')
        return LogEntry(get_entry_kind(components[0]), entry_date, components[2])

    @property
    def date(self):
        return self._date

    @property
    def kind(self):
        return self._kind


class Log(object):
    def __init__(self, entries):
        self._entries = entries

    @staticmethod
    def from_file(path):
        if not os.path.isfile(path):
            return
        entries = []
        with open(path, 'r') as input_file:
            for line in input_file:
                entries.append(LogEntry.parse(line))
            return Log(entries)

    def get_errors(self):
        sorted_entries = sorted(self.entries, key=lambda entry: entry.date, reverse=True)
        return [entry for entry in sorted_entries if entry.kind == LogEntry.ENTRY_ERROR]



def get_entry_kind(entry):
    """Returns the tag for a given entry."""

    if entry.startswith('INFO'):
        return LogEntry.ENTRY_INFO
    if entry.startswith('WARNING'):
        return LogEntry.ENTRY_WARNING
    if entry.startswith('ERROR'):
        return LogEntry.ENTRY_ERROR
