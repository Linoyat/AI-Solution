# ------------ Linoy Torogeman Home Assignment -----------
from docx import Document
import PyPDF2
import os
from dotenv import load_dotenv
import google.generativeai as genai
import psycopg2
import json


load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
POSTGRES_URL = os.getenv("POSTGRES_URL")

if not GEMINI_API_KEY:
    raise ValueError(" Error : API KEY not found ")

if not POSTGRES_URL:
    raise ValueError(" Error : POSTGRES_URL not found ")

genai.configure(api_key=GEMINI_API_KEY)


input_file = "/Users/linoy_tur/Downloads/CinamonRolls.docx"


# ---------------------- extract text function -----------------------------------
def extract_text_from_docx(path):
    doc = Document(path)
    return [p.text for p in doc.paragraphs if p.text.strip()]


def extract_text_from_pdf(path):
    text = ""
    with open(path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return [p.strip() for p in text.split("\n\n") if p.strip()]


def extract_chunks(input_file):
    ext = os.path.splitext(input_file)[1].lower()

    if ext == ".docx":
        return extract_text_from_docx(input_file)
    elif ext == ".pdf":
        return extract_text_from_pdf(input_file)
    else:
        raise ValueError("Unsupported file type")


# ------------------------- Create Embedding for each chunk -----------------------------------
def create_embedding_for_chunk(chunk_text):
    result = genai.embed_content(
        model="models/text-embedding-004",
        content=chunk_text
    )
    return result["embedding"]


# ----------------------------- Saved to DB --------------------------
def save_chunk_to_db(chunk_text, embedding, filename, strategy):
    try:
        conn = psycopg2.connect(POSTGRES_URL)
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO embeddings (chunk_text, embedding, filename, strategy_split)
            VALUES (%s, %s, %s, %s)
        """, (
            chunk_text,
            json.dumps(embedding),
            filename,
            strategy
        ))

        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        print(f"Database Error: {e}")


# ----------------------- Run ---------------------------------
try:
    chunks = extract_chunks(input_file)
    print(f" Total Chunks:{len(chunks)}")

    for chunk in chunks:
        embedding = create_embedding_for_chunk(chunk)
        save_chunk_to_db(chunk, embedding, input_file, "paragraph")

    print("Chunks Saved Successfully")

except Exception as e:
    print(f" Error: {e}")
