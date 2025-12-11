# AI-Solution
🌟 README.md — Embedding Indexer Project

📌 תיאור הפרויקט


הפרויקט מממש תשתית מלאה הכוללת:
קריאה של קבצי DOCX ו־PDF
חילוץ טקסט נקי
חלוקת המסמך למקטעים (Chunks) לפי פסקאות
יצירת Embeddings לכל מקטע באמצעות Google Gemini
שמירה של כל המקטעים והוקטורים במסד נתונים PostgreSQL
המערכת נועדה לשמש בסיס לפיתוח חיפוש סמנטי, מערכות RAG, וכל יישום המתבסס על אחזור מידע באמצעות Vector Database.

models/text-embedding-004 (Google Gemini API)

שמירת כל המקטעים והוקטורים במסד נתונים PostgreSQL
המערכת נועדה לשמש כתשתית לחיפוש סמנטי, אחזור מידע, או כל יישום המבוסס על Vector Database.

מבנה הפרויקט
<img width="640" height="158" alt="image" src="https://github.com/user-attachments/assets/019ef74b-34ca-4c10-8e16-3997d30758e1" />


⚙️ דרישות מערכת


Python 3.10+
PostgreSQL 16+
חיבור אינטרנט ליצירת Embeddings מול Google Gemini API

🏗️ התקנת הפרויקט

1️⃣ התקנת ספריות נדרשות

pip install python-docx PyPDF2 psycopg2-binary python-dotenv google-generativeai

🔐 קובץ .env — הגדרת משתני סביבה

חשוב: קובץ .env לא מועלה ל-Git כדי למנוע חשיפת מפתחות API.

יש ליצור קובץ בשם .env:

GEMINI_API_KEY=your_api_key_here
POSTGRES_URL=postgresql://username:password@localhost:5432/documents_db

🗄️ מבנה מסד הנתונים PostgreSQL

יש ליצור טבלה בשם embeddings:

CREATE TABLE embeddings (
    id SERIAL PRIMARY KEY,
    chunk_text TEXT,
    embedding JSONB,
    filename TEXT,
    strategy_split TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

🚀 הרצת המערכת

הפעלת המערכת

יש להגדיר את הנתיב לקובץ:
input_file = "/path/to/your/document.pdf"
הרצה:
python index_documents.py


הסקריפט יבצע:
חילוץ טקסט
חלוקה למקטעים
יצירת Embeddings
שמירה במסד הנתונים

🧪 בדיקות לאחר ההרצה

✔️ הטבלה embeddings קיימת
✔️ כל המקטעים נשמרו
✔️ הוקטורים נשמרו כ־JSON
✔️ מספר השורות מתאים למספר ה־Chunks

🛡️ הערות אבטחה

אין לשמור API Keys בקוד.
אין לשמור סיסמאות מסד נתונים בגוף הסקריפט.
כל פרטי החיבור צריכים להופיע בקובץ .env בלבד.
יש להוסיף את .env ל־.gitignore כדי למנוע העלאה ל־GitHub.
הקפיד לא לשתף את כתובת החיבור המלאה (POSTGRES_URL) עם אחרים.

🧪 בדיקות ואימות

לאחר הרצת index_documents.py, יש לבדוק:
שהטבלה embeddings נוצרה בהצלחה במסד הנתונים
שכל מקטע טקסט נשמר
שה-Embedding נשמר במבנה JSON
שמספר השורות בטבלה תואם למספר ה־Chunks

📚 טכנולוגיות בשימוש


Python (עיבוד טקסט ויצירת Embeddings)

Google Gemini API (יצירת וקטורים)

PostgreSQL (אחסון המקטעים והוקטורים)

psycopg2 (תקשורת בין פייתון למסד הנתונים)

python-docx, PyPDF2 (קריאת מסמכים)

dotenv לניהול מפתחות API
✔️ סיכום

הפרויקט מדגים תהליך מלא של:
עבודה עם קבצים (PDF/DOCX)
עיבוד טקסט וחלוקה למקטעים
שימוש ב־Google Gemini ליצירת Embeddings
שמירה יעילה במסד PostgreSQL
עבודה בטוחה עם משתני סביבה

מצ״ב דוגמאות לפלט תקין
<img width="568" height="104" alt="image" src="https://github.com/user-attachments/assets/28992596-c3cf-4309-b6ce-9289632d7263" />
<img width="2804" height="1482" alt="image" src="https://github.com/user-attachments/assets/603f805e-2fab-4039-b61f-321ddc4a501f" />



