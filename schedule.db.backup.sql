BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "alembic_version" (
	"version_num"	VARCHAR(32) NOT NULL,
	CONSTRAINT "alembic_version_pkc" PRIMARY KEY("version_num")
);
CREATE TABLE IF NOT EXISTS "dutyevent" (
	"id"	INTEGER NOT NULL,
	"duty_type_id"	INTEGER,
	"duty_person_id"	INTEGER,
	"date_time_start"	DATETIME NOT NULL,
	"date_time_stop"	DATETIME NOT NULL,
	"date_ym"	VARCHAR NOT NULL,
	"date_ymd"	VARCHAR NOT NULL,
	"table_date"	DATETIME NOT NULL UNIQUE,
	PRIMARY KEY("id"),
	FOREIGN KEY("duty_type_id") REFERENCES "dutytype"("id"),
	FOREIGN KEY("duty_person_id") REFERENCES "person"("id")
);
CREATE TABLE IF NOT EXISTS "roleperson" (
	"id"	INTEGER NOT NULL,
	"role_id"	INTEGER,
	"person_id"	INTEGER,
	PRIMARY KEY("id"),
	FOREIGN KEY("role_id") REFERENCES "role"("id"),
	FOREIGN KEY("person_id") REFERENCES "person"("id")
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
CREATE TABLE IF NOT EXISTS "person" (
	"id"	INTEGER NOT NULL,
	"username"	VARCHAR(32) NOT NULL,
	"password"	VARCHAR(128),
	"active"	BOOLEAN NOT NULL,
	"role"	VARCHAR NOT NULL,
	PRIMARY KEY("id"),
	CHECK(active IN (0,1))
);
CREATE TABLE IF NOT EXISTS "role" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "timeinterval" (
	"id"	INTEGER NOT NULL,
	"time_start"	DATETIME NOT NULL,
	"time_end"	DATETIME NOT NULL,
	PRIMARY KEY("id")
);
INSERT INTO "dutyevent" VALUES (1,1,2,'2019-07-14 03:00:00.000000','2019-07-14 15:00:00.000000','2019-07','2019-07-14','2019-07-14 00:00:00.000000');
INSERT INTO "dutyevent" VALUES (2,2,3,'2019-07-15 03:00:00.000000','2019-07-15 03:00:00.000000','2019-07','2019-07-15','2019-07-15 03:00:00.000000');
INSERT INTO "dutyevent" VALUES (3,3,4,'2019-08-14 03:00:00.000000','2019-08-14 15:00:00.000000','2019-08','2019-08-14','2019-08-14 10:00:00.000400');
INSERT INTO "dutyevent" VALUES (4,2,4,'2019-07-14 10:00:00.000000','2019-07-14 19:00:00.000000','2019-07','2019-07-14','2019-07-14 10:00:00.000001');
INSERT INTO "dutyevent" VALUES (5,3,5,'2019-07-14 19:00:00.000000','2019-07-14 19:00:00.000000','2019-07','2019-07-14','2019-07-14 19:00:00.0000022');
INSERT INTO "dutytype" VALUES (1,'деж1',1,1);
INSERT INTO "dutytype" VALUES (2,'деж2',1,1);
INSERT INTO "dutytype" VALUES (3,'деж3',2,2);
INSERT INTO "dutytype" VALUES (4,'деж4',2,2);
INSERT INTO "dutytype" VALUES (1000,'empty duty',NULL,NULL);
INSERT INTO "person" VALUES (1,'admin','pbkdf2:sha256:150000$weahZ411$79c954a6b56afb8e514087770ef561c19f019f3d55925d0b371fc209f3a7a2d7',1,'admin');
INSERT INTO "person" VALUES (2,'евдокимов',NULL,1,'user');
INSERT INTO "person" VALUES (3,'скороходов',NULL,1,'user');
INSERT INTO "person" VALUES (4,'потапов',NULL,1,'user');
INSERT INTO "person" VALUES (5,'филатов',NULL,1,'user');
INSERT INTO "person" VALUES (1000,'empty',NULL,0,'user');
INSERT INTO "role" VALUES (1,'role1');
INSERT INTO "role" VALUES (2,'role2');
INSERT INTO "timeinterval" VALUES (1,'2019-07-14 15:00:00.000000','2019-07-14 15:00:00.000000');
INSERT INTO "timeinterval" VALUES (2,'2019-07-14 15:00:00.000000','2019-07-14 15:00:00.000000');
CREATE UNIQUE INDEX IF NOT EXISTS "ix_person_username" ON "person" (
	"username"
);
COMMIT;
