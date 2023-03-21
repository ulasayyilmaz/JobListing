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

def load_job_from_DB(id):
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs where id = :val"), val = id)
        row = result.all()
        if len(row) == 0:
            return None
        else:
            return row[0]._mapping