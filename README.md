# Unofficial Codeforces API

## Start

1. Install dependencies `pip install -r requirements.txt`
2. Run `uvicorn main:app --reload`


## Routes

* `/problems`: Get info problem. Query Parameters: contest_id, id. for example: `/problems?contest_id=1805&id=A`
