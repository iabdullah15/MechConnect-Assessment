import argparse
import pandas as pd


def analyze(filename, print_to_console=True):

    df = pd.read_csv(filename)
    # Average price of spare parts by manufacturer.
    average_price_by_manufacturer = df.groupby("manufacturer").agg(
        average_price=('price', 'mean'),
    )
    # Count of spare parts by compatible car models.
    spare_parts_count_by_car_model = df.groupby("car_model").agg(
        spare_part_count=('part_name', 'count')
    )

    # Top 10 expensive parts
    top_expensive_parts = df[["part_name", "category", "car_model", "price"]].sort_values(
        "price", ascending=False).head(10)

    # Average Price by Category
    average_price_by_category = df.groupby("category").agg(
        average_price=('price', 'mean')
    )

    # Top 10 Parts with the lowest stock
    top_lowest_stock_parts = df[["part_name", "quantity", "category",
                                 "car_model", "price"]].sort_values("quantity", ascending=True).head(10)

    # Printing to the console
    if print_to_console:
        print("Average Price of parts grouped by manufacturer\n")
        print(average_price_by_manufacturer)
        print()

        print("Count of parts grouped by car_model\n")
        print(spare_parts_count_by_car_model)
        print()

        print("Top 10 expensive parts\n")
        print(top_expensive_parts)
        print()

        print("Average Price of parts grouped by category\n")
        print(average_price_by_category)
        print()

        print("Parts with the lowest stock\n")
        print(top_lowest_stock_parts)

    return (average_price_by_manufacturer, average_price_by_category, spare_parts_count_by_car_model, top_expensive_parts, top_lowest_stock_parts)


def remove_dups(filename):

    df = pd.read_csv(filename)
    df_cleaned = df.drop_duplicates()
    df_cleaned.to_csv('cleaned_data.csv', index=False)
    
    print(f"The data from {filename} has been cleaned and saved to the cleaned_data.csv file")


def generate_report(filename):

    average_price_by_manufacturer, average_price_by_category, spare_parts_count_by_car_model, top_expensive_parts, top_lowest_stock_parts = analyze(
        filename, print_to_console=False)

    report_filename = 'report.csv'

    with open(report_filename, 'w', newline="") as f:

        f.write("Average Price by Manufacturer\n")
        average_price_by_manufacturer.to_csv(f, index=True)
        f.write("\n")

        f.write("Average Price by Category\n")
        average_price_by_category.to_csv(f, index=True)
        f.write("\n")
        
        f.write("Count of parts grouped by car_model\n")
        spare_parts_count_by_car_model.to_csv(f, index=True)
        f.write("\n")
        
        f.write("Top 10 expensive parts\n")
        top_expensive_parts.to_csv(f, index=False)
        f.write("\n")
        
        f.write("Top 10 parts with the lowest stock\n")
        top_lowest_stock_parts.to_csv(f, index=False)
        f.write("\n")

    print("Your report has been generated and saved in the report.csv file.")

def main():

    filename = 'spare_parts_dataset.csv'
    parser = argparse.ArgumentParser(
        description="A simple command line tool for data analysis and cleaning")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--analyze", action="store_true",
                       help="Perform data analysis")
    group.add_argument("--remove-duplicates",
                       action="store_true", help="Remove duplicate data")
    group.add_argument("--generate-report", action="store_true",
                       help="Generate a report on the analysis of data")

    args = parser.parse_args()

    if args.analyze:
        analyze(filename)
    elif args.remove_duplicates:
        remove_dups(filename)
    elif args.generate_report:
        generate_report(filename)
    else:
        parser.error(
            "At least one of --analyze, --generate-report, or --remove-duplicates must be provided.")


if __name__ == '__main__':
    main()
