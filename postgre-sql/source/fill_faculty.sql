DELETE FROM university.faculty;
ALTER SEQUENCE university.faculty_faculty_id_seq RESTART WITH 1;

INSERT INTO university.faculty(university_fid, name) VALUES (1, 'Факультет информационных технологий и программирования');
INSERT INTO university.faculty(university_fid, name) VALUES (1, 'Факультет систем управления и робототехники');
INSERT INTO university.faculty(university_fid, name) VALUES (1, 'Высшая школа цифровой культуры');
INSERT INTO university.faculty(university_fid, name) VALUES (1, 'Факультет цифровых трансформаций');
INSERT INTO university.faculty(university_fid, name) VALUES (1, 'Институт дизайна и урбанистики');
INSERT INTO university.faculty(university_fid, name) VALUES (1, 'Факультет программной инженерии и компьютерной техники');
INSERT INTO university.faculty(university_fid, name) VALUES (1, 'Факультет инфокоммуникационных технологий');
INSERT INTO university.faculty(university_fid, name) VALUES (1, 'Факультет безопасности информационных технологий');
INSERT INTO university.faculty(university_fid, name) VALUES (1, 'Факультет прикладной оптики');
INSERT INTO university.faculty(university_fid, name) VALUES (1, 'Факультет фотоники и оптоинформатики');
INSERT INTO university.faculty(university_fid, name) VALUES (1, 'Физико-технический факультет');
INSERT INTO university.faculty(university_fid, name) VALUES (1, 'Факультет лазерной фотоники и оптоэлектроники ');
INSERT INTO university.faculty(university_fid, name) VALUES (1, 'Факультет энергетики и экотехнологий');
INSERT INTO university.faculty(university_fid, name) VALUES (1, 'Факультет биотехнологий');
INSERT INTO university.faculty(university_fid, name) VALUES (1, 'Научно-образовательный центр инфохимии ');
INSERT INTO university.faculty(university_fid, name) VALUES (1, 'Химико-биологический кластер');
INSERT INTO university.faculty(university_fid, name) VALUES (1, 'Факультет технологического менеджмента и инноваций');
INSERT INTO university.faculty(university_fid, name) VALUES (1, 'Институт международного развития и партнерства');

SELECT * FROM university.faculty;