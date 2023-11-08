import {z} from 'zod';

const HealthMarkersTest = z.object({
  weight: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Weight is required'})
    .nullish(),
  bmi: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'BMI is required'})
    .nullish(),
  waist_hip_ratio: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Waist to Hip ratio is required'})
    .nullish(),
  resting_hr: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Resting HR is required'})
    .nullish(),
  blood_pressure: z.string().optional(),
  vo2_max: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'VO2 Max is required'})
    .nullish(),
});

export const HealthMarkersSchema = z.object({
  tests: z
    .array(HealthMarkersTest)
    .nonempty({message: 'Requires tests to be created'}),
});

export type HealthMarkers = z.infer<typeof HealthMarkersSchema>;

const MeasurementsTest = z.object({
  chest: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Chest measurement is required'})
    .nullish(),
  biceps: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Biceps measurement is required'})
    .nullish(),
  forearms: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Forearms measurement is required'})
    .nullish(),
  lower_abdomen: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Lower Abdomen measurement is required'})
    .nullish(),
  hips: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Hips measurement is required'})
    .nullish(),
  upper_thigh: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Upper Thigh measurement is required'})
    .nullish(),
  mid_thigh: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Mid Thigh measurement is required'})
    .nullish(),
  calves: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Calves measurement is required'})
    .nullish(),
});

export const MeasurementsSchema = z.object({
  tests: z
    .array(MeasurementsTest)
    .nonempty({message: 'Requires tests to be created'}),
});

export type Measurements = z.infer<typeof MeasurementsSchema>;

const OverheadSquatTest = z.object({
  foot_ankle: z.string().optional(),
  knee: z.string().optional(),
  lphc: z.string().optional(),
  shoulder: z.string().optional(),
  solutions: z.string().optional(),
});

const OverheadSquatSchema = z.object({
  tests: z
    .array(OverheadSquatTest)
    .nonempty({message: 'Requires tests to be created'}),
});

export type OverheadSquat = z.infer<typeof OverheadSquatSchema>;

const YMCAStepTest = z.object({
  recovery_hr: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Recovery HR is required'})
    .nullish(),
  rating: z.string().optional(),
});

const YMCAStepSchema = z.object({
  tests: z
    .array(YMCAStepTest)
    .nonempty({message: 'Requires tests to be created'}),
});

export type YMCAStep = z.infer<typeof YMCAStepSchema>;

const SitReachTest = z.object({
  first_measurement: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'First measurement is required'})
    .nullish(),

  second_measurement: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Second measurement is required'})
    .nullish(),
  third_measurement: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Third measurement is required'})
    .nullish(),
});

const SitReachSchema = z.object({
  tests: z
    .array(SitReachTest)
    .nonempty({message: 'Requires tests to be created'}),
});

type SitReach = z.infer<typeof SitReachSchema>;

const PushUpTest = z.object({
  num_pushups: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Number of pushups is required'})
    .nullish(),
  completed: z.coerce.boolean(),
});

const PushUpSchema = z.object({
  tests: z
    .array(PushUpTest)
    .nonempty({message: 'Requires tests to be created'}),
});

export type PushUp = z.infer<typeof PushUpSchema>;

const DaviesTest = z.object({
  first_trial: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'First trial is required'})
    .nullish(),
  second_trial: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Second trial is required'})
    .nullish(),
  third_trial: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Third trial is required'})
    .nullish(),
});

const DaviesSchema = z.object({
  tests: z
    .array(DaviesTest)
    .nonempty({message: 'Requires tests to be created'}),
});

export type Davies = z.infer<typeof DaviesSchema>;

const SharkSkillsSide = z.object({
  time: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Time is required'})
    .nullish(),
  deduction_tally: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Deduction tally is required'})
    .nullish(),
  total_deducted: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Total deducted is required'})
    .nullish(),
  final_total: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Final total is required'})
    .nullish(),
});

const SharkSkillsTest = z.object({
  practice_left: SharkSkillsSide,
  practice_right: SharkSkillsSide,
  first_left: SharkSkillsSide,
  first_right: SharkSkillsSide,
  second_left: SharkSkillsSide,
  second_right: SharkSkillsSide,
});

const SharkSkillsSchema = z.object({
  tests: z
    .array(SharkSkillsTest)
    .nonempty({message: 'Requires tests to be created'}),
});

export type SharkSkills = z.infer<typeof SharkSkillsSchema>;

const CoreTest = z.object({
  first_trial: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'First trial is required'})
    .nullish(),
  second_trial: z.coerce
    .number({invalid_type_error: 'This field requires a number'})
    .min(1, {message: 'Second trial is required'})
    .nullish(),
});

const CoreSchema = z.object({
  tests: z.array(CoreTest).nonempty({message: 'Requires tests to be created'}),
});

export type Core = z.infer<typeof CoreSchema>;

export type FitnessAssessmentFormValues = {
  health_markers?: HealthMarkers;
  measurements?: Measurements;
  overhead_squat?: OverheadSquat;
  ymca_step?: YMCAStep;
  sit_reach?: SitReach;
  pushup?: PushUp;
  davies?: Davies;
  shark_skills?: SharkSkills;
  core?: Core;
};

export const FitnessAssessmentFormSchema = z.object({
  health_markers: HealthMarkersSchema,
  measurements: MeasurementsSchema,
  overhead_squat: OverheadSquatSchema,
  ymca_step: YMCAStepSchema,
  sit_reach: SitReachSchema,
  pushup: PushUpSchema,
  davies: DaviesSchema,
  shark_skills: SharkSkillsSchema,
  core: CoreSchema,
});
