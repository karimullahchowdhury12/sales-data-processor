import json
import os
from typing import Dict


class SalesAnalyzer:
    def __init__(self, products_path: str, discounts_path: str, orders_path: str):
        self.products = self._load_products(products_path)
        self.discounts = self._load_discounts(discounts_path)
        self.orders = self._load_json(orders_path)

    def _load_json(self, path: str):
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: File not found at {path}")
            return []

    def _load_products(self, path: str) -> Dict[int, float]:
        """
        Maps SKU to Price.
        Input: [{"sku": 1001, "price": 14.99}, ...]
        Output: {1001: 14.99, ...}
        """
        data = self._load_json(path)
        return {item['sku']: item['price'] for item in data}

    def _load_discounts(self, path: str) -> Dict[str, float]:
        """
        Maps Discount Key to Value.
        Input: [{"key": "SALE10", "value": 0.1}, ...]
        Output: {"SALE10": 0.1, ...}
        """
        data = self._load_json(path)
        return {d['key']: d['value'] for d in data}

    def get_discount_value(self, code_str) -> float:
        """
        Calculates total discount percentage.
        """
        if not code_str:
            return 0.0

        # Split string by comma to handle stacked codes
        # strip() removes accidental spaces like "SALE10, WINTERMADNESS"
        codes = [c.strip() for c in code_str.split(',')]

        total_discount = 0.0
        for code in codes:
            if code in self.discounts:
                total_discount += self.discounts[code]

        return total_discount

    def analyze(self, scenario_name: str):
        total_sales_before = 0.0
        total_sales_after = 0.0
        total_money_lost = 0.0
        discount_percentages = []

        for order in self.orders:
            # Calculate Order Subtotal
            order_subtotal = 0.0
            for item in order['items']:
                sku = item['sku']
                qty = item['quantity']
                price = self.products.get(sku, 0.0)
                order_subtotal += price * qty

            # Determine Discount Percentage
            discount_str = order.get('discount')
            discount_pct = self.get_discount_value(discount_str)

            # Calculate Financials
            discount_amount = order_subtotal * discount_pct
            final_total = order_subtotal - discount_amount

            # Update Aggregates
            total_sales_before += order_subtotal
            total_sales_after += final_total
            total_money_lost += discount_amount

            # Track Data for Average
            discount_percentages.append(discount_pct)

        # Calculate Average
        if discount_percentages:
            final_avg_discount_pct = (sum(discount_percentages) / len(discount_percentages)) * 100
        else:
            final_avg_discount_pct = 0.0

        # Prepare Output Text
        output_lines = [
            f"--- {scenario_name} OUTPUT ---",
            f"Total Sales Before Discount:      ${total_sales_before:,.2f}",
            f"Total Sales After Discount:       ${total_sales_after:,.2f}",
            f"Total Money Lost via Discounts:   ${total_money_lost:,.2f}",
            f"Avg Discount per Customer:        {final_avg_discount_pct:.2f}%",
            "-" * 30,
            ""
        ]
        output_str = "\n".join(output_lines)

        # 1. Print to Console
        print(output_str)

        # 2. Save to Text File
        with open('final_output.txt', 'a') as f:
            f.write(output_str + "\n")


if __name__ == "__main__":
    # Clear previous output file if it exists
    if os.path.exists("final_output.txt"):
        os.remove("final_output.txt")

    # PART 1 EXECUTION
    # Note: Using folder "TEST Part 1" as requested
    if os.path.exists('TEST Part 1/orders.json'):
        analyzer_p1 = SalesAnalyzer(
            products_path='TEST Part 1/products.json',
            discounts_path='TEST Part 1/discounts.json',
            orders_path='TEST Part 1/orders.json'
        )
        analyzer_p1.analyze("PART 1")

    # PART 2 EXECUTION
    # Note: Using folder "TEST Part 2" as requested
    if os.path.exists('TEST Part 2/orders.json'):
        analyzer_p2 = SalesAnalyzer(
            products_path='TEST Part 2/products.json',
            discounts_path='TEST Part 2/discounts.json',
            orders_path='TEST Part 2/orders.json'
        )
        analyzer_p2.analyze("PART 2")