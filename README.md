# PIPVoteCountProcessor
This program processes JSON files of Star Atlas PIP voting records. The user selects a file, and the program extracts, normalizes, and aggregates the voting data, then displays the results in the terminal, including the vote counts and voting power for YES, NO, and ABSTAIN, with timestamps in UTC.

# Program Description
This program processes JSON files containing Star Atlas PIP (Project Improvement Proposal) voting records and converts them into a human-readable format. The user is prompted to select a JSON file from a predefined list. The program then extracts and normalizes the voting data, calculates aggregate results, and displays the formatted output in the terminal. The output includes the number of votes and the total voting power for each voting option (YES, NO, ABSTAIN), with proper alignment and timestamps in UTC.

# Instructions on How to Run the Program

  1.  Install Required Libraries:
      Ensure you have Python and the required libraries installed. You can install the required libraries using pip:
    
          pip install pandas pytz

  2.  Update File Paths:
      Replace the placeholder file paths in the json_files dictionary with the actual paths to your JSON files. For example:

          json_files = {
              'PIP-01': 'c:\\Users\\fcpwa\\Desktop\\Star Atlas\\PIP\\bc8475e4-0525-4fba-b4f8-b848ccde7a9d.json',
              'PIP-02': 'c:\\Users\\fcpwa\\Desktop\\Star Atlas\\PIP\\1e2d7066-ec44-46e0-945f-b2e56b1e61b0.json',
              'PIP-03': 'c:\\Users\\fcpwa\\Desktop\\Star Atlas\\PIP\\additional_file_1.json',
              'PIP-04': 'c:\\Users\\fcpwa\\Desktop\\Star Atlas\\PIP\\additional_file_2.json'
          }

      The JSON files can be downloaded from the link located within each PIP at: https://govern.staratlas.com/proposals

  4.  Run the Script:
      Save the script to a file, for example vote_results.py, and run it in your terminal:

          python vote_results.py

  5.  View the Results:
      The script will process the chosen JSON file and display the voting results in the terminal.

        
