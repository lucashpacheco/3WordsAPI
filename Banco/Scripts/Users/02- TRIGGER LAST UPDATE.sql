USE dbTW
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
IF EXISTS(SELECT * FROM sys.triggers WHERE object_id = OBJECT_ID(N'[dbo].[trg_lastUpdate_user]'))
BEGIN
    DROP TRIGGER [dbo].[trg_lastUpdate_user]
END
GO
CREATE TRIGGER trg_lastUpdate_user
ON [dbo].tbUser
FOR UPDATE 
AS
BEGIN
    UPDATE [dbo].tbUser
    SET dt_lastUpdateDate = GETDATE()
    WHERE pk_IdUser IN (SELECT DISTINCT pk_IdUser FROM Inserted)

END
GO