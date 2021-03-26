-- Table: university.specialty_discipline

-- DROP TABLE university.specialty_discipline;

CREATE TABLE university.specialty_discipline
(
    specialty_discipline_id bigint NOT NULL DEFAULT nextval('university.specialty_discipline_specialty_discipline_id_seq'::regclass),
    specialty_fid bigint NOT NULL,
    discipline_fid bigint NOT NULL,
    form_of_education_fid bigint NOT NULL,
    teacher_fid bigint NOT NULL,
    lecture_hours smallint NOT NULL,
    laboratory_hours smallint NOT NULL,
    practical_hours smallint NOT NULL,
    date_of_scoring date NOT NULL,
    CONSTRAINT specialty_discipline_pkey PRIMARY KEY (specialty_discipline_id),
    CONSTRAINT specialty_discipline_specialty_fid_discipline_fid_form_of_e_key UNIQUE (specialty_fid, discipline_fid, form_of_education_fid, teacher_fid, lecture_hours, laboratory_hours, practical_hours, date_of_scoring),
    CONSTRAINT discipline_id_too_specialty_discipline FOREIGN KEY (discipline_fid)
        REFERENCES university.discipline (discipline_id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT form_of_education_id_too_specialty_discipline FOREIGN KEY (form_of_education_fid)
        REFERENCES university.form_of_education (form_of_education_id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT specialty_id_too_specialty_discipline FOREIGN KEY (specialty_fid)
        REFERENCES university.specialty (specialty_id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    CONSTRAINT teacher_id_too_specialty_discipline FOREIGN KEY (teacher_fid)
        REFERENCES university.teacher (teacher_id) MATCH SIMPLE
        ON UPDATE CASCADE
        ON DELETE CASCADE
)

TABLESPACE pg_default;

ALTER TABLE university.specialty_discipline
    OWNER to postgres;