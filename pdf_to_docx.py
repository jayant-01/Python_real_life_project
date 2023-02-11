from pdf2docx import converter
pdf_file="Japanese-Hiragana-Resources-HiraganaKatakanaWorksheet.pdf"
docx_file="sheet.docx"
cv= converter(pdf_file)
cv.convert(docx_file)
cv.close()