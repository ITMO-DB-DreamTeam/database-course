-- Table: university.faculty

-- DROP TABLE university.faculty;

CREATE TABLE university.faculty
(
    faculty_id bigint NOT NULL DEFAULT nextval('university.faculty_faculty_id_seq'::regclass),
    university_fid bigint NOT NULL,
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT faculty_pkey PRIMARY KEY (faculty_id),
    CONSTRAINT faculty_university_fid_name_key UNIQUE (university_fid, name),
    CONSTRAINT university_id_too_faculty FOREIGN KEY (university_fid)
        REFERENCES university.university (university_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE university.faculty
    OWNER to postgres;