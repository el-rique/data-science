import unittest

import pandas as pd

from mental_health_analysis.country import country_treatment_rates


class CountryTreatmentRatesTests(unittest.TestCase):
    def test_rates_include_counts_and_exclude_missing_responses(self) -> None:
        data = pd.DataFrame(
            {
                "Country": ["A", "A", "A", "B", "B"],
                "treatment": ["Yes", "Yes", "No", "No", None],
            }
        )

        result = country_treatment_rates(data)

        self.assertEqual(result.loc["A", "Yes"], 2)
        self.assertEqual(result.loc["A", "No"], 1)
        self.assertEqual(result.loc["A", "total"], 3)
        self.assertAlmostEqual(result.loc["A", "treatment_rate_percent"], 200 / 3)
        self.assertEqual(result.loc["B", "total"], 1)
        self.assertEqual(result.loc["B", "treatment_rate_percent"], 0)

    def test_unexpected_treatment_response_is_reported(self) -> None:
        data = pd.DataFrame({"Country": ["A"], "treatment": ["Unknown"]})

        with self.assertRaisesRegex(ValueError, "Unexpected treatment responses"):
            country_treatment_rates(data)


if __name__ == "__main__":
    unittest.main()
