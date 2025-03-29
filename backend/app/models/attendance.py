from sqlalchemy import Column, String, ForeignKey, DateTime, UniqueConstraint, Integer
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime

class Attendance(Base):
    __tablename__ = "attendances"
    __table_args__ = (
        UniqueConstraint('event_id', 'email', name='unique_attendee'),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    confirmed_at = Column(DateTime, default=datetime.utcnow)

    event_id = Column(Integer, ForeignKey("events.id"))
    event = relationship("Event", back_populates="attendees")
