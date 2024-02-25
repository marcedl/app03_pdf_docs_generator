from fpdf import FPDF
import pandas as pd 
#instance creation
pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page() #first page added

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10, 20, 200, 20)

    for i in range(row["Pages"] - 1):
        pdf.add_page()

#get the output
pdf.output("output.pdf")
