BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "dutyevent" (
	"id"	INTEGER NOT NULL,
	"duty_type_id"	INTEGER,
	"duty_person_id"	INTEGER,
	"date_time_start"	DATETIME NOT NULL,
	"date_time_stop"	DATETIME NOT NULL,
	"table_date"	DATETIME,
	PRIMARY KEY("id"),
	FOREIGN KEY("duty_person_id") REFERENCES "person"("id"),
	FOREIGN KEY("duty_type_id") REFERENCES "dutytype"("id")
);
CREATE TABLE IF NOT EXISTS "roleperson" (
	"id"	INTEGER NOT NULL,
	"role_id"	INTEGER,
	"person_id"	INTEGER,
	PRIMARY KEY("id"),
	FOREIGN KEY("person_id") REFERENCES "person"("id"),
	FOREIGN KEY("role_id") REFERENCES "role"("id")
);
CREATE TABLE IF NOT EXISTS "dutytype" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR NOT NULL,
	"time_interval_id"	INTEGER,
	"role_id"	INTEGER,
	FOREIGN KEY("time_interval_id") REFERENCES "timeinterval"("id"),
	PRIMARY KEY("id"),
	FOREIGN KEY("role_id") REFERENCES "role"("id")
);
CREATE TABLE IF NOT EXISTS "timeinterval" (
	"id"	INTEGER NOT NULL,
	"time_start"	DATETIME NOT NULL,
	"time_end"	DATETIME NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "role" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "person" (
	"id"	INTEGER NOT NULL,
	"username"	VARCHAR(32) NOT NULL,
	"password"	VARCHAR(128),
	"active"	BOOLEAN NOT NULL,
	"role"	VARCHAR NOT NULL,
	PRIMARY KEY("id"),
	CHECK(active IN (0,1))
);
CREATE TABLE IF NOT EXISTS "alembic_version" (
	"version_num"	VARCHAR(32) NOT NULL,
	CONSTRAINT "alembic_version_pkc" PRIMARY KEY("version_num")
);
INSERT INTO "roleperson" VALUES (1,1,1);
INSERT INTO "roleperson" VALUES (2,2,2);
INSERT INTO "roleperson" VALUES (3,3,3);
INSERT INTO "roleperson" VALUES (4,1,3);
INSERT INTO "dutytype" VALUES (1,'дежурный утро',1,1);
INSERT INTO "dutytype" VALUES (2,'дежурный вечер',2,1);
INSERT INTO "dutytype" VALUES (3,'дежурный старший',3,3);
INSERT INTO "dutytype" VALUES (4,'дежурный по фильтрам',4,2);
INSERT INTO "timeinterval" VALUES (1,'2019-07-26 03:00:00.000000','2019-07-26 15:00:00.000000');
INSERT INTO "timeinterval" VALUES (2,'2019-07-26 15:00:00.000000','2019-07-26 03:00:00.000000');
INSERT INTO "timeinterval" VALUES (3,'2019-07-26 10:00:00.000000','2019-07-26 19:00:00.000000');
INSERT INTO "timeinterval" VALUES (4,'2019-07-26 11:00:00.000000','2019-07-26 20:00:00.000000');
INSERT INTO "role" VALUES (1,'duty');
INSERT INTO "role" VALUES (2,'security');
INSERT INTO "role" VALUES (3,'level up');
INSERT INTO "person" VALUES (1,'admin','pbkdf2:sha256:150000$weahZ411$79c954a6b56afb8e514087770ef561c19f019f3d55925d0b371fc209f3a7a2d7',1,'admin');
INSERT INTO "person" VALUES (2,'Скороходов',NULL,1,'user');
INSERT INTO "person" VALUES (3,'Вельяминов',NULL,1,'user');
INSERT INTO "person" VALUES (4,'Сидоров',NULL,1,'user');
INSERT INTO "person" VALUES (5,'Павлов',NULL,1,'user');
INSERT INTO "person" VALUES (6,'Соколов',NULL,1,'user');
INSERT INTO "alembic_version" VALUES ('51a3a0338e3b');
CREATE UNIQUE INDEX IF NOT EXISTS "ix_person_username" ON "person" (
	"username"
);
COMMIT;
