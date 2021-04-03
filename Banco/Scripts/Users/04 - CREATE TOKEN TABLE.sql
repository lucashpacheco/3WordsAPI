USE dbTW
GO

CREATE TABLE tbToken ( 
"fk_IdUser" int identity,
"emailToken" smallint,
"dt_emailTokenExprirated" bit,
"dt_lastUpdateDate" datetime
);
