from tabulate import tabulate
import pandas as pd

def generate_report(issues_dict):
    report = "\n--- EHR DATA QUALITY REPORT ---\n"
    for issue, data in issues_dict.items():
        report += f"\n>> {issue}:\n"

        if isinstance(data, pd.DataFrame):
            if data.empty:
                report += "No issues found.\n"
            else:
                cleaned = data.head(5).copy()

                # Convert everything to string, round floats, clean NaN
                for col in cleaned.columns:
                    cleaned[col] = cleaned[col].apply(lambda x: f"{x:.2f}" if isinstance(x, float) else str(x))
                    cleaned[col] = cleaned[col].str.replace('\n', ' ').str.strip()

                formatted = tabulate(cleaned, headers='keys', tablefmt='grid', showindex=False)
                report += formatted + "\n"

        elif isinstance(data, pd.Series):
            series_df = data.reset_index()
            series_df.columns = ['Column', 'Missing Count']
            report += tabulate(series_df, headers='keys', tablefmt='grid', showindex=False) + "\n"

        else:
            report += str(data) + "\n"

    return report




