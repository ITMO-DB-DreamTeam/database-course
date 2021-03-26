DELETE FROM university.university;
ALTER SEQUENCE university.university_university_id_seq RESTART WITH 1;

INSERT INTO university.university(name) VALUES('Национальный исследовательский университет ИТМО');

SELECT * FROM university.university;