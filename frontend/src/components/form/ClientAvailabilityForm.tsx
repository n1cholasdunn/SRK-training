import { useEffect, useState } from 'react';
import { checkForOverlap, initialAvailability } from '../../utils/availability';
import { createTimeOptions } from '../../utils/timeOptions';

const ClientAvailabilityForm = () => {
  const [availability, setAvailability] = useState(initialAvailability);
  const [errorMessages, setErrorMessages] = useState<string[]>([]);

  const timeOptions = createTimeOptions();

  const handleTimeChange = (
    dayIndex: number,
    slotIndex: number,
    field: 'from' | 'to',
    value: string
  ) => {
    console.log('handle change start');

    const updatedAvailability = [...availability];
    updatedAvailability[dayIndex].slots[slotIndex][field] = value;
    setAvailability(updatedAvailability);

    const dayAvailability = updatedAvailability[dayIndex];
    const overlapMessage = checkForOverlap(dayAvailability);
    setErrorMessages(prevErrors => {
      const updatedErrors = [...prevErrors];

      updatedErrors[dayIndex] = overlapMessage || '';
      console.log('handle change end');
      return updatedErrors;
    });
    console.log(overlapMessage, 'this is overlap message');
  };
  useEffect(() => {
    console.log(errorMessages);
  }, [errorMessages]);

  const addSlot = (dayIndex: number) => {
    const updatedAvailability = [...availability];
    updatedAvailability[dayIndex].slots.push({ from: '', to: '' });
    setAvailability(updatedAvailability);

    setErrorMessages(prevErrors => {
      const updatedErrors = [...prevErrors];
      updatedErrors[dayIndex] = '';
      return updatedErrors;
    });
  };

  return (
    <div>
      <h2>Set Availability for Each Day</h2>
      <form>
        {availability.map((day, dayIndex) => (
          <div key={day.day}>
            <label>
              {day.day}:
              <br />
              {day.slots.map((slot, slotIndex) => (
                <div key={slotIndex}>
                  From:
                  <select
                    value={slot.from}
                    onChange={e =>
                      handleTimeChange(
                        dayIndex,
                        slotIndex,
                        'from',
                        e.target.value
                      )
                    }
                  >
                    <option value=''>Select Time</option>
                    {timeOptions.map((timeOption, index) => (
                      <option
                        key={index}
                        value={timeOption}
                      >
                        {timeOption}
                      </option>
                    ))}
                  </select>
                  To:
                  <select
                    value={slot.to}
                    onChange={e =>
                      handleTimeChange(
                        dayIndex,
                        slotIndex,
                        'to',
                        e.target.value
                      )
                    }
                  >
                    <option value=''>Select Time</option>
                    {timeOptions.map((timeOption, index) => (
                      <option
                        key={index}
                        value={timeOption}
                      >
                        {timeOption}
                      </option>
                    ))}
                  </select>
                </div>
              ))}
              <button
                type='button'
                onClick={() => addSlot(dayIndex)}
              >
                Add Slot
              </button>
              Comment:
              <input
                type='text'
                value={day.comment}
                onChange={e =>
                  setAvailability(prevAvailability => {
                    const updatedAvailability = [...prevAvailability];
                    updatedAvailability[dayIndex].comment = e.target.value;
                    return updatedAvailability;
                  })
                }
              />
              {errorMessages[dayIndex] && (
                <div className='error'>{errorMessages[dayIndex]}</div>
              )}
            </label>
          </div>
        ))}
      </form>
      <div>
        <h2>Availability:</h2>
        <ul>
          {availability.map(day => (
            <li key={day.day}>
              {day.day}:
              {day.slots.map((slot, slotIndex) => (
                <ul key={slotIndex}>
                  {slot.from && slot.to && (
                    <li>
                      From: {slot.from}, To: {slot.to}
                    </li>
                  )}
                </ul>
              ))}
              {day.comment && <div>Comment: {day.comment}</div>}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default ClientAvailabilityForm;
