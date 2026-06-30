from excel_reader.sheet_type import SheetType
from handlers.data_label_handler import DataLabelHandler
from handlers.table_handler import TableHandler


class SheetRouter:
    """
    Strict router that maps SheetType → Handler.

    No intelligence. No inference.
    Pure deterministic mapping.
    """

    def __init__(self):
        self._registry = {
            SheetType.DATA_LABEL: DataLabelHandler,
            SheetType.TABLE: TableHandler,
       
        }

    def get_handler(self, sheet_type: SheetType):
        """
        Return handler class based on sheet type.
        """

        if sheet_type not in self._registry:
            raise ValueError(
                f"No handler registered for sheet type: {sheet_type}"
            )

        return self._registry[sheet_type]

    def create_handler(self, sheet_type: SheetType, *args, **kwargs):
        """
        Instantiate handler directly.
        """

        handler_class = self.get_handler(sheet_type)
        return handler_class(*args, **kwargs)