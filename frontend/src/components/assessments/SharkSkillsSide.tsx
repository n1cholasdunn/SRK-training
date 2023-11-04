import {FieldErrors, UseFormRegister} from 'react-hook-form';
import {AssessmentFormValues} from '../../types/assessments/fitness';

type SharkSkillsSideProps = {
  index: number;
  side:
    | 'practice_left'
    | 'practice_right'
    | 'first_left'
    | 'first_right'
    | 'second_left'
    | 'second_right';
  register: UseFormRegister<AssessmentFormValues>;
  errors?: FieldErrors<AssessmentFormValues>;
};

const getSideName = (side: string) => {
  if (side === 'practice_left') return 'Practice Left';
  if (side === 'practice_right') return 'Practice Right';
  if (side === 'first_left') return 'First Left';
  if (side === 'first_right') return 'First Right';
  if (side === 'second_left') return 'Second Left';
  if (side === 'second_right') return 'Second Right';
};

const SharkSkillsSide = ({
  register,
  index,
  side,
  errors,
}: SharkSkillsSideProps) => {
  return (
    <div className="flex space-y-1">
      <h3 className="mr-2">{getSideName(side)}:</h3>
      <input
        {...register(`shark_skills.assessments.${index}.${side}.time`)}
        defaultValue=""
        placeholder="Time"
      />
      {errors?.shark_skills?.assessments?.[index]?.[side]?.time && (
        <p className="text-red-500 px-2">
          {errors.shark_skills.assessments?.[index]?.[side]?.time?.message}
        </p>
      )}

      <input
        {...register(
          `shark_skills.assessments.${index}.${side}.deduction_tally`
        )}
        defaultValue=""
        placeholder="Deduction Tally"
      />
      {errors?.shark_skills?.assessments?.[index]?.[side]?.deduction_tally && (
        <p className="text-red-500 px-2">
          {
            errors?.shark_skills?.assessments?.[index]?.[side]?.deduction_tally
              ?.message
          }
        </p>
      )}

      <input
        {...register(
          `shark_skills.assessments.${index}.${side}.total_deducted`
        )}
        defaultValue=""
        placeholder="Total Deducted"
      />
      {errors?.shark_skills?.assessments?.[index]?.[side]?.total_deducted && (
        <p className="text-red-500 px-2">
          {
            errors?.shark_skills?.assessments?.[index]?.[side]?.total_deducted
              ?.message
          }
        </p>
      )}

      <input
        {...register(`shark_skills.assessments.${index}.${side}.final_total`)}
        defaultValue=""
        placeholder="Final Total"
      />
      {errors?.shark_skills?.assessments?.[index]?.[side]?.final_total && (
        <p className="text-red-500 px-2">
          {errors.shark_skills.assessments[index]?.[side]?.final_total?.message}
        </p>
      )}
    </div>
  );
};

export default SharkSkillsSide;
