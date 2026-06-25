class BranchModel:

    def __init__(
        self,
        name: str,
        sales: float,
        orders: int
    ):
        self.name = name
        self.sales = sales
        self.orders = orders

    def __str__(self):
        return (
            f"Branch Model("
            f"name='{self.name}', "
            f"sales={self.sales}, "
            f"orders={self.orders})"
        )
        
    def __repr__(self):
        return self.__str__()