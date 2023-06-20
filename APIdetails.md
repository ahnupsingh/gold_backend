### GET /profile

`json
{
"total_investment": 0.00,
"total_investment_last_month": 0.00,
"last_invested_on": "2023-01-01",
"locker": {
"quantity": 88.1,
"amount": 121.43, # ?
"asset": "24K | 99.5% Pure Gold",
"currency": "$"
}
"total_rewards": 34.82
}
`

### GET /gold

`json
{
"current_buy_price": 0.00,
"current_sell_price": 0.00,
}

### POST /invest

`json
{
"current_buy_price": 0.00,
"current_sell_price": 0.00,
}

### POST /mandate

`json
{
"amount": 0.00,
"frequency": "DAILY" | "WEEKLY" | "MONTHLY",
"upi_id": "7762933208@ybl"
}
