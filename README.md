

#  ID Card Generator

This project is a simple and efficient **ID card generator** built with Python. It reads employee data from a CSV file, combines it with corresponding images, and automatically generates professional ID cards in PDF format.

---

##  Project Structure

```

id\_card\_generator/
├── photos/               # Folder containing employee photos
├── employee.csv          # Employee data (name, position, photo name, etc.)
├── logo.png              # Organization logo to be placed on ID cards
├── generate\_ids.py       # Python script to generate the ID cards
├── employee\_ids.pdf      # Sample output (combined PDF of all ID cards)
└── README.md             # Project documentation

````

---

##  Features

- Reads employee details from a CSV file
- Automatically matches each employee with their photo
- Generates individual ID cards
- Supports exporting to a single PDF (`employee_ids.pdf`)
- Customizable layout and design (including logos)

---

##  Requirements

- Python 3.x
- Libraries:
  - `Pillow`
  - `reportlab`
  - `csv`
  - `os`

Install dependencies using pip:

```bash
pip install pillow reportlab
````

---

##  How to Use

1. Place all employee photos inside the `photos/` directory.
2. Update `employee.csv` with employee details:

```
name,position,photo
John Doe,Manager,john_doe.jpg
Jane Smith,Engineer,jane_smith.jpg
```

3. Run the Python script:

```bash
python generate_ids.py
```

4. Find the generated `employee_ids.pdf` in your project folder.

---

##  Sample Output

The script creates a single PDF file (`employee_ids.pdf`) containing all generated ID cards.

---

##  Customization

You can customize the ID card layout by editing the `generate_ids.py` script:

* Change fonts, colors, or card dimensions
* Adjust the positioning of text, images, and logos
* Add additional fields (e.g., department, contact number, QR codes)

---


---

## 👤 Author

**Chandana Rajashekhar**
GitHub: [@Chandana9700](https://github.com/Chandana9700)

---

##  Show Your Support

If you find this project helpful, please ⭐️ the repo and share it with others!

````



