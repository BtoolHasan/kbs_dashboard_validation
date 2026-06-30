class ExcelProcessor:

    def __init__(self, parser, router):
        self.parser = parser
        self.router = router

    def process(self, workbook):

        results = {}

        for sheet in workbook.worksheets:

            sheet_name = sheet.title

            sheet_data = list(
                sheet.iter_rows(values_only=True)
            )

            sheet_info = self.parser.parse(sheet_name)

            handler = self.router.create_handler(
                sheet_info.sheet_type
            )

            result = handler.process(
                sheet_data,
                sheet_info
            )

            results[sheet_info.metric_name] = result

        return results