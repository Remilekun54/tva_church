from about.models import PresidingPastor, FoundingPastor

p = PresidingPastor.objects.first()
f = FoundingPastor.objects.first()

print("--- Presiding Pastor ---")
if p:
    print(f"Name: {p.pastor_name}")
    print(f"Selar: {p.selar_book_url}")
    print(f"Amazon: {p.amazon_book_url}")
    print(f"Contact Email: {p.contact_email}")
    print(f"LinkedIn: {p.linkedin_url}")
else:
    print("No Presiding Pastor found.")

print("\n--- Founding Pastor ---")
if f:
    print(f"Selar: {f.selar_book_url}")
    print(f"Amazon: {f.amazon_book_url}")
    print(f"LinkedIn: {f.linkedin_url}")
else:
    print("No Founding Pastor found.")
