import requests
import pandas as pd

API_KEY = "797W289MNH3FD9SET8YJ025MYR"
url = "https://api.climatiq.io/data/v1/estimate"

#starting kWh values
#3 different energy scenarios
scenarios = {
    "Single Customer (Actual Annual)": 11568,     #drops ~2% per year
    "Single Customer (Baseline Annual)": 10800,    #stays constant
    "Wayne County (Total Consumption)": 17291241000  #drops ~0.5% per year
}

years = [2020, 2021, 2022, 2023]

results = []
#for loop to go through each energy scenario and print out a separate statement
for scenario, start_kwh in scenarios.items():
    annual_kwh = start_kwh  # reset for each scenario
    for year in years:
        payload = {
            "emission_factor": {
                "activity_id": "electricity-supply_grid-source_residual_mix",
                "data_version": "^21"
            },
            "parameters": {
                "energy": annual_kwh,
                "energy_unit": "kWh"
            }
        }

        headers = {"Authorization": f"Bearer {API_KEY}"}
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
#adding this to the empty results array from earlier for each individual scenario
        results.append({
            "Scenario": scenario,
            "Year": year,
            "Energy_kWh": round(annual_kwh, 2),
            "CO2e_kg": round(data.get("co2e", None), 2)
        })

    #in order to accurately depict a picture of emissions, have to do some approximations
        if scenario == "Single Customer (Actual Annual)":
            annual_kwh *= 0.98  
        elif scenario == "Wayne County (Total Consumption)":
            annual_kwh *= 0.995  
     

#make dataframe
df = pd.DataFrame(results).sort_values(by=["Scenario", "Year"]).reset_index(drop=True)
print(df)
df.to_csv("electricity_emissions.csv", index=False)
