from sqlalchemy  import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class StudentDB(Base):
    __tableName__= "students"
    id: Mapped[int] = mapped_column(Integer, unique=True)
    equipment_id: Mapped[int] = mapped_column(Integer, index=True)
    student_id: Mapped[str] = mapped_column(String(8))
    description: Mapped[str] = mapped_column(String(100))
    priority: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column()
