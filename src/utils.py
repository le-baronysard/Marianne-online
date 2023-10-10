import pandas as pd
# ['Transaction Name', 'Transaction Name URL', 'Organization Industries',
#        'Organization Location', 'Organization Name', 'Organization Name URL',
#        'Funding Type', 'Money Raised', 'Money Raised Currency',
#        'Money Raised Currency (in USD)', 'Announced Date', 'Funding Stage',
#        'Organization Description', 'Total Funding Amount',
#        'Total Funding Amount Currency',
#        'Total Funding Amount Currency (in USD)', 'Number of Funding Rounds',
#        'Funding Status', 'Organization Revenue Range', 'Lead Investors',
#        'Organization Website', 'Investor Names', 'Number of Investors',
#        'Pre-Money Valuation', 'Pre-Money Valuation Currency',
#        'Pre-Money Valuation Currency (in USD)', 'Equity Only Funding']


def convert_devise(data:pd.DataFrame):
    rate = { "USD":0.93
            ,"GBP":1.17
            ,"AUD":0.61
            ,"CHF":1.04
    }
    for idx,row in  data.iterrows():
        if row["Money Raised Currency"] != "EUR":
            data.loc[idx,"Raised"] = row["Raised"] * rate[row["Money Raised Currency"]]
            data.loc[idx,"Money Raised Currency"] = "EUR"

def load_data(filter:list=None):
    data = pd.read_csv("data/funding-round-total.csv", index_col=0)
    data.dropna(subset=["Raised"],inplace=True)
    data["Raised"] = data["Raised"]/1_000_000
    convert_devise(data)
    data.rename(columns={"Total_usd":"Total raised ($)"
                ,"Raised":"Raised (million €)"}, inplace=True)
    data.drop(columns=["Money Raised Currency (in USD)","Money Raised Currency"], inplace=True)
    data.sort_values(by="Organization Name", ascending=True, inplace=True)
    print(data.columns)
    data.reset_index(inplace=True,drop=True)
    data["Date"] = pd.to_datetime(data["Date"])
    if not filter is None:
        data = data.loc[:,filter]
    # data = data.loc[:,[
    #                     "Date"
    #                     ,"Organization Name"
    #                     ,"Raised (million)"
    #                     ,"Money Raised Currency"
    #                     , "Transaction Name"
    #                     ,"Total_usd"
    #                     ,"Status"
    #                     ,"Type"
    #                     ,"Organization Industries"
    #                     ,"Organization Location"
    #                     ,"Investor Names"]]
    return data
