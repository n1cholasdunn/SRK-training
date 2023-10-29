import {z} from 'zod';

// TODO Have form have different grade options rendered if V scale or font scale chosen have default to vscale
export const ProgramInfoSchema = z.object({
  program_type: z.string().trim(),
  training_style: z.string().trim(),
  payment_rate: z.coerce.number(),
  program_start: z.date({
    required_error: 'Please select a date and time',
    invalid_type_error: 'That is not a valid date',
  }),
  outdoor_max: z
    .string()
    .trim()
    .min(2, {
      message:
        'The grade should be between 2-5 character in either V scale or Font grading',
    })
    .max(5, {
      message:
        'The grade should be between 2-5 character in either V scale or Font grading',
    })
    .optional(),
  outdoor_flash: z
    .string()
    .trim()
    .min(2, {
      message:
        'The grade should be between 2-5 character in either V scale or Font grading',
    })
    .max(5, {
      message:
        'The grade should be between 2-5 character in either V scale or Font grading',
    })
    .optional(),
  indoor_max: z
    .string()
    .trim()
    .min(2, {
      message:
        'The grade should be between 2-5 character in either V scale or Font grading',
    })
    .max(5, {
      message:
        'The grade should be between 2-5 character in either V scale or Font grading',
    })
    .optional(),
  indoor_flash: z
    .string()
    .trim()
    .min(2, {
      message:
        'The grade should be between 2-5 character in either V scale or Font grading',
    })
    .max(5, {
      message:
        'The grade should be between 2-5 character in either V scale or Font grading',
    })
    .optional(),
});
