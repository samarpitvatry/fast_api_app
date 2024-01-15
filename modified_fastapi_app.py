from fastapi import FastAPI, HTTPException
from typing import List, Optional
import pandas as pd

# Initialize FastAPI app
app = FastAPI()

# Load the data from the provided CSV files
account_details_df = pd.read_csv("data/account_details.csv")
invoice_details_df = pd.read_csv("data/invoice_details.csv")

# Endpoint 1: Fetch list of account_num and account_name
@app.get("/account/list", response_model=List[dict])
async def list_accounts():
    accounts = account_details_df[["account_num", "account_name"]].to_dict(orient='records')
    return accounts

# Endpoint 2: Get full account details
@app.get("/account/details/{account_num}", response_model=dict)
async def get_account_details(account_num: str):
    account_data = account_details_df[account_details_df["account_num"] == account_num].to_dict(orient='records')
    if account_data:
        return account_data[0]
    else:
        raise HTTPException(status_code=404, detail="Account details not found")

# Endpoint 3: Get invoice details
@app.get("/invoice/details/{account_num}", response_model=List[dict])
async def get_invoice_details(account_num: str):
    invoice_data = invoice_details_df[invoice_details_df["account_num"] == account_num].to_dict(orient='records')
    if invoice_data:
        return invoice_data
    else:
        raise HTTPException(status_code=404, detail="Invoice details not found")

# Endpoint 4: Search accounts
@app.get("/account/search", response_model=List[dict])
async def search_accounts_endpoint(query: Optional[str] = ''):
    filtered_accounts = account_details_df[
        account_details_df["account_num"].str.contains(query, case=False) |
        account_details_df["account_name"].str.contains(query, case=False)
    ][["account_num", "account_name"]].to_dict(orient='records')
    return filtered_accounts
