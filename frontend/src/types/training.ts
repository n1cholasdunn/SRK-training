import {z} from 'zod';

//covers prehab and gym training but otw adds warmup
const TrainingExercise = z.object({
  name: z.string().min(1, {message: 'Name is required'}),
  equipment_used: z.string().min(1, {message: 'Please specify equipment used'}),
  rest: z.string().min(1, {message: 'Rest amount is required'}),
  sets: z.string().min(1, {message: 'Sets are required'}),
  notes: z.string().optional(),
});

const OTWTrainingPlanSchema = z.object({
  warmup: z.string().min(1, {message: 'A warmup is required'}),
  exercises: z
    .array(TrainingExercise)
    .nonempty({message: 'Training exercises are required'}),
});
type OTWTrainingPlan = z.infer<typeof OTWTrainingPlanSchema>;

const TrainingPlanSchema = z.object({
  exercises: z
    .array(TrainingExercise)
    .nonempty({message: 'Training exercises are required'}),
});
type TrainingPlan = z.infer<typeof TrainingPlanSchema>;

export const TrainingFormSchema = z.object({
  otw_training: OTWTrainingPlanSchema,
  gym_training: TrainingPlanSchema,
  prehab_training: TrainingPlanSchema,
});

export type TrainingFormValues = {
  otw_training: OTWTrainingPlan;
  gym_training: TrainingPlan;
  prehab_training: TrainingPlan;
};
