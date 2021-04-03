USE dbTW
GO

CREATE TABLE tbWord ( 
"pk_IdWord" int identity,
"word" varchar(80),
"wordSubject" tinyint,
"wordDefinition" varchar(500),
"dt_insertDate" datetime,
"dt_lastUpdateDate" datetime
);

