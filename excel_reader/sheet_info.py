from dataclasses import dataclass

from excel_reader.sheet_type import SheetType


@dataclass(frozen=True)
class SheetInfo:
    metric_name: str
    sheet_type: SheetType
