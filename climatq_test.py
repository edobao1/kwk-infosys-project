import requests
#this whole thing can also be done as a curl request by I don't want that

url = "https://api.climatiq.io/data/v1/estimate" #this is the base url for Climatiq
#the API endpoint that's used to estimate how intensive an activity is, right above
headers = {
    "Authorization": "Bearer 797W289MNH3FD9SET8YJ025MYR", #my API key is right after Bearer
    "Content-Type": "application/json"
}
payload = {
    "emission_factor": {
        "activity_id": "electricity-supply_grid-source_residual_mix", #this is the emission factor
        "data_version": "^21"
    },
    "parameters": {
        "energy": 4200,
        "energy_unit": "kWh"
    }
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())

#response output: {'co2e': 3763.0, 'co2e_unit': 'kg',