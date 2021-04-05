class ResponseModel(object):
    """Response Model returns the response in the pattern of API response"""
    status:int
    message:str
    response:object
    
    def __init__(self , status , message , response):
        self.status = status
        self.message = message
        self.response = response
   


