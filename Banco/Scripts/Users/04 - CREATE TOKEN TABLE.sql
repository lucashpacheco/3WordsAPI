USE dbTW
GO

IF OBJECT_ID('dbo.tbToken', 'U') IS NOT NULL 
  DROP TABLE dbo.tbToken;

CREATE TABLE tbToken ( 
"fk_IdUser" int PRIMARY KEY,
"emailToken" int,
"dt_emailTokenExprirated" datetime NOT NULL CONSTRAINT DF__tbToken__dt_emailTokenExprirated DEFAULT(DATEADD(minute, 3, GETDATE())),
"dt_lastUpdateDate" datetime NOT NULL CONSTRAINT DF__tbToken__dt_lastUpdateDate  DEFAULT(GETDATE())
);
ALTER TABLE tbToken
    ADD CONSTRAINT fk_User_Token FOREIGN KEY (fk_IdUser) REFERENCES tbUser (pk_IdUser)
