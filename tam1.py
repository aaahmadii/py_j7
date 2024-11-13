
from datetime import datetime


birth_date_input = input("لطفا تاریخ تولد خود را به فرمت YYYY-MM-DD وارد کنید: ")


birth_date = datetime.strptime(birth_date_input, "%Y-%m-%d")

today = datetime.now()

days_lived = (today - birth_date).days


print(f"شما {days_lived} روز از زندگی خود را گذرانده‌اید.")


