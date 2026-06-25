
from models.branches_model import BranchModel
from models.summary_model import SummaryModel


class DataExtractor:
    def __init__(self, workbook):
        self.workbook = workbook

    def extract(self):
        summary = self._extract_summary()
        branch = self._extract_branches()
        return summary , branch

    def _extract_summary(self):
        sheet = self.workbook["Summary"]

        mapping = {
            "Total Sales": "total_sales",
            "Total Orders": "total_orders",
            "Average Order Value": "average_order_value"
        }

        summary = SummaryModel(
            total_sales=None,
            total_orders=None,
            average_order_value=None
        )

        for row in sheet.iter_rows(values_only=True):
            if not row[0]:
                continue

            key, value = row[0], row[1]

            if key in mapping:
                setattr(summary, mapping[key], value)

        return summary
    
    
    def _extract_branches(self):
        sheet = self.workbook["Branches"]

        rows = list(sheet.iter_rows(values_only=True))
        headers = rows[0]
        data_rows = rows[1:]

        branches = []

        for row in data_rows:
            if not row[0]:
                continue

            branch = BranchModel(
                name=row[0],
                sales=row[1],
                orders=row[2],
            )

            branches.append(branch)

        return branches