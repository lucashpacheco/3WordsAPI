USE dbTW
GO

CREATE TABLE tbLogin ( 
"fk_IdUser" int identity,
"userPassword" varchar(100),
"isLogged" bit,
"dt_fisrtLoginDate" datetime,
"dt_lastLoginDate" datetime,
"dt_lastUpdateDate" datetime
);

