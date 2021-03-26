-- Table: university.faculty_specialty

-- DROP TABLE university.faculty_specialty;

CREATE TABLE university.faculty_specialty
(
    faculty_specialty_id bigint NOT NULL DEFAULT nextval('university.faculty_specialty_faculty_specialty_id_seq'::regclass),
    faculty_fid bigint NOT NULL,
    specialty_fid bigint NOT NULL,
    CONSTRAINT faculty_specialty_pkey PRIMARY KEY (faculty_specialty_id),
    CONSTRAINT faculty_specialty_faculty_fid_specialty_fid_key UNIQUE (faculty_fid, specialty_fid),
    CONSTRAINT faculty_id_too_faculty_specialty FOREIGN KEY (faculty_fid)
        REFERENCES university.faculty (faculty_id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT specialty_id_too_faculty_specialty FOREIGN KEY (specialty_fid)
        REFERENCES university.specialty (specialty_id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE university.faculty_specialty
    OWNER to postgres;