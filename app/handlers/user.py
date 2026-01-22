from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from app.utils.get_weather import get_weather

router = Router()

class get_city(StatesGroup):
    city = State()

@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(get_city.city)
    await message.answer("🌍 Please enter a city name")

@router.message(get_city.city)
async def weather_city(message: Message, state: FSMContext):
    city = message.text
    weather = get_weather(city)

    if isinstance(weather, str):
        await message.answer(weather)
        await state.clear()
        return

    await message.answer(
        f"🌤 Description: {weather['desc'].title()}\n"
        f"🌡 Temperature: {weather['temp'].title()}\n"
        f"🥶 Feels like: {weather['feels'].title()}"
    )
    
    await state.clear()
