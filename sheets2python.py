import pandas as pd

#https://docs.google.com/spreadsheets/d/


# 1yoCokBD5mUzslBu5m_5sGscz3zNLnkWESdRDoVeqzk0/edit?usp=sharing
#1qxKyYOvRVokm0OPeE_pQ-QYxtK57UdXCN983K5DsK-0/edit?usp=sharing
sheet_id='1qxKyYOvRVokm0OPeE_pQ-QYxtK57UdXCN983K5DsK-0'
df=pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
print(df)
