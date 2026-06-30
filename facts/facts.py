from experta import Fact


class MetricFact(Fact):
    """
    Generic KPI / metric fact.

    Example:
        name = "TotalSales"
        value = 15000
    """
    pass


class TableRowFact(Fact):
    """
    Generic table row fact.

    Example:
        name = "sales_by_branch"
        row_data = {
            "Branch": "North",
            "Sales": 3000
        }
    """
    pass