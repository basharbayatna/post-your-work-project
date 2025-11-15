"""
Simple Bikeshare helper script.

This file is intentionally straightforward so you can make changes
on the ``refactor`` branch during the project.

Provides a small CSV loader and a few helper functions for exploring
basic counts. The CSV file `new_york_city.csv` is intentionally small
and excluded from version control via `.gitignore`.
"""

import csv
from collections import Counter
from typing import List, Dict, Any


def load_csv(path: str) -> List[Dict[str, Any]]:
    """Load a CSV file into a list of dictionaries.

    If the file is missing, returns an empty list and prints a message.
    """
    try:
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    except FileNotFoundError:
        print(f"Warning: file not found: {path}")
        return []


def most_common(values: List[str], n: int = 5) -> List[tuple]:
    """Return the n most common values from a list."""
    c = Counter(values)
    return c.most_common(n)


def summarize_trips(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Return a minimal summary from bikeshare data.

    Expects fields such as 'Start Station', 'End Station', 'User Type',
    'Gender', and 'Birth Year' when present in the CSV file.
    """
    summary = {
        'total_rows': len(data),
        'common_start_stations': [],
        'common_end_stations': [],
        'user_types': []
    }
    if not data:
        return summary

    start_stations = [row.get('Start Station', '') for row in data]
    end_stations = [row.get('End Station', '') for row in data]
    user_types = [row.get('User Type', '') for row in data]

    summary['common_start_stations'] = most_common(start_stations, 5)
    summary['common_end_stations'] = most_common(end_stations, 5)
    summary['user_types'] = most_common(user_types, 5)

    return summary


if __name__ == '__main__':
    # Simple CLI to demonstrate the code. This is safe to run even without the CSV file.
    data = load_csv('new_york_city.csv')
    s = summarize_trips(data)
    print(f"Loaded rows: {s['total_rows']}")
    if s['common_start_stations']:
        print('Top start stations:', s['common_start_stations'])
    else:
        print('No station data available.')
