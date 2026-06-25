import collections
import collections.abc
collections.Mapping = collections.abc.Mapping
from generators.facts_generator import FactsGenerator

collections.Mapping = collections.abc.Mapping
collections.MutableMapping = collections.abc.MutableMapping
collections.Sequence = collections.abc.Sequence

from experta import *
from excel_reader.data_extractor import DataExtractor
from excel_reader.file_loader import load_excel
from facts.branches_fact import BranchesTotalFact
from facts.summary_fact import SummaryFact
from rules.dashboard_validation_engine import DashboardValidationEngine

def main():
    workbook = load_excel(
        "data/KBS_Dashboard_Validation_v1.xlsx"
    )

    print(workbook.sheetnames)  

    extractor = DataExtractor(workbook)
    summary, branches = extractor.extract()
    generator = FactsGenerator()
    facts = generator.generate_all(summary, branches)
    engine = DashboardValidationEngine()
    engine.reset()

    for fact in facts:
        engine.declare(fact)

    engine.run()



if __name__ == "__main__":
    main()