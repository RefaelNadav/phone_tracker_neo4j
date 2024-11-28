
## Phone Tracker



### הוראות התקנה
1. שכפול המאגר:
```bash
git clone https://github.com/RefaelNadav/phone_tracker_neo4j.git
cd phone_tracker_neo4j
```

2. יצירת סביבת Python:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# או
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

3. הפעלת neo4j:
```bash
docker-compose up -d
```

### מבנה המערכת
המערכת מורכבת משלושה שירותים עיקריים:

1. **Insert Calls Service** 
   - הכנסת שיחות טלפון

2. **Analysis Service** 
   - הנתיב הארוך שמקושר עם בלוטות
   - אות חזק יותר מ -60
   - מספר המכשירים שמקושרים למכשיר
   - האם שני מכשירים מקושרים
   - השיחה האחרונה של המכשיר


### API Endpoints

#### Insert calls Service
```
POST /api/phone_tracker
```

#### Analysis Service
```
GET /api/analysis/bluetooth
GET /api/analysis/strength_dbm
GET /api/analysis/count_connected/<device_id>
GET /api/analysis/is_connected/<device_id1>/<device_id2>
GET /api/analysis/last_interaction/<device_id>
```

