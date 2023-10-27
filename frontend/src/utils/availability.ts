import { Day } from '../types/availability';

export const initialAvailability: Day[] = [
  {
    day: 'Monday',
    slots: [],
    comment: '',
  },
  {
    day: 'Tuesday',
    slots: [],
    comment: '',
  },
  {
    day: 'Wednesday',
    slots: [],
    comment: '',
  },
  {
    day: 'Thursday',
    slots: [],
    comment: '',
  },
  {
    day: 'Friday',
    slots: [],
    comment: '',
  },
  {
    day: 'Saturday',
    slots: [],
    comment: '',
  },
  {
    day: 'Sunday',
    slots: [],
    comment: '',
  },
];

export function checkForOverlap(
  availability: (typeof initialAvailability)[number]
): { message: string; slotIndices: [number, number] } | null {
  const slots = availability.slots;

  for (let i = 0; i < slots.length; i++) {
    const slotA = slots[i];
    const startTimeA = parseTime(slotA.from);
    const endTimeA = parseTime(slotA.to);

    if (startTimeA >= endTimeA) {
      return {
        message: `Start time must be earlier than end time in slot ${slotA.from} - ${slotA.to}`,
        slotIndices: [i, i],
      };
    }

    for (let j = i + 1; j < slots.length; j++) {
      const slotB = slots[j];
      const startTimeB = parseTime(slotB.from);
      const endTimeB = parseTime(slotB.to);

      if (startTimeA < endTimeB && endTimeA > startTimeB) {
        return {
          message: `Overlapping slots detected: ${slotA.from} - ${slotA.to} and ${slotB.from} - ${slotB.to}`,
          slotIndices: [i, j],
        };
      }
    }
  }

  return null;
}

// export function checkForOverlap(
//   availability: (typeof initialAvailability)[number]
// ): string | null {
//   const slots = availability.slots;

//   for (let i = 0; i < slots.length; i++) {
//     const slot = slots[i];

//     const startTime = parseTime(slot.from);
//     const endTime = parseTime(slot.to);

//     // Check if the start time is greater than or equal to the end time
//     if (startTime >= endTime) {
//       const invalidTimeMessage = `Invalid time slot: ${slot.from} - ${slot.to}. The start time must be earlier than the end time.`;
//       return invalidTimeMessage;
//     }

//     for (let j = i + 1; j < slots.length; j++) {
//       const compareSlot = slots[j];

//       const compareStartTime = parseTime(compareSlot.from);
//       const compareEndTime = parseTime(compareSlot.to);

//       if (
//         (startTime >= compareStartTime && startTime < compareEndTime) ||
//         (endTime > compareStartTime && endTime <= compareEndTime) ||
//         (compareStartTime >= startTime && compareStartTime < endTime) ||
//         (compareEndTime > startTime && compareEndTime <= endTime)
//       ) {
//         const overlapMessage = `Overlapping time slots: ${slot.from} - ${slot.to} and ${compareSlot.from} - ${compareSlot.to}`;
//         return overlapMessage;
//       }
//     }
//   }

//   console.log('No overlap detected');
//   return null;
// }

const parseTime = (timeString: string): Date => {
  const [hour, minute, period] = timeString.split(/[ :]/);

  // Convert to 24-hour format
  let hourValue = parseInt(hour, 10);
  if (period === 'PM' && hourValue < 12) {
    hourValue += 12;
  } else if (period === 'AM' && hourValue === 12) {
    hourValue = 0;
  }

  return new Date(1970, 0, 1, hourValue, parseInt(minute, 10));
};
