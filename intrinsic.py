import azure.functions as func
import yfinance as yf
from azure.storage.blob import BlobServiceClient
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    #fetch data
    ticker = req.params.get('ticker')
    stock = yf.Ticker(ticker)
    cash_flow = stock.cashflow.to_json()
    
    #Save to Blob Storage
    connection_string = os.environ["AzureWebJobsStorage"]
    blob_service = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service.get_blob_client(containers="financial-data",blob=f"{ticker} _cashflow.json")
    blob_client.upload_blob(cash_flow,overwrite=True) 

    return func.HttpResponse(f"Data for {ticker} uploaded!")