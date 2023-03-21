from sqlalchemy import create_engine, text
import os
engine = create_engine(os.getenv('enginekey'), 
connect_args={
    "ssl": {
        "ca": "/etc/ssl/cert.pem",
    }
})

def load_jobs_fromDB():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._mapping)
    return jobs