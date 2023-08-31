import math
import numpy as np
import h5py

from sqlalchemy.orm import Session
from fastapi import UploadFile

from PIL import Image
Image.MAX_IMAGE_PIXELS = 933120000

from app import crud
from app.schemas.task import TaskBase


class ProjectWorker():
    def __init__(self, project_name:str) -> None:
        self.project_name:str = project_name
        self.project_path:str = self.build_path() 
    
    def build_path(self) -> str:
        path = f'projects/{self.project_name}.hdf'
        return path

    def get_count_layers(self, w:int, h:int) -> int:
        col_layer = 0
        while w>1000 or h>1000:
            col_layer += 1
            w /= 2
            h /= 2
        if col_layer == 0:
            col_layer = 1
        return col_layer

    def add_task_db(self, db:Session, task_in:TaskBase):
            crud.task.create(db, task_in)

    def add_task(self,db:Session, hdf:h5py.File, image:UploadFile, index:int):
        img = Image.open(image.file)
        task_folder = hdf.create_group(str(index))

        w = img.size[0]
        h = img.size[1]
        count_layers = self.get_count_layers(w,h)

        task = TaskBase(id=index,
                        project_name=self.project_name,
                        file_name=image.filename,
                        width=w,
                        height=h,
                        layers_count=count_layers,
                        status='OK')
        self.add_task_db(db, task_in=task)

        for i in range(count_layers):
            if i == 0:
                desc = 1
            else:
                desc = 2
            width = int(img.size[0]/(desc))
            height = int(img.size[1]/(desc))
            img = img.resize((width, height))

            layer = task_folder.create_group(f"layer_{i}")
            for sampl_h in range(math.ceil(height/256)):
                for sampl_w in range(math.ceil(width/256)):
                    start_p = [sampl_w*256, sampl_h*256]
                    end_p = [(sampl_w+1)*256, (sampl_h+1)*256]
                    if ((sampl_w+1)*256) > width:
                        end_p[0] = width
                    if ((sampl_h+1)*256) > height:
                        end_p[1] = height
                    sample = img.crop((start_p[0],start_p[1], end_p[0], end_p[1]))
                    layer.create_dataset(f'{sampl_w}:{sampl_h}', data=np.asarray(sample, dtype='uint8'))

    def add_tasks(self,db, hdf:h5py.File, images:list[UploadFile]):
        for index, image in enumerate(images):
            self.add_task(db, hdf, image, index)

    def create_project(self,db:Session, images:list[UploadFile]) -> None:
        with h5py.File(self.project_path, 'w-') as hdf:
            self.add_tasks(db, hdf, images)
