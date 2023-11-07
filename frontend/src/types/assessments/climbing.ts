import {z} from 'zod';

const PowerEnduranceTest = z.object({
  seconds: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Time in seconds is required'})
    .nullish(),
});
export const PowerEnduranceSchema = z.object({
  tests: z
    .array(PowerEnduranceTest)
    .nonempty({message: 'Requires tests to be created'}),
});
type PowerEndurance = z.infer<typeof PowerEnduranceSchema>;

const MaxPullupsTest = z.object({
  reps: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Number of reps is required'})
    .nullish(),
});
export const MaxPullupsSchema = z.object({
  tests: z
    .array(MaxPullupsTest)
    .nonempty({message: 'Requires tests to be created'}),
});
type MaxPullups = z.infer<typeof MaxPullupsSchema>;

const MaxLockoffTest = z.object({
  seconds: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Time in seconds is required'})
    .nullish(),
});
export const MaxLockoffSchema = z.object({
  tests: z
    .array(MaxLockoffTest)
    .nonempty({message: 'Requires tests to be created'}),
});
type MaxLockoff = z.infer<typeof MaxLockoffSchema>;

const FingerStrengthTest = z.object({
  total_load: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Total load is required'})
    .nullish(),
  percentage_bodyweight: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Percentage of bodyweight is required'})
    .nullish(),
});
export const FingerStrengthSchema = z.object({
  tests: z
    .array(FingerStrengthTest)
    .nonempty({message: 'Requires tests to be created'}),
});
type FingerStrength = z.infer<typeof FingerStrengthSchema>;

const OAFingerStrengthTest = z.object({
  left: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Left is required'})
    .nullish(),
  right: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Right is required'})
    .nullish(),
  left_percentage: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Left percentage is required'})
    .nullish(),
  right_percentage: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Right Percentage is required'})
    .nullish(),
});
export const OAFingerStrengthSchema = z.object({
  tests: z
    .array(OAFingerStrengthTest)
    .nonempty({message: 'Requires tests to be created'}),
});
type OAFingerStrength = z.infer<typeof OAFingerStrengthSchema>;

const OAPinchTest = z.object({
  left: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Left is required'})
    .nullish(),
  right: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Right is required'})
    .nullish(),
});
export const OAPinchSchema = z.object({
  tests: z
    .array(OAPinchTest)
    .nonempty({message: 'Requires tests to be created'}),
});

type OAPinch = z.infer<typeof OAPinchSchema>;

export type AssessmentFormValues = {
  power_endurance: PowerEndurance;
  max_pullups: MaxPullups;
  max_lockoff: MaxLockoff;
  finger_strength: FingerStrength;
  oa_finger_strength: OAFingerStrength;
  oa_pinch_strength: OAPinch;
};

export const AssessmentFormSchema = z.object({
  power_endurance: PowerEnduranceSchema,
  max_pullups: MaxPullupsSchema,
  max_lockoff: MaxLockoffSchema,
  finger_strength: FingerStrengthSchema,
  oa_finger_strength: OAFingerStrengthSchema,
  oa_pinch_strength: OAPinchSchema,
});
