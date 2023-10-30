import {z} from 'zod';
import {
  vBoulderingGrades,
  fontBoulderingGrades,
  sportFrenchGrades,
  sportYDSGrades,
} from '../utils/climbingGrades';

export const programOptions = [
  'Self-Guided Written w/video consults',
  'Hourly Video Coaching',
  'In-Person Hourly Sessions',
  'In-Person Small Group Sessions',
] as const;

export const trainingStyles = ['Rock Climbing', 'General Fitness'] as const;

const ProgramTypeEnum = z.enum(programOptions, {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  errorMap: (_issue, _ctx) => {
    return {message: 'Please type of program'};
  },
});

const ClimbingGradesEnum = z.enum(
  [
    ...vBoulderingGrades,
    ...fontBoulderingGrades,
    ...sportFrenchGrades,
    ...sportYDSGrades,
  ],
  {
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    errorMap: (_issue, _ctx) => {
      return {message: 'Please choose a grade'};
    },
  }
);

const TrainingStyleEnum = z.enum(trainingStyles, {
  // eslint-disable-next-line @typescript-eslint/no-unused-vars
  errorMap: (_issue, _ctx) => {
    return {message: 'Please your style of training'};
  },
});
// TODO Have form have different grade options rendered if V scale or font scale chosen have default to vscale

export type ProgramFormValues = z.infer<typeof ProgramInfoSchema>;

export const ProgramInfoSchema = z.object({
  program_type: ProgramTypeEnum,
  training_style: TrainingStyleEnum,
  // TODO make this only render in form for superuser else only display without edit perms
  payment_rate: z.coerce.number().optional(),
  program_start: z.date({
    required_error: 'Please select a date and time',
    invalid_type_error: 'That is not a valid date',
  }),
  outdoor_max: ClimbingGradesEnum.optional(),
  outdoor_flash: ClimbingGradesEnum.optional(),
  indoor_max: ClimbingGradesEnum.optional(),
  indoor_flash: ClimbingGradesEnum.optional(),
});
