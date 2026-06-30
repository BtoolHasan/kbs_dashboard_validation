import json
from experta import KnowledgeEngine, Rule, MATCH
from facts.facts import MetricFact, TableRowFact


class ValidationEngine(KnowledgeEngine):

    def __init__(self, mapping_path):
        super().__init__()

        with open(mapping_path, "r") as f:
            self.mapping = json.load(f)

        self.metrics = {}
        self.tables = {}
        self.errors = []
        
    @Rule(MetricFact(name=MATCH.name, value=MATCH.value))
    def collect_metric(self, name, value):
        self.metrics[name] = value
        
    @Rule(TableRowFact(name=MATCH.name, row_data=MATCH.row))
    def collect_table(self, name, row):
        self.tables.setdefault(name, []).append(row)
        
    
    def run_validation(self):

        for metric_name, config in self.mapping.items():

            if metric_name not in self.metrics:
                self.errors.append(f"Missing metric: {metric_name}")
                continue

            metric_value = self.metrics[metric_name]

            table_name = config["source_table"]
            field = config["field"]

            rows = self.tables.get(table_name, [])

            calculated = sum(
                row.get(field, 0) for row in rows
            )

            if calculated != metric_value:
                self.errors.append(
                    f"{metric_name} mismatch: expected {metric_value}, got {calculated}"
                )