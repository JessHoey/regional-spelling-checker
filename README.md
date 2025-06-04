# 📝 Regional Spelling Checker (UK/US)

A simple Python command-line tool for detecting and comparing UK and US English spelling variations in text. Useful for students, writers, editors, or developers who want to ensure consistent spelling in notes, essays, or documentation.

---

## 🛠 Requirements

-Python 3.x
- For future web application : may need flask 

---

## 🔧 Features

- Detects UK and US spelling inconsistencies
- Highlights mixed usage in a single text
- Provides suggested alternatives for each spelling
- Customisable word pair list stored in a plain text file (`spelling_pairs.txt`)
- Accepts pasted text or reads from a `.txt` file

---

## 📁 Files Included

- `spelling_checker.py` — the main Python script
- `spelling_pairs.txt` — editable list of word pairs (`uk,us` format)

---

## ▶️ How to Use

### Option 1: Paste Text
python spelling_checker.py

### Option 2: Paste Text
python spelling_checker.py yourfile.txt

---

## 📚 Files Included

📘 UK spellings found:
 - organise (US: organize)
 - licence (US: license)

📙 US spellings found:
 - color (UK: colour)

⚠️ Mixed UK/US spelling detected — consider standardising.

---

## ✍️ Customise Word Pairs

You can edit spelling_pairs.txt to include more variations:

realise,realize
favourite,favorite
travelling,traveling

Use one word pair per line, separated by a comma.

## 💡 Future Ideas

Save results to a text file

Highlight results in-line

Add a web or GUI version

Package as a .exe for non-Python users
