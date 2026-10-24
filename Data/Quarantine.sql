CREATE TABLE QUARANTINE (
    id SERIAL PRIMARY KEY ,
    log_id INTEGER NOT NULL,
    quarantine_reason TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    FOREIGN KEY (log_id) REFERENCES Events(id)
);