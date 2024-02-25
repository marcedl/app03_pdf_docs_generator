from fpdf import FPDF
#instance creation
pdf = FPDF(orientation="P", unit="mm", format="A4")
#add a page
pdf.add_page()#method for the instance

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello there", align="L", ln=1, border=1)
pdf.cell(w=0, h=12, txt="Hi there", align="L", ln=1, border=1)

#to add more pages copy the code above

pdf.add_page()#method for the instance

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello there", align="L", ln=1, border=1)
pdf.cell(w=0, h=12, txt="Hi there", align="L", ln=1, border=1)

#get the output
pdf.output("output.pdf")
