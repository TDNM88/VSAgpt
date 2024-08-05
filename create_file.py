import openai
from docx import Document
from fpdf import FPDF

def create_text_file(conversation, filename, file_format, api_key):
    """
    Generates a text file, DOCX, or PDF with content from the conversation using OpenAI API.
    
    Parameters:
    - conversation (str): The conversation or specified content to be summarized or included.
    - filename (str): The name of the output file.
    - file_format (str): The format of the output file ('txt', 'docx', or 'pdf').
    - api_key (str): The OpenAI API key.
    """
    
    openai.api_key = api_key
    
    prompt = f"Please summarize the following conversation or specified content in a coherent and complete manner:\n\n{conversation}"
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        
        summary = response['choices'][0]['message']['content']
        
        if file_format == 'txt':
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(summary)
        elif file_format == 'docx':
            doc = Document()
            doc.add_paragraph(summary)
            doc.save(filename)
        elif file_format == 'pdf':
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 10, summary)
            pdf.output(filename)
        else:
            return {"status": "error", "message": "Unsupported file format. Please choose 'txt', 'docx', or 'pdf'."}
        
        return {"status": "success", "message": f"File '{filename}' has been created successfully."}
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
