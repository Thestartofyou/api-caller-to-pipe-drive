import requests
import matplotlib.pyplot as plt

# Define API endpoint and parameters
api_endpoint = 'https://example.com/api'
lead_id = '12345'
api_key = 'your_api_key'

# Function to call API based on number of calls made
def call_api(num_calls):
    headers = {'Authorization': f'Bearer {api_key}'}
    params = {'lead_id': lead_id, 'num_calls': num_calls}
    response = requests.get(api_endpoint, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f'Failed to call API. Status code: {response.status_code}')
        return None

# Define number of calls made to the lead
num_calls_list = [5, 10, 15, 20]  # Example values

# Call API for each number of calls and store success data
success_data = []
for num_calls in num_calls_list:
    data = call_api(num_calls)
    if data:
        success_data.append(data['success_rate'])

# Plot success data
plt.plot(num_calls_list, success_data, marker='o')
plt.xlabel('Number of Calls')
plt.ylabel('Success Rate')
plt.title('Success Rate vs. Number of Calls to Lead')
plt.grid(True)
plt.show()

