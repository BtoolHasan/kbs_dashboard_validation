from facts.summary_fact import SummaryFact
from facts.branches_fact import BranchesFact, BranchesTotalFact


class FactsGenerator:

    def generate_summary_fact(self, summary):
        return SummaryFact(
            total_sales=summary.total_sales,
            total_orders=summary.total_orders,
            average_order_value=summary.average_order_value
        )
        
    def generate_branches_facts(self, branches):

        facts = []

        for branch in branches:
            facts.append(
                BranchesFact(
                    name=branch.name,
                    sales=branch.sales,
                    orders=branch.orders,
                  
                )
            )

        return facts
    
    def generate_branches_total_fact(self, branches):

        total_sales = sum(branch.sales for branch in branches)
        total_orders = sum(branch.orders for branch in branches)

        return BranchesTotalFact(
            total_sales=total_sales,
            total_orders=total_orders
        )

    def generate_all(self, summary, branches):

        facts = []

        facts.append(
            self.generate_summary_fact(summary)
        )

        facts.extend(
            self.generate_branches_facts(branches)
        )

        facts.append(
            self.generate_branches_total_fact(branches)
        )

        return facts