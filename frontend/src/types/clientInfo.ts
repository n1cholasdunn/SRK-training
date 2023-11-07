import {z} from 'zod';

export type ClientFormValues = z.infer<typeof ClientInfoSchema>;

export const ClientInfoSchema = z.object({
  name: z
    .string()
    .trim()
    .min(2, {message: 'Name must be more than 2 characters long'}),
  phone: z
    .string()
    .min(10, {
      message: `Phone number must include a '+' follow the E.164 format (e.g., +1234567890)`,
    })
    .max(14, {
      message: `Phone number must include a '+' follow the E.164 format (e.g., +1234567890)`,
    })
    .refine(val => /^\+\d{1,14}$/.test(val), {
      message: `Phone number must include a '+' follow the E.164 format (e.g., +1234567890)`,
    }),
  age: z.coerce.number().min(2, {message: 'Age must be 2 digits'}),
  email: z
    .string()
    .email({message: 'Please enter a valid email'})
    .trim()
    .toLowerCase(),
  address: z
    .string()
    .min(8, {message: `This doesn't seem to be a valid address`}),
  emergency_contact: z
    .string()
    .trim()
    .min(2, {message: 'Name must be more than 2 characters long'}),
  emergency_phone: z
    .string()
    .min(10, {message: 'Phone numbers are minimum of 10 digits'}),
  height: z.string().min(1, {message: 'Height is required'}).trim(),
  weight: z.coerce.number().min(1, {message: 'Weight is required'}),
  ape_index: z
    .string({description: 'Your wingspan minus your height'})
    .trim()
    .optional(),
  occupation: z
    .string({description: 'Tell me about your work'})
    .trim()
    .optional(),
  hobbies: z
    .string({description: 'Tell me about your hobbies'})
    .trim()
    .optional(),
  primary_goals: z
    .string({
      required_error:
        'Please include your primary goals of recieving coaching/training',
    })
    .max(255, 'Maximum characters is 255')
    .trim(),
  health_concerns: z
    .string({
      required_error:
        'Please fill in required health concerns or select Not Applicable',
    })
    .trim(),
  parq_complete: z.boolean({
    required_error: 'Please complete PAR-Q waiver and then select completed',
  }),
  liablitiy_waiver: z.boolean({
    required_error:
      'Please complete the liability waiver and then select completed',
  }),
});
