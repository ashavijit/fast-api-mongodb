from fastapi import status, HTTPException

def GetResponse(done : bool , errorMessage : str):
    if done:
        return {"message": "Success"}
    else:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=errorMessage
        )
async def riseHTTPExceptionIfNotFound(result , message:str):
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )