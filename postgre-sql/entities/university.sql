-- Table: university.university

-- DROP TABLE university.university;

CREATE TABLE university.university
(
    university_id bigint NOT NULL DEFAULT nextval('university.university_university_id_seq'::regclass),
    name character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT university_pkey PRIMARY KEY (university_id),
    CONSTRAINT university_name_key UNIQUE (name)
)

TABLESPACE pg_default;

ALTER TABLE university.university
    OWNER to postgres;