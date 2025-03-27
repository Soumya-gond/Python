import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import pypdf

# Load Mistral 7B model (downloads ~4GB if not available)
model_name = "mistralai/Mistral-7B-Instruct-v0.1"
print("Loading model... (This may take time)")
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name, torch_dtype=torch.float16, device_map="auto"
)
print("Model loaded successfully!")

# Function to extract text from a PDF
def extract_text_from_pdf(pdf_path):
    try:
        with open(pdf_path, "rb") as file:
            reader = pypdf.PdfReader(file)
            text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""

# Function to ask Mistral a question
def ask_question(question, pdf_text):
    if not pdf_text:
        return "No text found in PDF."

    prompt = f"Based on the following document, answer the question:\n\n{pdf_text}\n\nQuestion: {question}\nAnswer:"
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")

    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=150)

    answer = tokenizer.decode(output[0], skip_special_tokens=True)
    return answer

# Ask the user for the PDF file
pdf_path = input("Enter PDF file path: ").strip()
pdf_text = extract_text_from_pdf(pdf_path)

if not pdf_text:
    print("Could not extract text from the PDF. Please try another file.")
else:
    question = input("Enter your question: ")
    answer = ask_question(question, pdf_text)
    print("\nAnswer:", answer)
