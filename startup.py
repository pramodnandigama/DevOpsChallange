import uvicorn
from mangum import Mangum

from app import application

handler = Mangum(application)

if __name__ == '__main__':
    uvicorn.run("app.main:application", debug=True)
