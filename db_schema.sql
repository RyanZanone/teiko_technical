CREATE TABLE Subjects (
    subject_id TEXT PRIMARY KEY,
    project TEXT,
    condition TEXT,
    age INTEGER,
    sex TEXT
);

CREATE TABLE Samples (
    sample_id TEXT PRIMARY KEY,
    subject_id TEXT,
    sample_type TEXT,
    time_from_treatment_start INTEGER,
    treatment TEXT,
    response TEXT,
    FOREIGN KEY(subject_id) REFERENCES Subjects(subject_id)
);

CREATE TABLE CellCounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sample_id TEXT,
    population TEXT,
    count INTEGER,
    FOREIGN KEY(sample_id) REFERENCES Samples(sample_id)
);