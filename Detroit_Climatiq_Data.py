import requests
#this is my range of years script
MY_API_KEY = "797W289MNH3FD9SET8YJ025MYR"

url = "https://api.climatiq.io/data/v1/estimate"

results = {}

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
            "energy": 1000, #this is based on the data of the average electricity consumer in Detroit MONTHLY
            "energy_unit": "kWh"
        }
    }

    headers = {
        "Authorization": f"Bearer 797W289MNH3FD9SET8YJ025MYR",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=json_body, headers=headers)

    if response.status_code == 200:
        data = response.json()
        results[year] = data
        print(f"Year {year} emissions estimate:")
        print(data)
    else:
        print(f"Error for year {year}: {response.status_code}")
        print(response.text)
