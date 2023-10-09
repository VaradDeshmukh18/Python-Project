import PyPDF2


def merge_pdfs(pdf1_path, pdf2_path, output_path):
  
    with open(pdf1_path, 'rb') as pdf1_file:
      
        pdf1_reader = PyPDF2.PdfFileReader(pdf1_file)

      
        with open(pdf2_path, 'rb') as pdf2_file:
           
            pdf2_reader = PyPDF2.PdfFileReader(pdf2_file)

          
            pdf_writer = PyPDF2.PdfFileWriter()

          
            for page_num in range(pdf1_reader.getNumPages()):
                page = pdf1_reader.getPage(page_num)
                pdf_writer.addPage(page)

           
            for page_num in range(pdf2_reader.getNumPages()):
                page = pdf2_reader.getPage(page_num)
                pdf_writer.addPage(page)

          
            with open(output_path, 'wb') as output_file:
                # Write the combined PDF to the output file
                pdf_writer.write(output_file)

if __name__ == "__main__":
    pdf1_path = 'path_to_first_pdf.pdf' 
    pdf2_path = 'path_to_second_pdf.pdf' 
    output_path = 'output_merged.pdf'   

    merge_pdfs(pdf1_path, pdf2_path, output_path)
    print(f"PDFs merged and saved to {output_path}")
