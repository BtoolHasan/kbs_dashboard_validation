class DataLabelHandler:
    """
    Handles DATA_LABEL sheets with format:

        Label        Value
        TotalSales   10000
    """

    def process(self, sheet_data, sheet_info):
        print(f"\n[DATA_LABEL] Processing: {sheet_info.metric_name}")

        value = self._extract_single_value(sheet_data)

        return {
            "metric_name": sheet_info.metric_name,
            "value": value
        }

    def _extract_single_value(self, sheet_data):
        """
        Extract value from second column of first valid data row.
        """

        for row in sheet_data:

            if not row or len(row) < 2:
                continue

            label = row[0]
            value = row[1]

            # skip header row safely
            if str(label).strip().lower() in ["label", "kpi", "metric"]:
                continue

            if value is not None and str(value).strip() != "":
                return value

        raise ValueError("No valid KPI value found in DATA_LABEL sheet.")