CREATE TABLE EVENTS (
    id SERIAL PRIMARY KEY,
    service_name TEXT NOT NULL,
    level TEXT NOT NULL,
    message TEXT NOT NULL,
    timestamp TEXT NOT NULL
);