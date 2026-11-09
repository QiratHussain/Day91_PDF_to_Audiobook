from pypdf import PdfReader

reader= PdfReader("today.pdf")
for index, page in enumerate(reader.pages):
    text = page.extract_text()
    print(f"--- Page {index + 1} ---")
    print(text)


# TODO: 2. send pdf text to api
# TODO: 3. receive voice from api
# TODO: 4. run the voice received
