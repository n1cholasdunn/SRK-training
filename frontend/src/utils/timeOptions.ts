export const createTimeOptions = () => {
  const timeOptions = [];
  for (let hour = 6; hour <= 23; hour++) {
    for (let minute = 0; minute < 60; minute += 30) {
      if (hour === 23 && minute == 30) continue;
      const isAM = hour < 12;
      const period = isAM ? 'AM' : 'PM';
      const formattedHour = (hour % 12 || 12).toString().padStart(2, '0');
      const formattedMinute = minute.toString().padStart(2, '0');
      const time = `${formattedHour}:${formattedMinute} ${period}`;
      timeOptions.push(time);
    }
  }
  return timeOptions;
};
