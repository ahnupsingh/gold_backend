# SaveZ backend design

### DB schemas

- BaseModel

  - created_at: date
  - updated_at: date
  - deleted_at: date
  - is_deleted: bool

- User

  - mobile
  - name
  - age | dob
  - validated_on
  - avatar | image ?
  - total_rewards: 34.82 // in INR
  - user_id

- Subscription

  - user_id
  - amount: 100.0
  - frequency: DAILY | WEEKLY | MONTHLY,
  - auto_renewal

- UpiWallets

  - user_id
  - paytmSsoToken ?

- Locker

  - quantity: 88.1 // in mg
  - amount:
  - asset: 24K | 99.5% Pure Gold

- LockerHistory

  - quantity: 8.1 // in mg
  - amount: 12.43 // in $ or INR
  - asset: 24K | 99.5% Pure Gold
  - debit: 0.00
  - credit: 0.00
  - order_id:

- Order

  - order_id: uuid
  - amount: 100.0
  - type: SUBSCRIPTION | BUY | SELL ?
  - status: INITIATED | IN PROGRESS | CANCELLED | SUCCESS | FAILED
  - placed_on: timestamp
  - subscription_id:

- Offers

  - code : uuid
  - amount
  - streak: 7 // in days
  - status: active | inactive
  - starts_on: date
  - ends_on: date

- Transaction

  - order_id:
  - token: uuid // need to pass this to paytm
  - status: IN PROGRESS | SUCCESS | FAILED | REFUNDED
  - transaction_date: timestamp

- Cache

  - gold_buy_price [expiry: 2 min ?]
  - gold_sell_price [expiry: 2 min ?]

- Rewards

  - user_id:
  - amount:

- EarnedPoints

  - user_id:
  - challenge_id:
  - points:
  - created_on:

- Notification

### Entity Relationships

- An order can have multiple transactions

### User API

LOGIN

- POST /login
- POST /validate

PROFILE

- GET /profile
- PUT /profile

HOMEPAGE

- GET /gold
  - Gets current buy/sell price
- POST /mandate
  - Creates an order entry with status = INITIATED
- POST /invest

WEBHOOK

- POST /upi/callback // for handling callback from UPI

OFFERS

- GET /offers/active
- POST /offers/claim

## Functionalities

DASHBOARD

- Total investment amount made in last month

UPI

- Request payment process

  - Generate request Checksum, transaction

- On sucessfull payment
  - Create a subscription
  -

### Onboarding

- User should be able to
  - login using mobile number
  - validate his phone using otp
  - update his profile (name/age)

### Homepage

- User should be able to

  - view his profile
  - view current gold buy price
  - view total investment amount made in last month
  - view active challenge
  - view active offer
  - claim reward

  - view gold in his locker
  - total rewards in his profile
  - invest on gold

### Setup UPI

- User should be able to
  - setup UPI mandate

### Environments/Secrets

PAYMENT

- clientId, version, channelId, websiteName
-
