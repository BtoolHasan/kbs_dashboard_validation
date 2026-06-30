import collections
import collections.abc

# Fix for experta compatibility
collections.Mapping = collections.abc.Mapping
collections.MutableMapping = collections.abc.MutableMapping
collections.Sequence = collections.abc.Sequence

from excel_reader.file_loader import load_excel
from excel_reader.sheet_name_parser import SheetNameParser
from routing.sheet_router import SheetRouter
from excel_reader.excel_processor import ExcelProcessor

from generators.facts_generator import FactGenerator
from rules.dashboard_validation_engine import ValidationEngine      


def main():

    # 1) Load Excel file
    workbook = load_excel(
        "data/KBS_Dashboard_Generic_v2.xlsx"
    )

    print("Sheets:", workbook.sheetnames)

    # 2) Process workbook
    parser = SheetNameParser()
    router = SheetRouter()

    processor = ExcelProcessor(
        parser=parser,
        router=router
    )

    processed_data = processor.process(workbook)

    print("\nProcessed Data:")
    print(processed_data)

    # 3) Generate Facts
    fact_generator = FactGenerator()
    facts = fact_generator.generate(processed_data)

    print("\nGenerated Facts:")
    for fact in facts:
        print(fact)

    # 4) Run Validation Engine
    engine = ValidationEngine(
        mapping_path="config/mapping.json"
    )

    engine.reset()

    for fact in facts:
        engine.declare(fact)

    engine.run()
    engine.run_validation()

    # 5) Print results
    print("\nValidation Errors:")

    if engine.errors:
        for error in engine.errors:
            print("❌", error)
    else:
        print("✅ All validations passed successfully!")


if __name__ == "__main__":
    main()