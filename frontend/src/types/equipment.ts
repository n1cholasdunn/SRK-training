import {z} from 'zod';

export const EquipmentSchema = z.object({
  name: z
    .string({required_error: 'Equipment is required'})
    .min(1, {message: 'At least 1 piece of equipment is required'}),
});

export type EquipmentFormData = z.infer<typeof EquipmentFormSchema>;

export const EquipmentFormSchema = z.object({
  equipment: z
    .array(EquipmentSchema)
    .nonempty({message: 'Equipment is required'}),
});
