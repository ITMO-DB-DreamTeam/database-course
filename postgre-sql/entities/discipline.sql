-- Table: university.discipline

-- DROP TABLE university.discipline;

CREATE TABLE university.discipline
(
    discipline_id bigint NOT NULL DEFAULT nextval('university.discipline_discipline_id_seq'::regclass),
    name character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT discipline_pkey PRIMARY KEY (discipline_id),
    CONSTRAINT discipline_name_key UNIQUE (name)
)

TABLESPACE pg_default;

ALTER TABLE university.discipline
    OWNER to postgres;