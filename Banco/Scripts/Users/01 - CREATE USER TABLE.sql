USE dbTW
GO

IF OBJECT_ID('dbo.tbUser', 'U') IS NOT NULL 
  DROP TABLE dbo.tbUser;

CREATE TABLE tbUser ( 
"pk_IdUser" int identity,
"userName" varchar(100),
"userSurname" varchar(50),
"userEmail" varchar(50),
"dt_userBithdate" datetime,
"userGender" tinyint,
"userPostalCode" int,
"userCellphone" bigint,
"dt_userRegisterDate" datetime NOT NULL CONSTRAINT DF__tbUser__dt_userRegisterDate DEFAULT(GETDATE()),
"dt_lastUpdateDate" datetime NOT NULL CONSTRAINT DF__tbUser__dt_lastUpdateDate  DEFAULT(GETDATE()),
"isActive" bit
);


