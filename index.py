import csv

# Open the CSV file
with open('aniket.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.DictReader(file)
    
    # Initialize dictionaries to store total valuation increase and count of startups by industry
    industry_total_valuation = {}
    industry_startup_count = {}
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Extract data from the row
        industry = row['IndustryVertical']
        
        # Check if IndustryVertical is not empty
        if industry:
            amount_in_usd_str = row['AmountInUSD'].replace(',', '')
            date_str = row['Date']
            
            # Check if AmountInUSD and Date are not empty
            if amount_in_usd_str and date_str:
                amount_in_usd = float(amount_in_usd_str)
                
                # Split the date string using both periods and forward slashes as delimiters
                date_parts = date_str.split('.') if '.' in date_str else date_str.split('/')
                
                # Extract the year from the date
                year = int(date_parts[-1])
                
                # Ensure that the year is reasonable (e.g., not in the future)
                current_year = 2024
                if year <= current_year:
                    # Calculate the number of years since joining
                    years_joined = current_year - year
                    
                    # Ensure that years_joined is not zero to avoid division by zero
                    if years_joined > 0:
                        # Calculate the valuation increase
                        valuation_increase = amount_in_usd / years_joined
                        
                        # Update the total valuation increase and startup count for the industry
                        if industry in industry_total_valuation:
                            industry_total_valuation[industry] += valuation_increase
                            industry_startup_count[industry] += 1
                        else:
                            industry_total_valuation[industry] = valuation_increase
                            industry_startup_count[industry] = 1
    
    # Calculate the average valuation increase for each industry
    industry_avg_valuation = {}
    for industry, total_valuation in industry_total_valuation.items():
        startup_count = industry_startup_count[industry]
        avg_valuation = total_valuation / startup_count
        industry_avg_valuation[industry] = avg_valuation
    
    print(industry_avg_valuation)
