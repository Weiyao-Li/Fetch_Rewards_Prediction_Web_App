from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import torch
from .ml_model import model  # Make sure your model is loaded this way
# Function to render index.html
def index(request):
    return render(request, 'index.html')

# Constants for scaling
min_receipt = 220033460
max_receipt = 309948684

# Function to render index.html
def index(request):
    return render(request, 'index.html')

# Function to handle prediction
@csrf_exempt
def predict(request):
    if request.method == 'GET':
        sequence = request.GET.get('sequence')
        if sequence:
            # First, scale the input sequence
            last_three_months_2021 = list(map(float, sequence.split(',')))
            last_three_months_2021_scaled = [(x - min_receipt) / (max_receipt - min_receipt) for x in last_three_months_2021]

            # Initialize an empty list to store forecasts for 2022
            forecasts_2022 = []

            for i in range(12):  # Loop through each month in 2022
                if i == 0:
                    input_data = last_three_months_2021_scaled  # For January
                elif i == 1:
                    input_data = [last_three_months_2021_scaled[1], last_three_months_2021_scaled[2], forecasts_2022[-1]]  # For February
                elif i == 2:
                    input_data = [last_three_months_2021_scaled[2], forecasts_2022[-2], forecasts_2022[-1]]  # For March
                else:
                    input_data = forecasts_2022[-3:]  # For the rest of the months

                # Convert input_data to a suitable format for the model
                input_tensor = torch.FloatTensor(input_data).view(1, -1, 1)

                # Make a prediction
                with torch.no_grad():
                    output = model(input_tensor).item()

                # Append the raw (scaled) forecast to the list
                forecasts_2022.append(output)

            # Convert all forecasts back to original scale
            forecasts_2022 = [(x * (max_receipt - min_receipt)) + min_receipt for x in forecasts_2022]

            return JsonResponse({"predictions": forecasts_2022})
        else:
            return JsonResponse({"error": "No sequence provided"}, status=400)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
