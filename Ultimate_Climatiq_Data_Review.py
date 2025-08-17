import requests

MY_API_KEY = "797W289MNH3FD9SET8YJ025MYR"
url = "https://api.climatiq.io/data/v1/estimate"

#3 different energy scenarios
energy_scenarios = {
    "Single Customer (Actual)": 11568,
    "Single Customer (Baseline)": 1000,
    "Wayne County Total": 17291241000
}

results = {}
#for loop to go through each energy scenario and print out a separate statement
for scenario, energy_kwh in energy_scenarios.items():
    results[scenario] = {}
    for year in range(2020, 2024):  
        json_body = {
            "emission_factor": {
                "activity_id": "electricity-supply_grid-source_supplier_mix-supplier_dte_energy",
                "source": "EEI",
                "region": "US-MI",
                "year": year,
                "source_lca_activity": "electricity_generation",
                "data_version": "^0",
                "allowed_data_quality_flags": [
                    "partial_factor"
                ]
            },
            "parameters": {
                "energy": energy_kwh,
                "energy_unit": "kWh"
            }
        }

        headers = {
            "Authorization": f"Bearer {MY_API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=json_body, headers=headers)

        if response.status_code == 200:
            data = response.json()
            results[scenario][year] = data
            print(f"{scenario} - Year {year} emissions estimate:")
            print(data)
        else:
            print(f"Error for {scenario} year {year}: {response.status_code}")
            print(response.text)

