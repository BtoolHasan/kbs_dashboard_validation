class TableHandler:
    """
    Handles TABLE sheets.

    Expected format:
        Column headers in first row
        Data rows below

    Example:
        branch | value
        North  | 3000
        South  | 2000   
    """

    def process(self, sheet_data, sheet_info):
        print(f"\n[TABLE] Processing: {sheet_info.metric_name}")

        rows = self._extract_rows(sheet_data)

        return {
            "metric_name": sheet_info.metric_name,
            "rows": rows
        }

    def _extract_rows(self, sheet_data):
        """
        Skip header row and extract structured rows.
        """

        structured_data = []

        # skip first row (header)
        data_rows = sheet_data[1:]

        for row in data_rows:

            if not row or len(row) < 2:
                continue

            key = str(row[0]).strip()
            value = row[1]

            if key == "" or value is None:
                continue

            structured_data.append({
                "key": key,
                "value": value
            })

        return structured_data