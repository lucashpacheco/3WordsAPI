USE dbTW
GO

IF OBJECT_ID('dbo.tbLogin', 'U') IS NOT NULL 
  DROP TABLE dbo.tbLogin;

CREATE TABLE tbLogin ( 
"fk_IdUser" int PRIMARY KEY,
"userPassword" varchar(100),
"isActive" bit NOT NULL CONSTRAINT DF__tbLogin__isActive  DEFAULT(0),
"isLogged" bit NOT NULL CONSTRAINT DF__tbLogin__isLogged  DEFAULT(0),
"dt_fisrtLoginDate" datetime,
"dt_lastLoginDate" datetime,
"dt_lastUpdateDate" datetime NOT NULL CONSTRAINT DF__tbLogin__dt_lastUpdateDate  DEFAULT(GETDATE())
);
ALTER TABLE tbLogin
    ADD CONSTRAINT fk_User FOREIGN KEY (fk_IdUser) REFERENCES tbUser (pk_IdUser)



