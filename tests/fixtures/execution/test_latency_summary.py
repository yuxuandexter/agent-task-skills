import unittest

from latency_summary import mean_completed_latency


class LatencySummaryTests(unittest.TestCase):
    def test_completed_samples(self):
        self.assertEqual(
            mean_completed_latency(
                [
                    {"status": "ok", "duration_ms": 10},
                    {"status": "ok", "duration_ms": 20},
                ]
            ),
            15,
        )

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            mean_completed_latency([])


if __name__ == "__main__":
    unittest.main()
