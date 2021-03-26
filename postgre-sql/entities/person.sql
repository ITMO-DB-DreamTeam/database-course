-- Table: university.person

-- DROP TABLE university.person;

CREATE TABLE university.person
(
    person_id bigint NOT NULL DEFAULT nextval('university.person_person_id_seq'::regclass),
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT person_pkey PRIMARY KEY (person_id),
    CONSTRAINT person_name_key UNIQUE (name)
)

TABLESPACE pg_default;

ALTER TABLE university.person
    OWNER to postgres;