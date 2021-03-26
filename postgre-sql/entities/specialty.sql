-- Table: university.specialty

-- DROP TABLE university.specialty;

CREATE TABLE university.specialty
(
    specialty_id bigint NOT NULL DEFAULT nextval('university.specialty_specialty_id_seq'::regclass),
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT specialty_pkey PRIMARY KEY (specialty_id),
    CONSTRAINT specialty_name_key UNIQUE (name)
)

TABLESPACE pg_default;

ALTER TABLE university.specialty
    OWNER to postgres;