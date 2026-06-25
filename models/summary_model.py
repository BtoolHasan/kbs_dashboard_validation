class SummaryModel: 
    def __init__(self, total_sales : float, total_orders : int, average_order_value : float):
        self.total_sales = total_sales
        self.total_orders = total_orders
        self.average_order_value = average_order_value
        
    def __str__(self):
        return (
            f"Summary Model("
            f"total_sales={self.total_sales}, "
            f"total_orders={self.total_orders}, "
            f"average_order_value={self.average_order_value})"
        )

    def __repr__(self):
        return self.__str__()