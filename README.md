# AI-Solution
🌟 README.md — Embedding Indexer Project
📌 תיאור הפרויקט

הפרויקט מממש מודול פייתון המאפשר:

קריאה של מסמכי DOCX או PDF

חילוץ הטקסט הנקי מתוכן

חלוקת המסמך למקטעים (Chunks) לפי פסקאות

יצירת Embeddings לכל מקטע באמצעות מודל
models/text-embedding-004 (Google Gemini API)

שמירת כל המקטעים והוקטורים במסד נתונים PostgreSQL

המערכת נועדה לשמש כתשתית לחיפוש סמנטי, אחזור מידע, או כל יישום המבוסס על Vector Database.

#מבנה הפרויקט
project-folder/
│
├── index_documents.py     # קובץ הפייתון הראשי
├── .env                   # משתני סביבה (לא מועלה ל-Git)
└── README.md              # תיעוד הפרויקט
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

פשוט מריצים:

python index_documents.py


הסקריפט יבצע:

חילוץ תכנים מהמסמך

יצירת Embeddings

שמירה של כל מקטע + וקטור בטבלה embeddings
⭐ המשך README.md — חלק אבטחה + סיכום
🛡️ הערות אבטחה

אין לשמור API Keys בקוד.

אין לשמור סיסמאות מסד נתונים בגוף הסקריפט.

כל פרטי החיבור צריכים להופיע בקובץ .env בלבד.

יש להוסיף את .env ל־.gitignore כדי למנוע העלאה ל־GitHub.

הקפידי לא לשתף את כתובת החיבור המלאה (POSTGRES_URL) עם אחרים.

#🧪 בדיקות ואימות

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
