import pandas as pd


Data = [

{
    "name": "Alice Johnson",
    "age": 28,
    "email": "alice.johnson@example.com",
    "phone": "+1-555-1234",
    "city": "San Francisco",
    "occupation": "Software Engineer"
},
{
    "name": "Michael Chen",
    "age": 35,
    "email": "michael.chen@example.com",
    "phone": "+1-555-5678",
    "city": "New York",
    "occupation": "Data Scientist"
},
{
    "name": "Sophie Brown",
    "age": 22,
    "email": "sophie.brown@example.com",
    "phone": "+1-555-9876",
    "city": "Austin",
    "occupation": "Marketing Specialist"
}

]






pd.DataFrame(Data)

Data.to_csv("data/data.csv")