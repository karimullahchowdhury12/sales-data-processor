
# Project Title

A brief description of what this project does and who it's for

# Sales Data Analytics Engine (Technical Assessment)

## 📌 Overview
This project is a high-performance Python-based data processor designed to ingest JSON-formatted sales datasets. It calculates critical business metrics including gross sales, net revenue, and discount impact.

The system was developed to handle two distinct scenarios:
1.  **Base Sales Processing:** Standard single-discount application.
2.  **Stacked Discount Logic:** An additive stacking algorithm (e.g., 30% + 10% = 40%) to handle complex promotional events like `WINTERMADNESS`.

## 🛠 Features
- **Flexible Data Ingestion:** Parses Discount, Product, and Order JSON schemas.
- **Additive Discount Stacking:** Custom logic to handle multiple concurrent discount codes as per the Part 2 requirements.
- **Precision Reporting:** Calculates:
    - Total sales (Pre-discount)
    - Total sales (Post-discount)
    - Total revenue lost to discounts
    - Average discount percentage per customer

## 📁 Project Structure
```text
.
├── main.py              # Core logic and processing engine
├── TEST Part 1/
|   ├── discounts.json
|   ├── products.json
|   ├── orders.json
├── TEST Part 2/
|   ├── discounts.json
|   ├── products.json
|   ├── orders.json
└── README.md
```
## 🚀 Installation & Usage
### 1. Clone the repository:

```bash
git clone https://github.com/karimullahchowdhury12/sales-data-processor.git
cd sales-data-processor
```
### 2. Run the processor:

```bash
python main.py
```
## 🧪 Logic Implementation
The core of the solution focuses on O(n) time complexity for order processing. By pre-loading product pricing into a hash map (dictionary), we ensure that item lookups during order summation stay efficient, even as the dataset scales.

## 📝 Assumptions
All prices are processed as floats/decimals for precision.

Discount codes in Part 2 are applied additively to the total percentage before being deducted from the gross amount.
