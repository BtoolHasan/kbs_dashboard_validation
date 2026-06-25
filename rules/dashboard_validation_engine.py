from experta import KnowledgeEngine, Rule, MATCH, TEST

from facts.branches_fact import BranchesTotalFact
from facts.summary_fact import SummaryFact

class DashboardValidationEngine(KnowledgeEngine):
    #total sales NOT correct
    @Rule(
    SummaryFact(total_sales=MATCH.summary_total),
    BranchesTotalFact(total_sales=MATCH.branches_total),
    TEST(lambda summary_total, branches_total:
         summary_total != branches_total)
    )
    def total_sales_mismatch(self,
                            summary_total,
                            branches_total):

        print(
            f"[ERROR] Total Sales mismatch. "
            f"Summary={summary_total}, "
            f"Branches={branches_total}"
        )
        
    #total sales are correct        
    @Rule(
    SummaryFact(total_sales=MATCH.summary_total),
    BranchesTotalFact(total_sales=MATCH.branches_total),
    TEST(lambda summary_total, branches_total:
         summary_total == branches_total)
    )
    def correct_total_sales(self,
                            summary_total,
                            branches_total):

        print(
            f"Total Sales are correct: "
            f"Summary={summary_total}, "
            f"Branches={branches_total}"
        )
       
       
    #total orders NOT correct
    @Rule(
    SummaryFact(total_orders=MATCH.summary_total),
    BranchesTotalFact(total_orders=MATCH.branches_total),
    TEST(lambda summary_total, branches_total:
         summary_total != branches_total)
    )
    def total_orders_mismatch(self,
                            summary_total,
                            branches_total):

        print(
            f"[Error] Total Orders mismatch. "
            f"Summary={summary_total}, "
            f"Branches={branches_total}"
        )
         
    #total orders are correct
    @Rule(
    SummaryFact(total_orders=MATCH.summary_total),
    BranchesTotalFact(total_orders=MATCH.branches_total),
    TEST(lambda summary_total, branches_total:
         summary_total == branches_total)
    )
    def correct_total_orders(self,
                            summary_total,
                            branches_total):

        print(
            f"Total Orders are correct: "
            f"Summary={summary_total}, "
            f"Branches={branches_total}"
        )