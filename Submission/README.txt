Sales Software Data Assessment
==================================================

Overview
--------
This solution processes sales data to calculate key metrics such as
Total Sales, Discounts Applied, and Average Customer Discount.
It handles both "TEST Part 1" (Standard) and "TEST Part 2" (Stacked Codes).

Folder Structure
----------------
Please ensure the files are organized as follows to allow the script to
locate the JSON data correctly:

submission/
│
├── main.py
│
├── TEST Part 1/
│   ├── discounts.json  (Base scenario definitions)
│   ├── products.json   (Product pricing)
│   └── orders.json     (Base order set)
│
└── TEST Part 2/
    ├── discounts.json  (Updated definitions with WINTERMADNESS)
    ├── products.json   (Product pricing)
    └── orders.json     (Updated orders with stacked codes)

How to Run
----------
1. Open your terminal or command prompt.
2. Navigate to the folder containing these files.
3. Run the following command:

   python main.py

Output
------
1. The results will be printed directly to the Console/Terminal (for immediate viewing).
2. A file named "final_output.txt" will be automatically generated containing the same results.
