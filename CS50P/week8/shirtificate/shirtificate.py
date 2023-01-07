from fpdf import FPDF


class MYPDF():
    def __init__(self, name):
        # Initiate an instance of the FPDF class
        self._pdf = FPDF()
        # Sets the font
        self._pdf.set_font("Helvetica", size=60)
        # Creating a page
        self._pdf.add_page()
        # Creating the header
        self._pdf.cell(w=0, h=50, txt="CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        # Gets the shirt from VS Code
        self._pdf.image("shirtificate.png", w=self._pdf.epw, alt_text="CS50 Shirtificate")
        # Sets font size, color and location of the Name printed on the shirt
        self._pdf.set_font_size(25)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=47.5, y=140, txt=f"{name} took CS50")


    def save(self, name):
        self._pdf.output(name)


def main():
    name = input("Name: ")
    new_pdf = MYPDF(name)
    new_pdf.save("shirtificate.pdf")



if __name__ == "__main__":
    main()