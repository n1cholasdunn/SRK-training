import { z } from 'zod';

const SlotSchema = z.object({
  from: z.string().nonempty('From time is required'),
  to: z.string().nonempty('To time is required'),
});

const DaySchema = z.object({
  day: z.string(),
  slots: z.array(SlotSchema),
  comment: z.string(),
});

export const FormValuesSchema = z.object({
  availability: z.array(DaySchema),
});
export type FormData = z.infer<typeof FormValuesSchema>;

export type Day = { day: string; slots: Slot[]; comment: string };

export type Slot = { from: string; to: string };

export type FormValues = {
  availability: Day[];
};

export type AvailabilityField = `availability.${number}.slots.${number}.${
  | 'from'
  | 'to'}`;
