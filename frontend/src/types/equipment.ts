import { z } from 'zod';

export const EquipmentSchema = z.object({
  name: z.string(),
});

export const ClientEquipmentSchema = z.object({
  equipment: z.array(EquipmentSchema),
});
