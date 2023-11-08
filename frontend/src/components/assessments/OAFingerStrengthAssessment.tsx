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

const OAFingerStrengthAssessment = ({control, register, errors}: Props) => {
  const {fields, append, remove} = useFieldArray({
    control,
    name: 'oa_finger_strength.tests',
  });

  const initialRender = useRef(true);

  useEffect(() => {
    if (initialRender.current) {
      append({
        left: undefined,
        right: undefined,
        left_percentage: undefined,
        right_percentage: undefined,
      });
      initialRender.current = false;
    }
  }, [append]);

  return (
    <>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input
            {...register(`oa_finger_strength.tests.${index}.left` as const)}
            defaultValue={undefined}
            placeholder="Total load Left Hand"
          />
          {errors?.oa_finger_strength?.tests?.[index]?.left && (
            <p className={'text-red-500 px-2'}>
              {errors?.oa_finger_strength?.tests?.[index]?.left?.message}
            </p>
          )}

          <input
            {...register(`oa_finger_strength.tests.${index}.right` as const)}
            defaultValue={undefined}
            placeholder="Total load Right Hand"
          />
          {errors?.oa_finger_strength?.tests?.[index]?.right && (
            <p className={'text-red-500 px-2'}>
              {errors?.oa_finger_strength?.tests?.[index]?.right?.message}
            </p>
          )}
          <input
            {...register(
              `oa_finger_strength.tests.${index}.left_percentage` as const
            )}
            defaultValue={undefined}
            placeholder="% of Bodyweight Left Hand"
          />
          {errors?.oa_finger_strength?.tests?.[index]?.left_percentage && (
            <p className={'text-red-500 px-2'}>
              {
                errors?.oa_finger_strength?.tests?.[index]?.left_percentage
                  ?.message
              }
            </p>
          )}

          <input
            {...register(
              `oa_finger_strength.tests.${index}.right_percentage` as const
            )}
            defaultValue={undefined}
            placeholder="% of Bodyweight Right Hand"
          />
          {errors?.oa_finger_strength?.tests?.[index]?.right_percentage && (
            <p className={'text-red-500 px-2'}>
              {
                errors?.oa_finger_strength?.tests?.[index]?.right_percentage
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
          append({
            left: undefined,
            right: undefined,
            left_percentage: undefined,
            right_percentage: undefined,
          })
        }>
        Add One Arm Finger Strength Test
      </button>
    </>
  );
};

export default OAFingerStrengthAssessment;
