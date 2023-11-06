import {z} from 'zod';

export const ContactFormSchema = z.object({
  sender_email: z.string().email().min(1, {message: 'Email is required'}),
  message: z.string().min(1, {message: 'A message is required'}),
});

export type ContactFormValues = z.infer<typeof ContactFormSchema>;
