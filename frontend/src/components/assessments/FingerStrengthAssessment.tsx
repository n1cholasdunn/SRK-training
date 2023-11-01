import {
  Control,
  FieldErrors,
  UseFormRegister,
  useFieldArray,
} from 'react-hook-form';
import {AssessmentFormValues} from '../../types/assessments/climbing';
import {useEffect} from 'react';

type Props = {
  control: Control<AssessmentFormValues>;
  register: UseFormRegister<AssessmentFormValues>;
  errors?: FieldErrors<AssessmentFormValues>;
};

const FingerStrengthAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'finger_strength.assessments',
  });

  useEffect(() => {
    if (fields.length === 0) {
      append({total_load: undefined, percentage_bodyweight: undefined});
    }
  }, [fields, append]);

  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input
            {...register(
              `finger_strength.assessments.${index}.total_load` as const
            )}
            defaultValue={undefined}
            placeholder="Total Load"
          />
          {errors?.finger_strength?.assessments?.[index]?.total_load && (
            <p className={'text-red-500 px-2'}>
              {
                errors?.finger_strength?.assessments?.[index]?.total_load
                  ?.message
              }
            </p>
          )}

          <input
            {...register(
              `finger_strength.assessments.${index}.percentage_bodyweight` as const
            )}
            defaultValue={undefined}
            placeholder="% of Bodyweight"
          />
          {errors?.finger_strength?.assessments?.[index]
            ?.percentage_bodyweight && (
            <p className={'text-red-500 px-2'}>
              {
                errors?.finger_strength?.assessments?.[index]
                  ?.percentage_bodyweight?.message
              }
            </p>
          )}
          {fields.length > 1 && (
            <button type="button" onClick={() => remove(index)}>
              Remove
            </button>
          )}
        </div>
      ))}
      <button
        type="button"
        onClick={() =>
          append({total_load: undefined, percentage_bodyweight: undefined})
        }>
        Add Finger Strength Test
      </button>
    </>
  );
};

export default FingerStrengthAssessment;
