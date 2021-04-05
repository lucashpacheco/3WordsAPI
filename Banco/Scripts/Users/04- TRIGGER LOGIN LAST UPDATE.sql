
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TRIGGER trg_lastUpdate_login
ON [dbo].tbLogin
AFTER UPDATE
AS
BEGIN
    UPDATE [dbo].tbUser
    SET dt_lastUpdateDate = GETDATE()
    WHERE pk_IdUser IN (SELECT DISTINCT pk_IdUser FROM Inserted)

END
GO