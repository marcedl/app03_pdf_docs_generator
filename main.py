from fpdf import FPDF
import pandas as pd 
#instance creation
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0) #to use footer pages shouldn't be broken automatically

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page() #first page added

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    for i in range(20, 290, 10):
        pdf.line(10, i, 200, i)
    pdf.line(10, 20, 200, 20)
    #Set footer only on first page
    pdf.ln(265)


    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        for i in range(20, 290, 10):
            pdf.line(10, i, 200, i)
        #Set footer for other pages
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")


#get the output
pdf.output("output.pdf")
