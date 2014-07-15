import os

from datetime import datetime as dt


class MalformedLogEntry(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __repr__(self):
        return self._msg


class LogEntry(object):
    """A class for log entries."""

    INFO = 0
    WARNING = 1
    ERROR = 2

    def __init__(self, kind, date, msg):
        self._kind = kind
        self._date = date
        self._msg = msg

    @staticmethod
    def parse(line):
        """Returns a log entry from a log line."""

        components = line.split(' ', maxsplit=2)
        entry_date = dt.strptime(components[1], '%Y-%m-%d')
        kind = get_entry_kind(components[0])
        if kind is None:
            raise MalformedLogEntry('unknown log entry kind {0}. only use {1}'.format(components[0], 'INFO, WARNING or ERROR'))
        return LogEntry(kind, entry_date, components[2])

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
    def from_file(path, skip_malformed_entries=False):
        entries = []
        with open(path, 'r') as input_file:
            for line in input_file:
                try:
                    entries.append(LogEntry.parse(line))
                except MalformedLogEntry as ex:
                    if not skip_malformed_entries:
                        raise ex
            return Log(entries)

    def get_errors(self):
        sorted_entries = sorted(self._entries, key=lambda entry: entry.date, reverse=True)
        return [entry for entry in sorted_entries if entry.kind == LogEntry.ERROR]


ENTRY_KINDS = { 'INFO': LogEntry.INFO,
                'WARNING': LogEntry.WARNING,
                'ERROR': LogEntry.ERROR }


def get_entry_kind(kind):
    """Returns the tag for a given entry."""
    return ENTRY_KINDS.get(kind)


def get_entry_kind_name(kind):
    """Returns the tag for a given entry."""

    for k, v in ENTRY_KINDS.items():
        if kind == v:
            return k


def log(log_file, kind, msg_fmt, *args):
    now = dt.now()
    log_line = '{0} {1} {2}\n'
    line = log_line.format(get_entry_kind_name(kind),
                           now.strftime('%Y-%m-%d'),
                           msg_fmt.format(*args))
    log_file.write(line)
