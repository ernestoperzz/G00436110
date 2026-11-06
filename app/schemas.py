from typing import Annotated

from pydantic import BaseModel, ConfigDict,StringConstraints, Field

student_id_str = Annotated[str, StringConstraints(pattern= r"^ST^{4}")] 
descriptionStr = Annotated[str, StringConstraints(min_length=5, max_length= 100)]

class StudentCreate(BaseModel):
    description: descriptionStr
    equipment_id: int = Field(gt = 0)
    student_id: student_id_str
    priority: int= Field(gt =1 , lt = 5)
    status: "open"

class StudentRead(BaseModel):
    model_config = ConfigDict(from_attributes= True)
    id:int
    equipment_id = int
    student_id = student_id_str
    priority:int 
    status: "open"