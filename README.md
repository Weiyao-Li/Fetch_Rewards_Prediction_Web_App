# Fetch Rewards User Guide

## Overview
Predict the number of scanned receipts for each month in 2022 based on 2021 data.

## Prerequisites
- Python 3.8+
- PyTorch
- Django

## Installation

### Local
1. **Clone Repo**
    ```bash
    git clone git@github.com:Weiyao-Li/Fetch_Rewards_Prediction_Web_App.git

    ```
   You may use PyCharm to open the djangoProject inside for the web app
## Usage Instructions

### Via Web App

1. **Start the Server**
    ```bash
    python manage.py runserver
    ```

2. **Access the Web App**
    - Open your web browser and go to `http://127.0.0.1:8000/`

3. **Make Predictions**
    - Enter the receipt counts for the last three months of 2021.
    - Click on the "Predict" button.

### Via API Endpoint

You can also make predictions using the API as follows:

```bash
curl "http://127.0.0.1:8000/predict/?sequence=<sequence_of_last_three_months>"
```
![image](https://github.com/Weiyao-Li/Fetch_Rewards_Prediction_Web_App/blob/main/webApp.jpg)

