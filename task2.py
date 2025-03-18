import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import random
import os

def generate_sample_data(filename="sample_data.csv"):
    data = {
        "Product": [f"Item_{i}" for i in range(1, 11)],
        "Sales": [random.randint(100, 1000) for _ in range(10)],
    }
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Sample data saved to {filename}")
    return df

def analyze_data(df, summary_file="summary.txt"):
    summary = df.describe()
    with open(summary_file, "w") as f:
        f.write(str(summary))
    print(f"Data summary saved to {summary_file}")
    return summary

def generate_bar_chart(df, chart_file="sales_chart.png"):
    plt.figure(figsize=(6, 4))
    plt.bar(df["Product"], df["Sales"], color="skyblue")
    plt.xticks(rotation=45)
    plt.title("Sales Data")
    plt.xlabel("Products")
    plt.ylabel("Sales Amount")
    plt.savefig(chart_file)
    plt.close()
    print(f"Sales chart saved to {chart_file}")
    return chart_file

def generate_pdf_report(summary, chart_file, pdf_file="Automated_Report.pdf"):
    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.setFont("Helvetica", 14)
    c.drawString(100, 750, "Automated Sales Report")
    c.setFont("Helvetica", 10)

    # Adding Summary to PDF
    y_position = 730
    for line in str(summary).split("\n"):
        c.drawString(100, y_position, line)
        y_position -= 15  # Move text down
    
    # Adding Chart to PDF
    c.drawImage(chart_file, 100, y_position - 200, width=400, height=200)
    c.save()
    print(f"PDF report generated: {pdf_file}")
    return pdf_file

def main():
    # Step 1: Generate Sample Data
    df = generate_sample_data()
    
    # Step 2: Perform Data Analysis
    summary = analyze_data(df)
    
    # Step 3: Generate Sales Chart
    chart_file = generate_bar_chart(df)
    
    # Step 4: Generate PDF Report
    generate_pdf_report(summary, chart_file)

if __name__ == "__main__":
    main()