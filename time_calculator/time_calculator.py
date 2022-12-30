def add_time(start, duration, weekday=None):
  new_time = "00:00 AM"
  days_added = 0
  splitted_time = start.split()
  period = splitted_time[1]
  duration_splitted = duration.split(":")
  weekdays = [
    "sunday", "monday", "tuesday", "wednesday", "thursday", "friday",
    "saturday"
  ]

  hour_splitted = splitted_time[0].split(":")

  start_hour = int(hour_splitted[0])
  start_min = int(hour_splitted[1])

  duration_hour = int(duration_splitted[0])
  duration_min = int(duration_splitted[1])

  add_hour = 1 if (((start_min) + duration_min) / 60) > 1 else 0

  new_min = str((start_min + duration_min) % 60).rjust(2, '0')
  new_hour = "12" if (start_hour + duration_hour +
                      add_hour) % 12 == 0 else str(
                        (start_hour + duration_hour + add_hour) % 12)

  passed_period = int(((start_hour + duration_hour + add_hour) / 12) // 1)

  for x in range(passed_period):
    if period == "AM":
      period = "PM"
    elif period == "PM":
      days_added += 1
      period = "AM"

  new_period = period

  addedDaysMessage = str(addDaysMessage(days_added))

  new_weekday = ""
  if weekday is not None:
    actual_index = weekdays.index(weekday.lower())

    if days_added > 0:
      weekday_added = days_added % 7

      for x in range(weekday_added):
        if actual_index == 6:
          actual_index = 0
          continue
        actual_index += 1

    new_weekday = ", " + weekdays[actual_index].capitalize()

  new_time = new_hour + ":" + new_min + " " + new_period + new_weekday + addedDaysMessage
  return new_time


def addDaysMessage(days_added):
  if days_added == 1:
    return " (next day)"
  elif days_added > 1:
    return " (" + str(days_added) + " days later)"
  else:
    return ""


def getNewPeriod(change_period, period):
  if change_period:
    if (period == "AM"):
      return "PM"
    else:
      return "AM"
  else:
    return period
