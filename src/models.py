from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from src.database import Base


class Schedule(Base):
    __tablename__ = "schedules"
    

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    target_url = Column(String, nullable=False)
    http_method = Column(String, nullable=False)
    headers = Column(Text, nullable=True)
    body = Column(Text, nullable=True)

    schedule_type = Column(String, nullable=False)
    schedule_expression = Column(String, nullable=False)
    timezone = Column(String, default="UTC")

    is_enabled = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_run_at = Column(DateTime(timezone=True), nullable=True)
    next_run_at = Column(DateTime(timezone=True), nullable=True)
    last_status = Column(String, nullable=True)

    logs = relationship("JobExecutionLog", back_populates="schedule", cascade="all, delete-orphan")



class JobExecutionLog(Base):
    __tablename__ = "job_execution_logs" 
    
    id = Column(Integer, primary_key=True, index=True)
    schedule_id = Column(Integer, ForeignKey("schedules.id"), nullable=False)

    run_at = Column(DateTime(timezone=True), server_default=func.now())
    response_status = Column(Integer, nullable=True)
    response_body = Column(Text, nullable=True)
    success = Column(Boolean, default=False)
    error_message = Column(Text, nullable=True)

    schedule = relationship("Schedule", back_populates="logs")