def print_participant_data_meaning():
    participant_data = {
        "ID": "Unikalny identyfikator badanego",
        "gender": "Płeć badanego (określone wartości)",
        "age": "Wiek badanego w latach",
        "height(cm)": "Wzrost badanego w centymetrach",
        "weight(kg)": "Waga badanego w kilogramach",
        "waist(cm)": "Obwód talii badanego w centymetrach",
        "eyesight(left)": "Ostrość wzroku w lewym oku",
        "eyesight(right)": "Ostrość wzroku w prawym oku",
        "hearing(left)": "Poziom słuchu w lewym uchu (określone wartości)",
        "hearing(right)": "Poziom słuchu w prawym uchu (określone wartości)",
        "systolic": "Ciśnienie skurczowe krwi badanego",
        "relaxation": "Ciśnienie rozkurczowe krwi badanego",
        "fasting blood sugar": "Poziom glukozy na czczo we krwi badanego",
        "Cholesterol": "Całkowity poziom cholesterolu we krwi",
        "triglyceride": "Poziom trójglicerydów we krwi",
        "HDL": "Poziom cholesterolu HDL we krwi (tzw. dobry cholesterol)",
        "LDL": "Poziom cholesterolu LDL we krwi (tzw. zły cholesterol)",
        "hemoglobin": "Poziom hemoglobiny we krwi badanego",
        "Urine protein": "Zawartość białka w moczu badanego",
        "serum creatinine": "Poziom kreatyniny w surowicy krwi (wskaźnik funkcji nerek)",
        "AST": "Poziom enzymu AST (wskaźnik funkcji wątroby)",
        "ALT": "Poziom enzymu ALT (wskaźnik funkcji wątroby)",
        "Gtp": "Poziom gamma-GTP (wskaźnik funkcji wątroby)",
        "oral": "Stan zdrowia jamy ustnej badanego (ogólna ocena)",
        "dental caries": "Informacja o występowaniu próchnicy",
        "tartar": "Informacja o obecności kamienia nazębnego",
        "smoking": "Informacja o statusie palenia badanego (określone wartości)"
    }

    print("Semantyczne znaczenie danych ze zbioru:\n")
    print("| Dana | Znaczenie |")
    print("| :---- | :-------- |")

    for key, value in participant_data.items():
        print(f"| {key} | {value} |")