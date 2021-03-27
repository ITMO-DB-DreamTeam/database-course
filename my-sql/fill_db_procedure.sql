DELIMITER $$
CREATE DEFINER=`root`@`%` PROCEDURE `generateRandomData`(IN `NumRows` INT)
    NO SQL
BEGIN
	DECLARE i INT;
	DECLARE j INT;
	DECLARE n INT;
	DECLARE m INT;
	
	# fill books
	SET i = 1;
	START TRANSACTION;
		WHILE i <= NumRows DO
			INSERT INTO book (name) VALUES (CONCAT('book_',i));
			SET i = i + 1;
		END WHILE;
	COMMIT;
	
	# fill users
	SET i = 1;
	START TRANSACTION;
        WHILE i <= NumRows DO
            INSERT INTO user (fio, position_id) VALUES (CONCAT('fio_',i), FLOOR(1+RAND()*3));
            SET i = i + 1;
        END WHILE;
    COMMIT;
	
	#fill conferences
	SET i = 1;
	START TRANSACTION;
        WHILE i <= NumRows DO
            INSERT INTO conference (name, place, started) VALUES (CONCAT('conference_',i), CONCAT('place_',FLOOR(1+RAND()*100)), FROM_UNIXTIME(UNIX_TIMESTAMP('2010-01-01 00:00:01') + FLOOR(0 + RAND() * 378432000)));
            SET i = i + 1;
        END WHILE;
    COMMIT;
	
	#fill conferences_members
	SET i = 1;
	START TRANSACTION;
        WHILE i <= NumRows DO
			SET n = FLOOR(RAND()*(50)+1);
			SET j = 1;
				WHILE j <= n DO
					INSERT INTO conference_member (conference_id, user_id) VALUES (i, FLOOR(1+RAND()*NumRows));
					SET j = j + 1;
				END WHILE;
			SET i = i + 1;
        END WHILE;
    COMMIT;
	
	#fill edition
	SET i = 1;
	START TRANSACTION;
        WHILE i <= NumRows DO
			SET n = FLOOR(1+RAND()*500);
			INSERT INTO edition (name, volume, type_id, place_id, lang_id) VALUES (CONCAT('edition_',i), n, FLOOR(1+RAND()*2), FLOOR(1+RAND()*2), FLOOR(1+RAND()*2));
			SET i = i + 1;
        END WHILE;
    COMMIT;
	
	#fill library_card
	SET i = 1;
	START TRANSACTION;
        WHILE i <= NumRows DO
			SET j = UNIX_TIMESTAMP('2010-01-01 00:00:01') + FLOOR(0 + RAND() * 346896000);
			SET n = j+FLOOR(0 + RAND() * 7776000);
			INSERT INTO library_card (user_id, book_id, tooked, returned) VALUES (FLOOR(1+RAND()*NumRows), FLOOR(1+RAND()*NumRows), FROM_UNIXTIME(j), FROM_UNIXTIME(n));
			SET i = i + 1;
        END WHILE;
    COMMIT;
	
	# fill projects
	SET i = 1;
	START TRANSACTION;
		WHILE i <= NumRows DO
			INSERT INTO project (name) VALUES (CONCAT('project_',i));
			SET i = i + 1;
		END WHILE;
	COMMIT;
	
	#fill project_members
	SET i = 1;
	START TRANSACTION;
        WHILE i <= NumRows DO
			SET n = FLOOR(RAND()*(5)+1);
			SET j = 1;
				WHILE j <= n DO
					SET m = UNIX_TIMESTAMP('2010-01-01 00:00:01') + FLOOR(0 + RAND() * 315360000);
					INSERT INTO project_member (project_id, user_id, started, ended) VALUES (i, FLOOR(1+RAND()*NumRows), FROM_UNIXTIME(m), FROM_UNIXTIME(m+FLOOR(0 + RAND() * 31536000)));
					SET j = j + 1;
				END WHILE;
			SET i = i + 1;
        END WHILE;
    COMMIT;
	
	#fill publication
	SET i = 1;
	START TRANSACTION;
        WHILE i <= NumRows DO
			SET n = FLOOR(1+RAND()*50);
			INSERT INTO publication (name, type_id, user_id, edition_id, citation, published) VALUES (CONCAT('publication_',i), FLOOR(1+RAND()*2), FLOOR(1+RAND()*NumRows), FLOOR(1+RAND()*NumRows), n, FROM_UNIXTIME(UNIX_TIMESTAMP('2010-01-01 00:00:01') + FLOOR(0 + RAND() * 346896000)));
			SET i = i + 1;
        END WHILE;
    COMMIT;
	
	#fill publication_co-authors
	SET i = 1;
	START TRANSACTION;
        WHILE i <= NumRows DO
			SET n = FLOOR(RAND()*(5)+1);
			SET j = 1;
				WHILE j <= n DO
					INSERT INTO `publication_co-authors` (publication_id, user_id) VALUES (i, FLOOR(1+RAND()*NumRows));
					SET j = j + 1;
				END WHILE;
			SET i = i + 1;
        END WHILE;
    COMMIT;
END$$
DELIMITER ;