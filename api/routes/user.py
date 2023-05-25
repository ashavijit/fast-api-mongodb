from bson import ObjectId
from fastapi import status ,File, UploadFile, APIRouter
from api.models.users import CreateUser
from api.routes.constantHTTP import GetResponse , riseHTTPExceptionIfNotFound
from api.utils.savepic import save_pic
from api.services import userServices as service


userRoutes = APIRouter()
base = "/user"
UploadImage = f"{base}/uploadImage"
_notFoundMessage = "Could not find user with the given Id."

@userRoutes.get(base)
async def getAllUser():
    return service.getAllUser()

@userRoutes.get(base+'{id}')
async def getById(id):
    return await resultVerification(id)   
  

@userRoutes.post(base)
async def InsertUser(data: CreateUser):
    return await service.InsertUser(data)


@userRoutes.put(base+'{id}', status_code=status.HTTP_204_NO_CONTENT)
async def updateUser(id, data: CreateUser):
    await resultVerification(id)
    done : bool = await service.updateUser(id,data);
    return GetResponse(done, errorMessage="An error occurred while editing the user information.")


@userRoutes.delete(base+'{id}', status_code=status.HTTP_204_NO_CONTENT)
async def deleteUser(id):
    await resultVerification(id)
    done : bool = await service.deleteUser(id);
    return GetResponse(done, errorMessage="There was an error.")   


@userRoutes.post(UploadImage+'{id}', status_code=status.HTTP_204_NO_CONTENT)
async def uploadUserImage(id: str, file: UploadFile = File(...)):
    result = await resultVerification(id)
    imageUrl = save_pic(file=file, folderName='users', fileName=result['name'])
    done = await service.savePicture(id, imageUrl)
    return GetResponse(done, errorMessage="An error occurred while saving user image.")



# Helpers

async def resultVerification(id: ObjectId):
    result = await service.getById(id)
    if result is None:
        raise riseHTTPExceptionIfNotFound(_notFoundMessage)
    return result
