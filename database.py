from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://qwo8eeovdjhknibb3xih:pscale_pw_wo20sU2pgV1TJtCTzrt9clBb4qCOtWoGKU0OaNJY527@eu-central.connect.psdb.cloud/ulascareers?charset=utf8mb4", 
connect_args={
    "ssl": {
        "ca": "/etc/ssl/cert.pem",
    }
})

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    all_result = result.all()
    print("type of result:" + str(type(result)))
    print("type of all results:" + str(type(all_result)))
    print("type of first elem in results:" + str(type(all_result[0])))
    firstresult = all_result[0]
    first_resultDict = firstresult._mapping
    print(first_resultDict)