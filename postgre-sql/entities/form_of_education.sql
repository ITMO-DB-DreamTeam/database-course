-- Table: university.form_of_education

-- DROP TABLE university.form_of_education;

CREATE TABLE university.form_of_education
(
    form_of_education_id bigint NOT NULL DEFAULT nextval('university.form_of_education_form_of_education_id_seq'::regclass),
    name character varying(15) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT form_of_education_pkey PRIMARY KEY (form_of_education_id),
    CONSTRAINT form_of_education_name_key UNIQUE (name)
)

TABLESPACE pg_default;

ALTER TABLE university.form_of_education
    OWNER to postgres;