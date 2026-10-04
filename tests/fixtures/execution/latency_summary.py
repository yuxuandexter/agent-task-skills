"""Small intentionally incomplete implementation for an isolated behavior probe."""


def mean_completed_latency(rows):
    """Return the mean duration of rows whose status is 'ok'.

    Raise ValueError when no completed rows exist. Every 'ok' row has a
    numeric duration_ms. Other row statuses may have missing durations.
    """
    if not rows:
        raise ValueError("No completed samples")
    return sum(row.get("duration_ms", 0) for row in rows) / len(rows)
