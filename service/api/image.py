from fastapi import HTTPException, Path
from fastapi.responses import FileResponse
import os

ALLOWED_EXTENSIONS = {'png'}
IMAGE_FOLDER = 'images'

def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


async def image(filename: str = Path(...)):
    if not allowed_file(filename):
        raise HTTPException(
            status_code=400,
            detail={
                "error": "Invalid file extension",
                "message": "Image extension should be .png"
            }
        )
    print(f"API – /images/{{filename}} – {filename}")

    file_path = os.path.join(IMAGE_FOLDER, filename)
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail={"error": "File not found"}
        )

    return FileResponse(file_path)
