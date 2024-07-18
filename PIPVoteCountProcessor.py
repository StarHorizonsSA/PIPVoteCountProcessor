import pandas as pd
import json
import os
from datetime import datetime
import pytz

# Define the file paths (replace these placeholders with actual file paths)
json_files = {
    'PIP-01': 'c:\\path\\to\\your\\json\\file\\bc8475e4-0525-4fba-b4f8-b848ccde7a9d.json',
    'PIP-02': 'c:\\path\\to\\your\\json\\file\\1e2d7066-ec44-46e0-945f-b2e56b1e61b0.json',
    'PIP-03': 'c:\\path\\to\\your\\json\\file\\additional_file_1.json',  # Example additional file
    'PIP-04': 'c:\\path\\to\\your\\json\\file\\additional_file_2.json'   # Another example additional file
}

def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return 0.0

# Prompt the user to choose a file
print("Please choose a JSON file:")
for key, value in json_files.items():
    print(f"{key}     {os.path.basename(value)}")

chosen_pip = input("Enter your choice (PIP-01, PIP-02, PIP-03, or PIP-04): ")

# Validate the user input
if chosen_pip not in json_files:
    print("Invalid choice. Please run the program again and choose a valid PIP.")
else:
    json_file_path = json_files[chosen_pip]
    
    try:
        # Load the JSON data
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            # Get the file's modification date
            mod_time = os.path.getmtime(json_file_path)
            mod_date = datetime.fromtimestamp(mod_time, pytz.utc).strftime("%B %d, %Y %H:%M %Z")

        # Convert the JSON data to a DataFrame
        df = pd.DataFrame(data)

        # Normalize the voteResult values to uppercase
        df['voteResult'] = df['voteResult'].str.upper()

        # Convert votingPower values to floats
        df['votingPower'] = df['votingPower'].apply(convert_to_float)

        # Aggregate the voting results
        result_counts = df['voteResult'].value_counts()
        voting_power = df.groupby('voteResult')['votingPower'].sum()

        # Ensure voting power values are numbers
        result_output = {
            'NO': {
                'count': result_counts.get('NO', 0),
                'votingPower': float(voting_power.get('NO', 0))
            },
            'YES': {
                'count': result_counts.get('YES', 0),
                'votingPower': float(voting_power.get('YES', 0))
            },
            'ABSTAIN': {
                'count': result_counts.get('ABSTAIN', 0),
                'votingPower': float(voting_power.get('ABSTAIN', 0))
            }
        }

        total_count = result_counts.sum()
        total_voting_power = voting_power.sum()

        # Determine the length of the output for alignment
        max_length = max(
            len(f"NO       {result_output['NO']['count']:>4}       VotingPower    {result_output['NO']['votingPower']:>15,.2f}"),
            len(f"YES      {result_output['YES']['count']:>4}       VotingPower    {result_output['YES']['votingPower']:>15,.2f}"),
            len(f"ABSTAIN  {result_output['ABSTAIN']['count']:>4}       VotingPower    {result_output['ABSTAIN']['votingPower']:>15,.2f}"),
            len(f"Totals   {total_count:>4}                       {total_voting_power:>15,.2f}")
        )

        # Print the formatted result
        print(f"{chosen_pip}   VOTES  {mod_date}")
        print("=" * max_length)
        print(f"NO       {result_output['NO']['count']:>4}       VotingPower    {result_output['NO']['votingPower']:>15,.2f}")
        print(f"YES      {result_output['YES']['count']:>4}       VotingPower    {result_output['YES']['votingPower']:>15,.2f}")
        print(f"ABSTAIN  {result_output['ABSTAIN']['count']:>4}       VotingPower    {result_output['ABSTAIN']['votingPower']:>15,.2f}")
        print("-" * max_length)
        print(f"Totals   {total_count:>4}                       {total_voting_power:>15,.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
