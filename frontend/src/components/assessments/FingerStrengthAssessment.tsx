import {
  Control,
  FieldErrors,
  UseFormRegister,
  useFieldArray,
} from 'react-hook-form';
import {ClimbingAssessmentFormValues} from '../../types/assessments/climbing';
import {useEffect, useRef} from 'react';

type Props = {
  control: Control<ClimbingAssessmentFormValues>;
  register: UseFormRegister<ClimbingAssessmentFormValues>;
  errors?: FieldErrors<ClimbingAssessmentFormValues>;
};

const FingerStrengthAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'finger_strength.tests',
  });

  const initialRender = useRef(true);

  useEffect(() => {
    if (initialRender.current) {
      append({total_load: undefined, percentage_bodyweight: undefined});
      initialRender.current = false;
    }
  }, [fields, append]);

  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input
            {...register(`finger_strength.tests.${index}.total_load` as const)}
            defaultValue={undefined}
            placeholder="Total Load"
          />
          {errors?.finger_strength?.tests?.[index]?.total_load && (
            <p className={'text-red-500 px-2'}>
              {errors?.finger_strength?.tests?.[index]?.total_load?.message}
            </p>
          )}

          <input
            {...register(
              `finger_strength.tests.${index}.percentage_bodyweight` as const
            )}
            defaultValue={undefined}
            placeholder="% of Bodyweight"
          />
          {errors?.finger_strength?.tests?.[index]?.percentage_bodyweight && (
            <p className={'text-red-500 px-2'}>
              {
                errors?.finger_strength?.tests?.[index]?.percentage_bodyweight
                  ?.message
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
