from pathlib import Path
import fitz

source = Path("attached_assets/Sachi_Bajaj_August_2026_1790210384368.pdf")
output = Path(".agents/outputs/resume-pages")
output.mkdir(parents=True, exist_ok=True)

document = fitz.open(source)
print(f"pages={document.page_count}")
for number, page in enumerate(document, start=1):
    pixmap = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
    destination = output / f"page-{number}.png"
    pixmap.save(destination)
    print(destination)