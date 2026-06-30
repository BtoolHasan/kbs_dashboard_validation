from excel_reader.sheet_info import SheetInfo
from excel_reader.sheet_type import SheetType


class SheetNameParser:
    """
    STRICT Convention-based Sheet Parser

    Expected format:
        <metric_name>-<sheet_type>

    Examples:
        TotalSales-data_label
        sales_by_branch-table

    Note:
        This system does NOT perform any intelligent inference.
        It strictly validates predefined naming conventions.
    """

    SEPARATOR = "-"

    @staticmethod
    def parse(sheet_name: str) -> SheetInfo:
        """
        Parse sheet name into structured SheetInfo object.
        """

        if not isinstance(sheet_name, str):
            raise TypeError("Sheet name must be a string.")

        sheet_name = sheet_name.strip()

        if not sheet_name:
            raise ValueError("Sheet name cannot be empty.")

        # Split using strict convention
        parts = sheet_name.split(SheetNameParser.SEPARATOR)

        if len(parts) != 2:
            raise ValueError(
                f"Invalid sheet name format: '{sheet_name}'\n"
                f"Expected format: <metric_name>{SheetNameParser.SEPARATOR}<sheet_type>"
            )

        metric_name = parts[0].strip()
        sheet_type_raw = parts[1].strip()

        if not metric_name:
            raise ValueError(f"Metric name is empty in '{sheet_name}'.")

        if not sheet_type_raw:
            raise ValueError(f"Sheet type is empty in '{sheet_name}'.")

        # Strict enum validation
        try:
            sheet_type = SheetType(sheet_type_raw)

        except ValueError:
            supported = ", ".join(t.value for t in SheetType)

            raise ValueError(
                f"Unsupported sheet type: '{sheet_type_raw}' in '{sheet_name}'\n"
                f"Supported types: {supported}"
            )

        return SheetInfo(
            metric_name=metric_name,
            sheet_type=sheet_type
        )   