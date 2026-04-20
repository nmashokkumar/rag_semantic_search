import pandas as pd

def load_data(file_path: str):
    df = pd.read_csv(r"F:\job_hunting_projects\rag\data\Sample - Superstore.csv", encoding="latin1")
    return df


def convert_to_text(df: pd.DataFrame):
    documents = []

    for _, row in df.iterrows():
        text = (
            f"Order {row['Order ID']} placed on {row['Order Date']} "
            f"by {row['Customer Name']} in {row['Segment']} segment "
            f"from {row['City']}, {row['State']}, {row['Region']}. "
            f"Product: {row['Product Name']} (Category: {row['Category']}, Sub-category: {row['Sub-Category']}). "
            f"Sales: {row['Sales']}, Quantity: {row['Quantity']}, "
            f"Discount: {row['Discount']}, Profit: {row['Profit']}."
        )
        documents.append(text)

    return documents