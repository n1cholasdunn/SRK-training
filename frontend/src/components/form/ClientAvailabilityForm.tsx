import { useForm } from 'react-hook-form';
import { checkForOverlap, initialAvailability } from '../../utils/availability';
import { createTimeOptions } from '../../utils/timeOptions';
import {
  FormData,
  FormValues,
  FormValuesSchema,
} from '../../types/availability';
import { useEffect, useState } from 'react';
import { zodResolver } from '@hookform/resolvers/zod';

const ZodClientAvailabilityForm = () => {
  const [forceUpdate, setForceUpdate] = useState(0);

  const timeOptions = createTimeOptions();
  const {
    handleSubmit,
    watch,
    setValue,
    setError,
    clearErrors,
    formState: { errors },
    register,
  } = useForm<FormValues>({
    resolver: zodResolver(FormValuesSchema),
    defaultValues: { availability: initialAvailability },
  });

  const availability = watch('availability', initialAvailability);
  console.log(availability, 'avail');
  console.log(initialAvailability, 'initial');

  const getSlotErrorMessage = (dayIndex: number, slotIndex: number) => {
    return errors.availability?.[dayIndex]?.slots?.[slotIndex]?.message;
  };

  useEffect(() => {
    availability?.forEach((day, dayIndex) => {
      day.slots.forEach((_, slotIndex) => {
        const overlapError = checkForOverlap(day);

        if (overlapError) {
          const { message, slotIndices } = overlapError;

          slotIndices.forEach(index => {
            const errorPath =
              `availability.${dayIndex}.slots.${index}` as const;
            setError(errorPath, { message });
          });

          setForceUpdate(prev => prev + 1);
        } else {
          const errorPath =
            `availability.${dayIndex}.slots.${slotIndex}` as const;
          clearErrors(errorPath);
          setForceUpdate(prev => prev + 1);
        }
      });
    });
  }, [availability, setError, clearErrors, forceUpdate]);

  const addSlot = (dayIndex: number) => {
    setValue(`availability.${dayIndex}.slots`, [
      ...(availability[dayIndex].slots || []),
      { from: '', to: '' },
    ]);
  };

  const onSubmit = (data: FormData) => {
    try {
      FormValuesSchema.parse(data);
      console.log(data);

      // TODO add submit logic
    } catch (error) {
      // TODO add error handling
    }
  };

  return (
    <div>
      <h2>Set Availability for Each Day</h2>
      <form onSubmit={handleSubmit(onSubmit)}>
        {availability && availability.length > 0 ? (
          availability.map((day, dayIndex) => (
            <div key={day.day}>
              <label>
                {day.day}:
                <br />
                {day.slots && day.slots.length > 0 ? (
                  day.slots.map((_, slotIndex) => (
                    <div key={slotIndex}>
                      From:
                      <select
                        {...register(
                          `availability.${dayIndex}.slots.${slotIndex}.from`
                        )}
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
                        {...register(
                          `availability.${dayIndex}.slots.${slotIndex}.to`
                        )}
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
                      {getSlotErrorMessage(dayIndex, slotIndex) && (
                        <div className='error'>
                          <p className='text-red-600'>
                            {getSlotErrorMessage(dayIndex, slotIndex)}
                          </p>
                        </div>
                      )}
                    </div>
                  ))
                ) : (
                  <p>No slots added</p>
                )}
                <button
                  type='button'
                  onClick={() => addSlot(dayIndex)}
                  className='bg-red-200 rounded py-1 px-2 m-1'
                >
                  Add Slot
                </button>
              </label>
            </div>
          ))
        ) : (
          <p>No availability data</p>
        )}

        <button type='submit'>Submit</button>
      </form>
    </div>
  );
};

export default ZodClientAvailabilityForm;
