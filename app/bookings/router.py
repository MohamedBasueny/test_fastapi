from datetime import date

from fastapi import APIRouter, Depends, BackgroundTasks, Response
from fastapi_versioning import version
from pydantic import parse_obj_as

from app.bookings.dao import BookingDAO
from app.bookings.schemas import SBooking, SBookingRoomInfo
from app.tasks.tasks import send_booking_confirmation_email
from app.users.dependencies import get_current_user
from app.users.models import Users

router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)


@router.get("")
@version(1)
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBookingRoomInfo]:
    """returns a list of all bookings for user"""
    return await BookingDAO.get_booking_for_user(user)


@router.post("")
@version(1)
async def add_booking(
    # background_tasks: BackgroundTasks,
    room_id: int,
    date_from: date,
    date_to: date,
    user: Users = Depends(get_current_user),
):
    booking = await BookingDAO.add_booking_for_user(user.id, room_id, date_from, date_to)
    booking_dict = parse_obj_as(SBooking, booking).dict()
    # background_tasks.add_task(send_booking_confirmation_email, booking_dict, user.email)
    return booking_dict


@router.delete("/{booking_id}")
@version(1)
async def delete_booking(
    booking_id: int,
    user: Users = Depends(get_current_user),
) -> Response:
    await BookingDAO.delete_booking_for_user(booking_id=int(booking_id), user_id=user.id)
    return Response(status_code=204)
