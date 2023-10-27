import { Day } from '../types/availability';

export const initialAvailability: Day[] = [
  {
    day: 'mon',
    slots: [{ from: '', to: '' }],
    comment: '',
  },
  {
    day: 'tue',
    slots: [{ from: '', to: '' }],
    comment: '',
  },
  {
    day: 'wed',
    slots: [{ from: '', to: '' }],
    comment: '',
  },
  {
    day: 'thu',
    slots: [{ from: '', to: '' }],
    comment: '',
  },
  {
    day: 'fri',
    slots: [{ from: '', to: '' }],
    comment: '',
  },
  {
    day: 'sat',
    slots: [{ from: '', to: '' }],
    comment: '',
  },
  {
    day: 'sun',
    slots: [{ from: '', to: '' }],
    comment: '',
  },
];

// console.log(startTimeA, 'startA');
// console.log(endTimeA, 'endA');
// console.log(startTimeB, 'startB');
// console.log(endTimeB, 'endB');

export function checkForOverlap(
  availability: (typeof initialAvailability)[number]
): string | null {
  const slots = availability.slots;

  for (let i = 0; i < slots.length; i++) {
    for (let j = i + 1; j < slots.length; j++) {
      const slotA = slots[i];
      const slotB = slots[j];

      const startTimeA = parseTime(slotA.from);
      console.log(startTimeA, 'startA');
      const endTimeA = parseTime(slotA.to);
      console.log(endTimeA, 'endA');
      const startTimeB = parseTime(slotB.from);
      console.log(startTimeB, 'startB');
      const endTimeB = parseTime(slotB.to);
      console.log(endTimeB, 'endB');

      if (startTimeA < endTimeB && endTimeA > startTimeB) {
        const overlapMessage = `Overlapping time slots: ${slotA.from} - ${slotA.to} and ${slotB.from} - ${slotB.to}`;
        console.log(overlapMessage);
        return overlapMessage;
      }
    }
  }

  console.log('No overlap detected');
  return null;
}

function parseTime(timeString: string): Date {
  const [hour, minute, period] = timeString.split(/[ :]/);

  // Convert to 24-hour format
  let hourValue = parseInt(hour, 10);
  if (period === 'PM' && hourValue < 12) {
    hourValue += 12;
  } else if (period === 'AM' && hourValue === 12) {
    hourValue = 0;
  }

  return new Date(1970, 0, 1, hourValue, parseInt(minute, 10));
}
