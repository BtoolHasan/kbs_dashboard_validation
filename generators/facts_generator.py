from facts.facts import MetricFact, TableRowFact


class FactGenerator:
    """
    Converts ExcelProcessor output into Experta Facts.

    This is the bridge between:
        Structured Data  →  Knowledge Facts
    """

    def generate(self, processed_data: dict):
        facts = []

        for metric_name, result in processed_data.items():

            # Case 1: Metric (DATA_LABEL)
            if "value" in result:
                fact = MetricFact(
                    name=result.get("metric_name", metric_name),
                    value=result["value"]
                )
                facts.append(fact)

            # Case 2: Table (TABLE)
            elif "rows" in result:
                table_name = result.get("metric_name", metric_name)

                for row in result["rows"]:

                    fact = TableRowFact(
                        name=table_name,
                        row_data=row
                    )
                    facts.append(fact)

        return facts