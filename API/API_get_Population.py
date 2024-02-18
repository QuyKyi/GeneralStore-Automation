import requests

# Define the API endpoint
url = "https://datausa.io/api/data"
params = {
    "drilldowns": "Nation",
    "measures": "Population"
}

# Send GET request to the API
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    try:
        # Extract data from the response
        response_data = response.json()
        source = response_data["source"][0]["annotations"]["source_name"]
        data = response_data["data"]

        # Extract relevant information
        years = [int(entry["Year"]) for entry in data]
        start_year = min(years)
        end_year = max(years)
        years.sort()
        print(years)
        # Calculate growth percentages
        growth_rates = []
        i = 0
        while i < len(years)-1:
            current_year = years[i]
            Population_current_year = 0
            next_year = years[i+1]
            Population_next_year = 0
            for entry in data:
                if int(entry["Year"]) == current_year:
                    Population_current_year = int(entry["Population"])
                if int(entry["Year"]) == next_year:
                    Population_next_year = int(entry["Population"])
            i = i + 1
            growth_rate_calc = (Population_next_year - Population_current_year)/Population_current_year*100
            growth_rates.append(growth_rate_calc)
        print(growth_rates)
        # Find peak growth and lowest growth
        peak_growth = max(growth_rates)
        peak_growth_year = years[growth_rates.index(peak_growth) + 1]

        lowest_growth = min(growth_rates)
        lowest_growth_year = years[growth_rates.index(lowest_growth) + 1]

        # Output the data
        print(
            f"According to {source}, in {end_year - start_year} years from {start_year} to {end_year}, peak population growth was {peak_growth:.2f}% in {peak_growth_year} and the lowest population increase was {lowest_growth:.2f}% in {lowest_growth_year}.")
    except KeyError as e:
        print("Failed to extract required data from the API response.")
        print("KeyError:", e)
else:
    print("Failed to retrieve data from the API. Status code:", response.status_code)
