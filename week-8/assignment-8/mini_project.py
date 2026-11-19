import csv

file_path = "../data/messy_data.csv"

clean_rows = []
skipped_rows = []
rows_attempted = 0

try:
    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row_num, row in enumerate(reader, start=1):
            rows_attempted += 1

            if None in row:
                skipped_rows.append(f"Row {row_num}: extra column detected - skipped")
                continue

            try:
                name = row["name"].strip()
                category = row["category"].strip()
                raw_amount = row["amount"].strip()

                if not name or not category:
                    skipped_rows.append(f"Row {row_num}: missing name or category - skipped")
                    continue

                amount = float(raw_amount)

                clean_rows.append({
                    "name": name,
                    "category": category,
                    "amount": amount
                })

            except ValueError:
                skipped_rows.append(f"Row {row_num}: ValueError - could not convert '{row.get('amount', '')}' to float")
            except KeyError as e:
                skipped_rows.append(f"Row {row_num}: KeyError - missing expected column {e}")

except FileNotFoundError:
    print(f"Error: Could not find '{file_path}'. Please ensure the file exists and try again.")
    exit()

print("=== CSV Report ===")
print(f"Rows attempted: {rows_attempted}")
print(f"Rows parsed:    {len(clean_rows)}")
print(f"Rows skipped:   {len(skipped_rows)}")

print("\nSkipped rows:")
for skip_msg in skipped_rows:
    print(f"  {skip_msg}")

print("\nClean data:")
for item in clean_rows:
    print(f"  {item['name']} | {item['category']} | ${item['amount']:.2f}")
