# Galiboo front
Simple app to test [Galiboo](galiboo.com) API
## Setup front
```
cd front
npm install
npm run dev
```

## Setup back

> setup virtualenv with python3

> create `.env` file like so: `server/myapp/.env` and place your Galiboo API key
> GALIBOO_KEY=\<YOUR-GALIBOO-KEY-HERE>

> _optional_ in `.env` YOUTUBE_KEY=\<YOUR-YOUTUBE-KEY-HERE>

> See .envExample for clearer understanding
```
cd server
pip install -r requirements.txt
python run.py
```

Server is serving request on port 5000

Front is serving on port 3000

---
_Ether tips are warmly welcomed:_ `0x5e58ae8b59fe9ef291c9bb6ae20af5a8583c71a2`